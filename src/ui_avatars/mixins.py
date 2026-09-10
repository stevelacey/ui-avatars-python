from ui_avatars.generator import avatars


class AvatarMixin:
    avatars = avatars

    def get_avatar_name(self) -> str:
        return (
            (hasattr(self, "get_full_name") and self.get_full_name())
            or getattr(self, "full_name", "")
            or getattr(self, "name", "")
            or f"{getattr(self, 'first_name', '') or ''} {getattr(self, 'last_name', '') or ''}".strip()
            or getattr(self, "username", "")
        ).replace("_", " ").strip()

    def get_avatar_email(self) -> str:
        return getattr(self, "email", "") or ""

    def get_avatar_image(self) -> object | str | None:
        return getattr(self, "avatar", None) or getattr(self, "image", None)

    def get_avatar_url(self, **options) -> str:
        return self.avatars.build(
            name=self.get_avatar_name(),
            email=self.get_avatar_email(),
            image=self.get_avatar_image(),
            **options,
        )

    @property
    def avatar_url(self) -> str:
        return self.get_avatar_url()
