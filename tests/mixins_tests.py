from pytest import raises

from ui_avatars import AvatarMixin, Avatars, avatar_url


class User(AvatarMixin):
    def __init__(
        self,
        first_name="",
        last_name="",
        username="",
        email="",
        avatar=None,
        image=None,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.avatar = avatar
        self.image = image

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()


class Person(AvatarMixin):
    def __init__(self, **attrs):
        self.__dict__.update(attrs)


def test_django_user_uses_full_name_and_email():
    user = User(
        first_name="Ada",
        last_name="Lovelace",
        username="ada",
        email="ada@example.com",
    )
    assert user.avatar_url == avatar_url(name="Ada Lovelace", email="ada@example.com")


def test_django_user_falls_back_to_username_when_name_is_empty():
    user = User(username="ada_lovelace")
    assert user.get_avatar_name() == "ada lovelace"
    assert user.avatar_url == avatar_url(name="ada lovelace")


def test_django_user_uses_uploaded_avatar():
    user = User(
        first_name="Ada",
        last_name="Lovelace",
        email="ada@example.com",
        avatar="https://cdn.example.com/ada.png",
    )
    assert user.avatar_url == avatar_url(
        name="Ada Lovelace",
        email="ada@example.com",
        image="https://cdn.example.com/ada.png",
    )


def test_first_and_last_name_are_combined_without_get_full_name():
    person = Person(first_name="Ada", last_name="Lovelace")
    assert person.get_avatar_name() == "Ada Lovelace"
    assert person.avatar_url == avatar_url(name="Ada Lovelace")


def test_first_name_only_is_used_when_last_name_is_missing():
    person = Person(first_name="Ada")
    assert person.get_avatar_name() == "Ada"


def test_last_name_only_is_used_when_first_name_is_missing():
    person = Person(last_name="Lovelace")
    assert person.get_avatar_name() == "Lovelace"


def test_name_attribute_is_used_for_generic_models():
    person = Person(name="Ada Lovelace", email="ada@example.com")
    assert person.avatar_url == avatar_url(name="Ada Lovelace", email="ada@example.com")


def test_full_name_attribute_is_preferred_over_name():
    person = Person(full_name="Ada Lovelace", name="Ignored")
    assert person.get_avatar_name() == "Ada Lovelace"


def test_get_full_name_is_preferred_over_name_fields():
    user = User(first_name="Ada", last_name="Lovelace", username="ada")
    user.name = "Ignored"
    user.full_name = "Also Ignored"
    assert user.get_avatar_name() == "Ada Lovelace"


def test_empty_get_full_name_falls_through_to_username():
    user = User(username="ada")
    assert user.get_avatar_name() == "ada"


def test_email_is_optional():
    person = Person(name="Ada Lovelace")
    assert person.get_avatar_email() == ""
    assert person.avatar_url == avatar_url(name="Ada Lovelace")


def test_underscores_are_replaced_in_any_name():
    person = Person(name="ada_lovelace")
    assert person.get_avatar_name() == "ada lovelace"


def test_whitespace_only_name_is_ignored():
    person = Person(name="  ")
    assert person.get_avatar_name() == ""


def test_image_attribute_is_used_when_avatar_is_missing():
    person = Person(name="Ada Lovelace", image="https://cdn.example.com/photo.png")
    assert person.get_avatar_image() == "https://cdn.example.com/photo.png"
    assert person.avatar_url == avatar_url(
        name="Ada Lovelace", image="https://cdn.example.com/photo.png"
    )


def test_avatar_is_preferred_over_image():
    person = Person(
        name="Ada Lovelace",
        avatar="https://cdn.example.com/avatar.png",
        image="https://cdn.example.com/image.png",
    )
    assert person.get_avatar_image() == "https://cdn.example.com/avatar.png"


def test_empty_avatar_falls_through_to_image():
    person = Person(
        name="Ada Lovelace", avatar="", image="https://cdn.example.com/photo.png"
    )
    assert person.get_avatar_image() == "https://cdn.example.com/photo.png"


def test_get_avatar_name_can_be_overridden():
    class Author(AvatarMixin):
        def get_avatar_name(self):
            return "Pen Name"

    assert Author().get_avatar_name() == "Pen Name"
    assert Author().avatar_url == avatar_url(name="Pen Name")


def test_get_avatar_email_can_be_overridden():
    class Author(AvatarMixin):
        name = "Ada Lovelace"

        def get_avatar_email(self):
            return "pen@example.com"

    assert Author().avatar_url == avatar_url(
        name="Ada Lovelace", email="pen@example.com"
    )


def test_get_avatar_image_can_be_overridden():
    class Author(AvatarMixin):
        name = "Ada Lovelace"

        def get_avatar_image(self):
            return "https://cdn.example.com/photo.png"

    assert Author().avatar_url == avatar_url(
        name="Ada Lovelace", image="https://cdn.example.com/photo.png"
    )


def test_get_avatar_url_passes_through_options():
    person = Person(name="Ada Lovelace")
    assert person.get_avatar_url(size=64, rounded=True) == avatar_url(
        name="Ada Lovelace", size=64, rounded=True
    )


def test_avatar_url_property_matches_get_avatar_url():
    person = Person(name="Ada Lovelace", email="ada@example.com")
    assert person.avatar_url == person.get_avatar_url()


def test_mixin_defaults_to_the_shared_avatars_instance():
    assert Person.avatars is AvatarMixin.avatars
    person = Person(name="Ada Lovelace")
    assert person.avatars is AvatarMixin.avatars
    assert person.avatar_url == avatar_url(name="Ada Lovelace")


def test_mixin_respects_shared_avatars_configuration(restore_defaults):
    restore_defaults.configure(size=256, rounded=True)
    person = Person(name="Ada Lovelace")
    assert person.avatar_url == avatar_url(name="Ada Lovelace")
    assert "/256/" in person.avatar_url


def test_model_can_assign_a_custom_avatars_instance():
    custom = Avatars(size=64, rounded=True)

    class Author(AvatarMixin):
        avatars = custom
        name = "Ada Lovelace"

    assert Author().avatar_url == custom.build(name="Ada Lovelace")
    assert Author().avatar_url != avatar_url(name="Ada Lovelace")


def test_instance_can_override_the_avatars_instance():
    person = Person(name="Ada Lovelace")
    person.avatars = Avatars(size=64)
    assert person.avatar_url == person.avatars.build(name="Ada Lovelace")
    assert Person(name="Ada Lovelace").avatar_url == avatar_url(name="Ada Lovelace")


def test_username_of_only_underscores_is_ignored():
    person = Person(username="___")
    assert person.get_avatar_name() == ""
    with raises(ValueError, match="requires at least one"):
        person.get_avatar_url()


def test_related_featured_image_file_url_is_resolved():
    class FieldFile:
        url = "https://cdn.example.com/featured.png"

    class FeaturedImage:
        file = FieldFile()

    person = Person(name="Ada Lovelace", image=FeaturedImage())
    assert "https%3A%2F%2Fcdn.example.com%2Ffeatured.png" in person.avatar_url
