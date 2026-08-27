import re
from urllib.parse import unquote

import pytest

from ui_avatars import Avatars, avatars


def test_instance_requires_name_or_email():
    with pytest.raises(ValueError, match="requires at least one"):
        Avatars().build()


def test_all_colors_are_valid_hex_triples():
    assert Avatars.COLORS
    for color in Avatars.COLORS:
        assert re.fullmatch(r"#[0-9a-f]{6}", color)


def test_all_colors_are_unique():
    assert len(Avatars.COLORS) == len(set(Avatars.COLORS))


def test_default_instance_uses_the_default_palette():
    assert Avatars().colors == Avatars.COLORS


def test_custom_colors_are_used_instead_of_the_default_palette(name):
    avatars = Avatars(colors=["000000"])
    url = avatars.build(name=name)
    assert "/000000/" in url


def test_hash_prefixed_colors_are_stripped_before_building_the_url(name):
    avatars = Avatars(colors=["#000000"])
    url = avatars.build(name=name)
    assert "/000000/" in url
    assert "#" not in url


def test_shorthand_hex_colors_are_expanded_to_six_digits(name):
    avatars = Avatars(colors=["#fff"])
    url = avatars.build(name=name)
    assert "/ffffff33/ffffff/" in url


def test_shorthand_hex_colors_do_not_crash_the_png_path(name, email):
    avatars = Avatars(colors=["#fff"])
    url = unquote(avatars.build(name=name, email=email))
    assert "rgba(255,255,255,0.2)" in url
    assert "/ffffff/" in url


def test_shorthand_hex_works_in_tuple_color_entries(name):
    avatars = Avatars(colors=[("#fff", "#f00")])
    url = avatars.build(name=name)
    assert "/ffffff33/ff0000/" in url


def test_custom_colors_list_is_copied_not_referenced():
    colors = ["000000", "ffffff"]
    avatars = Avatars(colors=colors)
    colors.append("123456")
    assert avatars.colors == ["000000", "ffffff"]


def test_tuple_color_entries_pick_background_and_text_independently(name):
    avatars = Avatars(colors=[("#fee2e2", "#ef4444")])
    url = avatars.build(name=name)
    background, text = re.search(
        r"/([0-9a-f]{6})[0-9a-f]{2}/([0-9a-f]{6})/2/", url
    ).groups()
    assert background == "fee2e2"
    assert text == "ef4444"


def test_tuple_color_entries_still_apply_alpha_to_the_background(name):
    avatars = Avatars(colors=[("#fee2e2", "#ef4444")])
    url = avatars.build(name=name)
    # default alpha 0.2 * 255 = 51 = 0x33
    assert "/fee2e233/ef4444/" in url


def test_tuple_color_entries_can_be_made_fully_opaque_via_alpha(name):
    avatars = Avatars(colors=[("#fee2e2", "#ef4444")], alpha=1)
    url = avatars.build(name=name)
    assert "/fee2e2ff/ef4444/" in url


def test_opaque_single_color_keeps_the_text_the_same_hue(name):
    avatars = Avatars(colors=["#ef4444"], alpha=1)
    url = avatars.build(name=name)
    assert "/ef4444ff/ef4444/" in url


def test_font_color_overrides_the_palette_derived_text_color(name):
    avatars = Avatars(colors=[("#fee2e2", "#ef4444")])
    url = avatars.build(name=name, font_color="#fff")
    assert "/ffffff/" in url
    assert "ef4444" not in url


def test_font_color_overrides_regardless_of_alpha(name):
    avatars = Avatars(colors=["#ef4444"], alpha=1)
    url = avatars.build(name=name, font_color="#000")
    assert "/ef4444ff/000000/" in url


def test_configure_sets_a_persistent_font_color_override(name):
    avatars = Avatars(colors=[("#fee2e2", "#ef4444")]).configure(font_color="#fff")
    url = avatars.build(name=name)
    assert "/ffffff/" in url
    assert "ef4444" not in url


def test_background_overrides_the_palette_derived_background(name):
    avatars = Avatars(colors=[("#fee2e2", "#ef4444")])
    url = avatars.build(name=name, background="#000", alpha=1)
    assert "/000000ff/ef4444/" in url


def test_configure_sets_a_persistent_background_override(name):
    avatars = Avatars(alpha=1).configure(background="#000000")
    ada = avatars.build(name=name)
    grace = avatars.build(name="Grace Hopper")
    assert "/000000ff/" in ada
    assert "/000000ff/" in grace
    assert ada.split("/000000ff/")[1] != grace.split("/000000ff/")[1]


def test_tuple_color_entries_apply_alpha_on_the_png_path_too(name, email):
    avatars = Avatars(colors=[("#fee2e2", "#ef4444")])
    url = unquote(avatars.build(name=name, email=email))
    assert "rgba(254,226,226,0.2)" in url
    assert "/ef4444/" in url


