from pytest import mark

from ui_avatars.initials import generate_initials


@mark.parametrize(
    ("name", "expected"),
    [
        ("Dr. Dre", "DD"),
        ("Gustav Årgonson", "GÅ"),
        ("John Doe (Anderson)", "JA"),
        ("John Doe Bergerson", "JB"),
        ("John Doe", "JD"),
        ("John", "JO"),
        ("MA", "MA"),
    ],
)
def test_matches_php_initials(name, expected):
    assert generate_initials(name) == expected


def test_can_preserve_letter_case():
    assert generate_initials("john doe", uppercase=False) == "jd"


def test_generates_first_and_last_initials():
    assert generate_initials("John Christian Doe") == "JD"


def test_limits_a_single_name_to_the_requested_length():
    assert generate_initials("Leonardo") == "LE"


def test_uses_each_name_when_the_requested_length_allows_it():
    assert generate_initials("John Christian Doe", length=3) == "JCD"


def test_reuses_letters_from_the_last_name_when_needed():
    assert generate_initials("Ada Lovelace", length=3) == "ALO"


def test_preserves_hyphenated_surnames_when_two_initials_are_requested():
    assert generate_initials("Lasse Foo-Rafn") == "LF"


def test_removes_special_characters():
    assert generate_initials("John Doe (Anderson)") == "JA"


def test_splits_hyphenated_surnames_when_more_initials_are_requested():
    assert generate_initials("Lasse Foo-Rafn", length=3) == "LFR"


def test_splits_a_hyphenated_single_name():
    assert generate_initials("Jean-Luc") == "JL"


def test_trims_outer_hyphens_and_whitespace():
    assert generate_initials(" -Jean-Luc- ") == "JL"


def test_uppercases_unicode_initials():
    assert generate_initials("Jens Ølsted") == "JØ"
