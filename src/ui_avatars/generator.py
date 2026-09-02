import hashlib
from urllib.parse import quote, urlencode

from tailwind_colors import TCH


class Avatars:
    COLORS = list(TCH.RAINBOW_500)

    DEFAULT_HOST = "https://ui-avatars.com"
    DEFAULT_PROXY = "https://wsrv.nl"

    REGION_EU = "eu"
    REGION_NA = "na"

    REGIONS = {
        REGION_EU: "https://eu.ui-avatars.com",
        REGION_NA: "https://na.ui-avatars.com",
    }

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
        format: str | None = None,
        host: str | None = None,
        length: int = 2,
        mask: str | None = None,
        proxy: str | None = None,
        region: str | None = None,
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
        self.format = format
        self.host = host
        self.length = length
        self.mask = mask
        self.proxy = proxy
        self.region = region
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
        format: str | None = None,
        host: str | None = None,
        length: int | None = None,
        mask: str | None = None,
        proxy: str | None = None,
        region: str | None = None,
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
        format = self.format if format is None else format
        host = self.parse_hostname(host or self.host)
        length = self.length if length is None else length
        region = self.region if region is None else region
        rounded = int(self.rounded if rounded is None else rounded)
        mask = mask or self.mask or email and rounded and "circle" or ""
        rounded = int(rounded or mask == "circle")
        proxy = self.parse_hostname(proxy or self.proxy)
        size = self.size if size is None else size
        source = self.source if source is None else source
        origin = self.parse_hostname(self.SOURCES.get(source, source))
        uppercase = int(self.uppercase if uppercase is None else uppercase)

        if not name and not email:
            raise ValueError("requires at least one of name or email")

        if host and "." not in host:
            raise ValueError(f"unknown host: {host!r}")

        if proxy and "." not in proxy:
            raise ValueError(f"unknown proxy: {proxy!r}")

        if region and region not in self.REGIONS:
            raise ValueError(f"unknown region: {region!r}")

        if origin and "." not in origin:
            raise ValueError(f"unknown source: {source!r}")

        host = host or self.REGIONS.get(region) or self.DEFAULT_HOST
        proxy = proxy or self.DEFAULT_PROXY

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

        if format is None:
            format = "png" if email and ("gravatar.com" in origin or rounded) else "svg"

        if format == "png":
            r, g, b = (int(background_color[i : i + 2], 16) for i in (0, 2, 4))
            background_color = f"rgba({r},{g},{b},{alpha})"
        elif alpha < 1:
            alpha_suffix = f"{min(255, max(0, round(alpha * 255))):02x}"
            background_color = f"{background_color}{alpha_suffix}"

        url = default = (
            f"{host}/api/{quote(name)}/{size}/{background_color}/{text_color}/"
            f"{length}/{font_size}/{rounded}/{bold}/{uppercase}/{format}"
        )

        if email:
            url = self.build_url(f"{origin}/avatar/{digest}", s=size, d=default)

        if email and rounded or format not in ("png", "svg") or mask:
            if email and (format not in ("png", "svg") or mask and mask != "circle"):
                default = self.build_url(
                    f"{proxy}/",
                    url=default,
                    w=size,
                    h=size,
                    mask=mask,
                    output=format,
                )
            url = self.build_url(
                f"{proxy}/",
                url=(
                    self.build_url(f"{origin}/avatar/{digest}", s=size, d=404)
                    if email
                    else url
                ),
                default=default if email else None,
                w=size,
                h=size,
                mask=mask,
                output=format,
            )

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
        format: str | None = None,
        host: str | None = None,
        length: int | None = None,
        mask: str | None = None,
        proxy: str | None = None,
        region: str | None = None,
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
        if format is not None:
            self.format = format
        if host is not None:
            self.host = host
        if length is not None:
            self.length = length
        if mask is not None:
            self.mask = mask
        if proxy is not None:
            self.proxy = proxy
        if region is not None:
            self.region = region
        if rounded is not None:
            self.rounded = rounded
        if size is not None:
            self.size = size
        if source is not None:
            self.source = source
        if uppercase is not None:
            self.uppercase = uppercase

        return self

    def build_url(self, base: str, **params: str | int | None) -> str:
        params = {key: value for key, value in params.items() if value is not None}
        return f"{base}?{urlencode(params, quote_via=quote)}"

    def parse_hostname(self, value: str) -> str:
        return f"https://{value}" if value and "://" not in value else value


avatars = Avatars()