def test_colors_list_can_mix_plain_hex_and_tuple_entries(name):
    avatars = Avatars(colors=["#3b82f6", ("#fee2e2", "#ef4444")])
    url = avatars.build(name=name)
    assert any(color in url for color in ("3b82f6", "fee2e2"))


def test_separate_instances_do_not_share_configuration(name):
    red_only = Avatars(colors=["ff0000"])
    blue_only = Avatars(colors=["0000ff"])
    assert "/ff0000/" in red_only.build(name=name)
    assert "/0000ff/" in blue_only.build(name=name)


def test_custom_size_appears_in_the_ui_avatars_url(name):
    avatars = Avatars(size=256)
    url = avatars.build(name=name)
    assert "/256/" in url


def test_custom_size_is_passed_through_to_gravatars_s_param(name, email):
    avatars = Avatars(size=256)
    url = avatars.build(name=name, email=email)
    assert url.startswith("https://www.gravatar.com/avatar/")
    assert "?s=256&d=" in url


def test_default_size_is_128():
    assert Avatars().size == 128


def test_default_source_is_gravatar():
    assert Avatars().source == "gravatar"


def test_source_selects_the_photo_host(name, email):
    url = Avatars().build(name=name, email=email, source="libravatar")
    assert url.startswith("https://seccdn.libravatar.org/avatar/")


def test_unknown_source_raises(name, email):
    with pytest.raises(ValueError, match="unknown source"):
        Avatars().build(name=name, email=email, source="notarealsource")


def test_unknown_source_raises_even_without_email(name):
    with pytest.raises(ValueError, match="unknown source"):
        Avatars().build(name=name, source="notarealsource")


def test_custom_host_without_a_scheme_defaults_to_https(name, email):
    url = Avatars().build(name=name, email=email, source="avatars.example.com")
    assert url.startswith("https://avatars.example.com/avatar/")


def test_custom_host_keeps_an_explicit_scheme(name, email):
    url = Avatars().build(name=name, email=email, source="https://avatars.example.com")
    assert url.startswith("https://avatars.example.com/avatar/")


def test_configure_updates_source_in_place():
    avatars = Avatars()
    avatars.configure(source="libravatar")
    assert avatars.source == "libravatar"


def test_source_can_be_overridden_per_call_without_mutating_the_instance(name, email):
    avatars = Avatars()
    url = avatars.build(name=name, email=email, source="libravatar")
    assert "libravatar" in url
    assert avatars.source == "gravatar"


def test_default_format_is_none():
    assert Avatars().format is None


def test_email_with_gravatar_defaults_to_png(name, email):
    url = Avatars().build(name=name, email=email)
    assert url.endswith("%2Fpng")


def test_email_with_libravatar_defaults_to_svg(name, email):
    url = Avatars().build(name=name, email=email, source="libravatar")
    assert url.endswith("%2Fsvg")


def test_no_email_defaults_to_svg_regardless_of_source(name):
    url = Avatars().build(name=name, source="libravatar")
    assert url.endswith("/svg")


def test_format_can_force_svg_on_gravatar_even_though_it_is_broken_there(name, email):
    url = Avatars().build(name=name, email=email, format="svg")
    assert url.endswith("%2Fsvg")


def test_format_can_force_png_on_libravatar(name, email):
    url = Avatars().build(name=name, email=email, source="libravatar", format="png")
    assert url.endswith("%2Fpng")


def test_format_can_force_png_without_an_email(name):
    url = Avatars().build(name=name, format="png")
    assert url.endswith("/png")


def test_unknown_format_raises(name, email):
    with pytest.raises(ValueError, match="unknown format"):
        Avatars().build(name=name, email=email, format="webp")


def test_unknown_format_raises_even_without_email(name):
    with pytest.raises(ValueError, match="unknown format"):
        Avatars().build(name=name, format="webp")


def test_configure_updates_format_in_place():
    avatars = Avatars()
    avatars.configure(format="png")
    assert avatars.format == "png"


def test_format_can_be_overridden_per_call_without_mutating_the_instance(name):
    avatars = Avatars(format="png")
    url = avatars.build(name=name, format="svg")
    assert url.endswith("/svg")
    assert avatars.format == "png"


def test_default_ui_avatars_options_match_the_original_hardcoded_values(name):
    avatars = Avatars()
    assert (
        avatars.length,
        avatars.font_size,
        avatars.rounded,
        avatars.bold,
        avatars.uppercase,
    ) == (
        2,
        0.4,
        False,
        True,
        True,
    )
    assert avatars.build(name=name).endswith("/2/0.4/0/1/1/svg")


