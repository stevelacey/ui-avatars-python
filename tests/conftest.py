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
    original_colors, original_size = avatars.colors, avatars.size
    yield avatars
    avatars.configure(colors=original_colors, size=original_size)
