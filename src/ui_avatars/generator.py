import hashlib
from urllib.parse import quote

from tailwind_colors import TCH


class Avatars:
    COLORS = list(TCH.RAINBOW_500)

    GRAVATAR = "gravatar"
    LIBRAVATAR = "libravatar"

    SOURCES = {
        GRAVATAR: "https://www.gravatar.com",
        LIBRAVATAR: "https://seccdn.libravatar.org",
    }

    def __init__(
        self,
        *,
        alpha: float = 0.2,
        background: str | None = None,
        bold: bool = True,
        colors: list[str | tuple[str, str]] = COLORS,
        font_color: str | None = None,
        font_size: float = 0.4,
        length: int = 2,
        rounded: bool = False,
        size: int = 128,
        source: str = GRAVATAR,
        uppercase: bool = True,
    ) -> None:
        self.alpha = alpha
        self.background = background
        self.bold = bold
        self.colors = list(colors)
        self.font_color = font_color
        self.font_size = font_size
        self.length = length
        self.rounded = rounded
        self.size = size
        self.source = source
        self.uppercase = uppercase

    def build(
        self,
        *,
        name: str | None = None,
        email: str | None = None,
        alpha: float | None = None,
        background: str | None = None,
        bold: bool | None = None,
        color: str | None = None,
        font_color: str | None = None,
        font_size: float | None = None,
        length: int | None = None,
        rounded: bool | None = None,
        size: int | None = None,
        source: str | None = None,
        uppercase: bool | None = None,
    ) -> str:
        alpha = self.alpha if alpha is None else alpha
        background = self.background if background is None else background
        bold = int(self.bold if bold is None else bold)
        font_color = self.font_color if font_color is None else font_color
        font_size = self.font_size if font_size is None else font_size
        length = self.length if length is None else length
        rounded = int(self.rounded if rounded is None else rounded)
        size = self.size if size is None else size
        source = self.source if source is None else source
        origin = self.SOURCES.get(
            source, source if "://" in source else f"https://{source}"
        )
        uppercase = int(self.uppercase if uppercase is None else uppercase)

        if not name and not email:
            raise ValueError("requires at least one of name or email")

        if "." not in origin:
            raise ValueError(f"unknown source: {source!r}")

        if not name:
            local_part = email.strip().split("@", 1)[0]
            name = "".join(c for c in local_part if c.isalpha())[:2] or local_part[:2]

        digest = hashlib.md5(
            (email or name).strip().lower().encode(), usedforsecurity=False
        ).hexdigest()

        background_color, text_color = color, color
        if color is None:
            palette_entry = self.colors[int(digest[:8], 16) % len(self.colors)]
            background_color, text_color = (
                palette_entry
                if isinstance(palette_entry, tuple)
                else (palette_entry, palette_entry)
            )
        if background is not None:
            background_color = background
        if font_color is not None:
            text_color = font_color

        background_color, text_color = (
            background_color.lstrip("#"),
            text_color.lstrip("#"),
        )
        if len(background_color) == 3:
            background_color = "".join(c * 2 for c in background_color)
        if len(text_color) == 3:
            text_color = "".join(c * 2 for c in text_color)

        format = "svg" if not email or source == self.LIBRAVATAR else "png"
        if format == "png":
            r, g, b = (int(background_color[i : i + 2], 16) for i in (0, 2, 4))
            background_color = f"rgba({r},{g},{b},{alpha})"
        else:
            alpha_suffix = f"{min(255, max(0, round(alpha * 255))):02x}"
            background_color = f"{background_color}{alpha_suffix}"

        url = (
            f"https://ui-avatars.com/api/{quote(name)}/{size}/{background_color}/{text_color}/"
            f"{length}/{font_size}/{rounded}/{bold}/{uppercase}/{format}"
        )

        if email:
            url = f"{origin}/avatar/{digest}?s={size}&d={quote(url, safe='')}"

        return url

    def configure(
        self,
        *,
        alpha: float | None = None,
        background: str | None = None,
        bold: bool | None = None,
        colors: list[str | tuple[str, str]] | None = None,
        font_color: str | None = None,
        font_size: float | None = None,
        length: int | None = None,
        rounded: bool | None = None,
        size: int | None = None,
        source: str | None = None,
        uppercase: bool | None = None,
    ) -> "Avatars":
        if alpha is not None:
            self.alpha = alpha
        if background is not None:
            self.background = background
        if bold is not None:
            self.bold = bold
        if colors is not None:
            self.colors = list(colors)
        if font_color is not None:
            self.font_color = font_color
        if font_size is not None:
            self.font_size = font_size
        if length is not None:
            self.length = length
        if rounded is not None:
            self.rounded = rounded
        if size is not None:
            self.size = size
        if source is not None:
            self.source = source
        if uppercase is not None:
            self.uppercase = uppercase
        return self


avatars = Avatars()
