import hashlib
from urllib.parse import quote

from tailwind_colors import TCH


class Avatars:
    COLORS = list(TCH.RAINBOW_500)

    def __init__(
        self,
        *,
        alpha: float = 0.2,
        bold: bool = True,
        colors: list[str | tuple[str, str]] = COLORS,
        font_size: float = 0.4,
        length: int = 2,
        rounded: bool = False,
        size: int = 128,
        uppercase: bool = True,
    ) -> None:
        self.alpha = alpha
        self.bold = bold
        self.colors = list(colors)
        self.font_size = font_size
        self.length = length
        self.rounded = rounded
        self.size = size
        self.uppercase = uppercase

    def build(
        self,
        *,
        name: str | None = None,
        email: str | None = None,
        alpha: float | None = None,
        bold: bool | None = None,
        color: str | tuple[str, str] | None = None,
        font_size: float | None = None,
        length: int | None = None,
        rounded: bool | None = None,
        size: int | None = None,
        uppercase: bool | None = None,
    ) -> str:
        if not name and not email:
            raise ValueError("requires at least one of name or email")

        alpha = self.alpha if alpha is None else alpha
        bold = self.bold if bold is None else bold
        font_size = self.font_size if font_size is None else font_size
        length = self.length if length is None else length
        rounded = self.rounded if rounded is None else rounded
        size = self.size if size is None else size
        uppercase = self.uppercase if uppercase is None else uppercase

        if not name:
            local_part = email.strip().split("@", 1)[0]
            name = "".join(c for c in local_part if c.isalpha())[:2] or local_part[:2]

        digest = hashlib.md5(
            (email or name).strip().lower().encode(), usedforsecurity=False
        ).hexdigest()

        if color is None:
            color = self.colors[int(digest[:8], 16) % len(self.colors)]

        background, font_color = color if isinstance(color, tuple) else (color, color)
        background, font_color = background.lstrip("#"), font_color.lstrip("#")
        if len(background) == 3:
            background = "".join(c * 2 for c in background)
        if len(font_color) == 3:
            font_color = "".join(c * 2 for c in font_color)
        alpha_255 = min(255, max(0, round(alpha * 255)))
        background_color = f"{background}{alpha_255:02x}"
        image_format = "png" if email else "svg"

        if image_format == "png":
            r, g, b = (int(background[i : i + 2], 16) for i in (0, 2, 4))
            background_color = f"rgba({r},{g},{b},{alpha})"

        url = (
            f"https://ui-avatars.com/api/{quote(name)}/{size}/{background_color}/{font_color}/"
            f"{length}/{font_size}/{int(rounded)}/{int(bold)}/{int(uppercase)}/{image_format}"
        )

        if email:
            url = f"https://www.gravatar.com/avatar/{digest}?s={size}&d={quote(url, safe='')}"

        return url

    def configure(
        self,
        *,
        alpha: float | None = None,
        bold: bool | None = None,
        colors: list[str | tuple[str, str]] | None = None,
        font_size: float | None = None,
        length: int | None = None,
        rounded: bool | None = None,
        size: int | None = None,
        uppercase: bool | None = None,
    ) -> "Avatars":
        if alpha is not None:
            self.alpha = alpha
        if bold is not None:
            self.bold = bold
        if colors is not None:
            self.colors = list(colors)
        if font_size is not None:
            self.font_size = font_size
        if length is not None:
            self.length = length
        if rounded is not None:
            self.rounded = rounded
        if size is not None:
            self.size = size
        if uppercase is not None:
            self.uppercase = uppercase
        return self


avatars = Avatars()
