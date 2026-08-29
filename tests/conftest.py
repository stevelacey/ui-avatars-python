from pytest import fixture

from ui_avatars import avatars


@fixture
def name():
    return "Ada Lovelace"


@fixture
def email():
    return "ada@example.com"


@fixture
def restore_defaults():
    original = dict(vars(avatars))
    original["colors"] = list(avatars.colors)
    yield avatars
    for key, value in original.items():
        setattr(avatars, key, value)
