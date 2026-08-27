import re
from urllib.parse import unquote

import pytest

from ui_avatars import Avatars, avatar_url, avatars


def test_requires_name_or_email():
    with pytest.raises(ValueError, match="requires at least one"):
        avatar_url()


def test_avatar_url_delegates_to_the_shared_avatars_instance(name, email):
    assert avatar_url(name=name, email=email) == avatars.build(name=name, email=email)


def test_reconfiguring_the_shared_instance_changes_the_shortcut(name, restore_defaults):
    restore_defaults.configure(colors=["abcdef"])
    assert "/abcdef/" in avatar_url(name=name)


def test_fresh_default_configuration_matches_the_shortcut(name, email):
    assert Avatars().build(name=name, email=email) == avatar_url(name=name, email=email)


def test_without_email_is_direct_ui_avatars_url(name):
    url = avatar_url(name=name)
    assert url.startswith("https://ui-avatars.com/api/Ada%20Lovelace/")
    assert "gravatar" not in url


def test_without_email_uses_svg(name):
    assert avatar_url(name=name).endswith("/svg")


def test_with_email_uses_png(name, email):
    assert avatar_url(name=name, email=email).endswith("%2Fpng")


def test_with_email_wraps_in_gravatar(name, email):
    url = avatar_url(name=name, email=email)
    assert url.startswith("https://www.gravatar.com/avatar/")
    assert "ui-avatars.com" in url


def test_without_name_derives_initials_from_email(email):
    url = avatar_url(email=email)
    assert "%2Fad%2F" in url


def test_derived_initials_skip_non_letters_in_the_local_part():
    url = avatar_url(email="42.john@example.com")
    assert "%2Fjo%2F" in url


def test_derived_initials_fall_back_to_raw_characters_when_no_letters_exist():
    url = avatar_url(email="42@example.com")
    assert "%2F42%2F" in url


def test_derived_initials_strip_whitespace_before_the_no_letters_fallback():
    url = avatar_url(email="  42@example.com")
    assert "%2F42%2F" in url
    assert "%2520" not in url


def test_derived_initials_never_come_from_the_email_domain():
    url = avatar_url(email="42@example.com")
    assert "%2Fex%2F" not in url


def test_is_deterministic(name):
    assert avatar_url(name=name) == avatar_url(name=name)


def test_gravatar_hash_matches_email_hash(name, email):
    import hashlib

    digest = hashlib.md5(email.encode(), usedforsecurity=False).hexdigest()
    assert digest in avatar_url(name=name, email=email)


def test_color_is_picked_from_email_not_name_when_both_given(name, email):
    def color(url):
        return re.search(r"/([0-9a-f]{6})/2/0\.4/0/1/1/", unquote(url)).group(1)

    with_ada = avatar_url(name=name, email=email)
    with_other_name = avatar_url(name="Someone Else", email=email)
    assert color(with_ada) == color(with_other_name)


def test_color_differs_from_email_when_no_email_given():
    by_name = avatar_url(name="Ada Lovelace")
    by_different_name = avatar_url(name="Grace Hopper")
    assert by_name != by_different_name


def test_email_is_case_and_whitespace_insensitive_for_the_gravatar_hash():
    def gravatar_digest(url):
        return url.removeprefix("https://www.gravatar.com/avatar/").split("?")[0]

    padded = avatar_url(email=" Ada@Example.com ")
    plain = avatar_url(email="ada@example.com")
    assert gravatar_digest(padded) == gravatar_digest(plain)


def test_name_is_url_encoded():
    url = avatar_url(name="José García")
    assert "é" not in url
    assert "%20" in url or "+" in url


def test_svg_background_carries_alpha_suffix_on_hex_color(name):
    url = avatar_url(name=name)
    background = url.split("/128/")[1].split("/")[0]
    text = url.split("/128/")[1].split("/")[1]
    # default alpha 0.2 * 255 = 51 = 0x33
    assert background == f"{text}33"


def test_png_background_is_rgba_of_the_hex_color(name, email):
    url = unquote(avatar_url(name=name, email=email))
    match = re.search(r"/128/rgba\((\d+),(\d+),(\d+),0\.2\)/([0-9a-f]{6})/", url)
    assert match
    r, g, b, text = match.groups()
    assert (int(r), int(g), int(b)) == tuple(
        int(text[i : i + 2], 16) for i in (0, 2, 4)
    )


def test_size_can_be_overridden_per_call(name):
    assert "/64/" in avatar_url(name=name, size=64)


def test_source_can_be_overridden_per_call(name, email):
    url = avatar_url(name=name, email=email, source="libravatar")
    assert url.startswith("https://seccdn.libravatar.org/avatar/")


def test_format_can_be_overridden_per_call(name, email):
    url = avatar_url(name=name, email=email, format="svg")
    assert url.endswith("%2Fsvg")


def test_ui_avatars_options_can_be_overridden_per_call(name):
    url = avatar_url(
        name=name, length=1, font_size=0.5, rounded=True, bold=False, uppercase=False
    )
    assert url.endswith("/1/0.5/1/0/0/svg")


def test_alpha_can_be_overridden_per_call(name, restore_defaults):
    restore_defaults.configure(colors=["#000000"])
    url = avatar_url(name=name, alpha=0.5)
    assert "/00000080/" in url


def test_color_forces_the_same_color_regardless_of_name():
    ada = avatar_url(name="Ada Lovelace", color="#dc2626")
    grace = avatar_url(name="Grace Hopper", color="#dc2626")
    assert "/dc262633/dc2626/" in ada
    assert "/dc262633/dc2626/" in grace


def test_color_combines_with_font_color(name):
    url = avatar_url(name=name, color="#fee2e2", font_color="#dc2626")
    assert "/fee2e233/dc2626/" in url


def test_color_accepts_shorthand_hex(name):
    url = avatar_url(name=name, color="#fff")
    assert "/ffffff33/ffffff/" in url


def test_color_does_not_mutate_the_shared_avatars_instance(name):
    before = avatars.colors
    avatar_url(name=name, color="#dc2626")
    assert avatars.colors == before


def test_hash_prefixed_colors_do_not_leak_a_literal_hash_into_the_url(
    name, restore_defaults
):
    restore_defaults.configure(colors=["#000000"])
    url = avatar_url(name=name)
    assert "/000000/" in url
    assert "#" not in url


def test_per_call_overrides_do_not_mutate_the_shared_avatars_instance(name):
    before = (avatars.bold, avatars.size)
    avatar_url(name=name, bold=False, size=64)
    assert (avatars.bold, avatars.size) == before
