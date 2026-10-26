import re

from ui_avatars import generator

LOCAL_HOST = re.compile(
    r"^(localhost|[^.:]+|.+\.(localhost|test|local|internal|lan|example|home\.arpa)"
    r"|(127|10|192\.168|169\.254|172\.(1[6-9]|2\d|3[01]))\.[\d.]+|0\.0\.0\.0"
    r"|::1|f[cd][\da-f]*:.*|fe[89ab][\da-f]*:.*)$"
)


def avatar_url(
    *,
    name: str | None = None,
    email: str | None = None,
    image: object | str | None = None,
    alpha: float | None = None,
    background: str | None = None,
    base: str | None = None,
    bold: bool | None = None,
    color: str | None = None,
    font_color: str | None = None,
    font_size: float | None = None,
    format: str | None = None,
    hash: str | None = None,
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
    return generator.avatars.build(
        name=name,
        email=email,
        image=image,
        alpha=alpha,
        background=background,
        base=base,
        bold=bold,
        color=color,
        font_color=font_color,
        font_size=font_size,
        format=format,
        hash=hash,
        host=host,
        length=length,
        mask=mask,
        proxy=proxy,
        region=region,
        rounded=rounded,
        size=size,
        source=source,
        uppercase=uppercase,
    )


def is_local(url: str) -> bool:
    if "://" not in url:
        return True
    authority = url.split("://", 1)[1].split("/")[0].split("?")[0].split("#")[0]
    host = authority.rsplit("@", 1)[-1]
    host = host[1:].split("]")[0] if host.startswith("[") else host.split(":")[0]
    return bool(LOCAL_HOST.match(host.lower().rstrip(".")))