def test_custom_ui_avatars_options_appear_in_the_url(name):
    avatars = Avatars(
        bold=False,
        font_size=0.5,
        length=1,
        rounded=True,
        uppercase=False,
    )
    assert avatars.build(name=name).endswith("/1/0.5/1/0/0/svg")


def test_default_alpha_is_0_2():
    assert Avatars().alpha == 0.2


def test_default_alpha_matches_between_svg_and_rgba_paths(name, email):
    avatars = Avatars(colors=["#000000"])
    svg_url = avatars.build(name=name)
    png_url = unquote(avatars.build(name=name, email=email))
    assert "/00000033/" in svg_url
    assert "rgba(0,0,0,0.2)" in png_url


def test_custom_alpha_changes_both_representations(name, email):
    avatars = Avatars(colors=["#000000"], alpha=0.5)
    svg_url = avatars.build(name=name)
    png_url = unquote(avatars.build(name=name, email=email))
    # 0.5 * 255 = 127.5, rounds to 128 = 0x80
    assert "/00000080/" in svg_url
    assert "rgba(0,0,0,0.5)" in png_url


def test_alpha_is_clamped_to_a_valid_hex_byte_range(name):
    avatars = Avatars(colors=["#000000"], alpha=2)
    url = avatars.build(name=name)
    assert "/000000ff/" in url


def test_configure_updates_colors_in_place(name):
    avatars = Avatars(colors=["000000"])
    avatars.configure(colors=["ffffff"])
    assert "/ffffff/" in avatars.build(name=name)


def test_configure_can_switch_to_tuple_color_entries(name):
    avatars = Avatars()
    avatars.configure(colors=[("#fee2e2", "#ef4444")])
    assert "/fee2e233/ef4444/" in avatars.build(name=name)


def test_configure_updates_size_in_place():
    avatars = Avatars()
    avatars.configure(size=64)
    assert avatars.size == 64


def test_configure_updates_ui_avatars_options_in_place(name):
    avatars = Avatars()
    avatars.configure(
        bold=False,
        font_size=0.5,
        length=1,
        rounded=True,
        uppercase=False,
    )
    assert avatars.build(name=name).endswith("/1/0.5/1/0/0/svg")


def test_configure_leaves_ui_avatars_options_unchanged_when_omitted(name):
    avatars = Avatars(rounded=True)
    avatars.configure(size=256)
    assert avatars.rounded is True


def test_configure_updates_alpha_in_place():
    avatars = Avatars()
    avatars.configure(alpha=0.5)
    assert avatars.alpha == 0.5


def test_configure_leaves_omitted_fields_unchanged():
    avatars = Avatars(colors=["000000"], size=64)
    avatars.configure(size=256)
    assert avatars.colors == ["000000"]
    assert avatars.size == 256


def test_configure_returns_self_for_chaining():
    avatars = Avatars()
    assert avatars.configure(size=64) is avatars


def test_configure_copies_the_given_colors_list():
    avatars = Avatars()
    colors = ["000000"]
    avatars.configure(colors=colors)
    colors.append("ffffff")
    assert avatars.colors == ["000000"]


def test_build_accepts_per_call_overrides_without_mutating_the_instance(name):
    avatars = Avatars()
    url = avatars.build(name=name, size=64, rounded=True)
    assert "/64/" in url
    assert avatars.size == 128
    assert avatars.rounded is False


def test_build_falls_back_to_instance_configuration_when_no_override_given(name):
    avatars = Avatars(size=256, bold=False)
    assert avatars.build(name=name) == avatars.build(name=name, size=None, bold=None)


def test_alpha_can_be_overridden_per_call_without_mutating_the_instance(name):
    avatars = Avatars(colors=["#000000"])
    url = avatars.build(name=name, alpha=0.5)
    assert "/00000080/" in url
    assert avatars.alpha == 0.2


def test_color_bypasses_the_configured_palette(name):
    avatars = Avatars(colors=["#000000"])
    url = avatars.build(name=name, color="#dc2626")
    assert "/dc262633/dc2626/" in url


def test_color_combines_with_font_color(name):
    avatars = Avatars()
    url = avatars.build(name=name, color="#fee2e2", font_color="#dc2626")
    assert "/fee2e233/dc2626/" in url


def test_color_does_not_mutate_the_instance(name):
    avatars = Avatars()
    avatars.build(name=name, color="#dc2626")
    assert avatars.colors == Avatars.COLORS


def test_shared_avatars_instance_is_the_same_object_across_imports():
    from ui_avatars.generator import avatars as avatars_from_generator

    assert avatars is avatars_from_generator


def test_shared_avatars_instance_has_default_configuration():
    assert isinstance(avatars, Avatars)
    assert avatars.colors == Avatars.COLORS
    assert avatars.size == 128
