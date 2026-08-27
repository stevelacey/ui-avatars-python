from ui_avatars.generator import avatars


def avatar_url(
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
    return avatars.build(
        name=name,
        email=email,
        alpha=alpha,
        background=background,
        bold=bold,
        color=color,
        font_color=font_color,
        font_size=font_size,
        length=length,
        rounded=rounded,
        size=size,
        source=source,
        uppercase=uppercase,
    )
