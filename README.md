# ui-avatars

[![PyPI](https://img.shields.io/pypi/v/ui-avatars.svg?style=flat-square)](https://pypi.org/project/ui-avatars/)
[![CI](https://img.shields.io/github/actions/workflow/status/stevelacey/ui-avatars-python/ci.yml?branch=main&style=flat-square)](https://github.com/stevelacey/ui-avatars-python/actions/workflows/ci.yml?query=branch:main)
[![Coverage](https://img.shields.io/codecov/c/github/stevelacey/ui-avatars-python?style=flat-square)](https://codecov.io/gh/stevelacey/ui-avatars-python)
[![Downloads](https://img.shields.io/pypi/dm/ui-avatars.svg?style=flat-square)](https://pypi.org/project/ui-avatars/)
[![License](https://img.shields.io/github/license/stevelacey/ui-avatars-python?style=flat-square)](LICENSE.md)

Deterministic avatar URLs for light and dark designs:
[Gravatar](https://gravatar.com) or [Libravatar](https://libravatar.org) photos falling
back to colored initials via [ui-avatars.com](https://ui-avatars.com).
Same input, same URL, always.

<table>
<tr>
<td align="center"><a href="https://ui-avatars.com/api/AL/128/f9731633/f97316/2/0.4/0/1/1/svg"><img src="https://ui-avatars.com/api/AL/128/f9731633/f97316/2/0.4/0/1/1/svg" style="object-fit: contain" width="72" height="72"></a></td>
<td align="center"><a href="https://www.gravatar.com/avatar/7487baad7b087cb03cc4ccf7d044c150?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FSL%2F128%2Frgba%28236%2C72%2C153%2C0.2%29%2Fec4899%2F2%2F0.4%2F0%2F1%2F1%2Fpng"><img src="https://www.gravatar.com/avatar/7487baad7b087cb03cc4ccf7d044c150?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FSL%2F128%2Frgba%28236%2C72%2C153%2C0.2%29%2Fec4899%2F2%2F0.4%2F0%2F1%2F1%2Fpng" style="object-fit: contain" width="72" height="72"></a></td>
<td align="center"><a href="https://ui-avatars.com/api/AT/128/84cc1633/84cc16/2/0.4/0/1/1/svg"><img src="https://ui-avatars.com/api/AT/128/84cc1633/84cc16/2/0.4/0/1/1/svg" style="object-fit: contain" width="72" height="72"></a></td>
<td align="center"><a href="https://ui-avatars.com/api/LT/128/06b6d433/06b6d4/2/0.4/0/1/1/svg"><img src="https://ui-avatars.com/api/LT/128/06b6d433/06b6d4/2/0.4/0/1/1/svg" style="object-fit: contain" width="72" height="72"></a></td>
<td align="center"><a href="https://www.gravatar.com/avatar/629999fcb3f6a928abe5f65ed0ab09c2?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FPI%2F128%2Frgba%2859%2C130%2C246%2C0.2%29%2F3b82f6%2F2%2F0.4%2F0%2F1%2F1%2Fpng"><img src="https://www.gravatar.com/avatar/629999fcb3f6a928abe5f65ed0ab09c2?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FPI%2F128%2Frgba%2859%2C130%2C246%2C0.2%29%2F3b82f6%2F2%2F0.4%2F0%2F1%2F1%2Fpng" style="object-fit: contain" width="72" height="72"></a></td>
<td align="center"><a href="https://ui-avatars.com/api/MH/128/3b82f633/3b82f6/2/0.4/0/1/1/svg"><img src="https://ui-avatars.com/api/MH/128/3b82f633/3b82f6/2/0.4/0/1/1/svg" style="object-fit: contain" width="72" height="72"></a></td>
<td align="center"><a href="https://www.gravatar.com/avatar/3869e93ce6b2a22e37cf13281d9e6f75?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FLV%2F128%2Frgba%28139%2C92%2C246%2C0.2%29%2F8b5cf6%2F2%2F0.4%2F0%2F1%2F1%2Fpng"><img src="https://www.gravatar.com/avatar/3869e93ce6b2a22e37cf13281d9e6f75?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FLV%2F128%2Frgba%28139%2C92%2C246%2C0.2%29%2F8b5cf6%2F2%2F0.4%2F0%2F1%2F1%2Fpng" style="object-fit: contain" width="72" height="72"></a></td>
<td align="center"><a href="https://www.gravatar.com/avatar/047f2332cde3730f1ed661eebb0c5686?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FGR%2F128%2Frgba%28139%2C92%2C246%2C0.2%29%2F8b5cf6%2F2%2F0.4%2F0%2F1%2F1%2Fpng"><img src="https://www.gravatar.com/avatar/047f2332cde3730f1ed661eebb0c5686?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FGR%2F128%2Frgba%28139%2C92%2C246%2C0.2%29%2F8b5cf6%2F2%2F0.4%2F0%2F1%2F1%2Fpng" style="object-fit: contain" width="72" height="72"></a></td>
</tr>
<tr>
<td align="center"><a href="https://www.gravatar.com/avatar/b8605bc56f7d1249560eb40f7cc69001?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FCW%2F128%2Frgba%2820%2C184%2C166%2C0.2%29%2F14b8a6%2F2%2F0.4%2F0%2F1%2F1%2Fpng"><img src="https://www.gravatar.com/avatar/b8605bc56f7d1249560eb40f7cc69001?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FCW%2F128%2Frgba%2820%2C184%2C166%2C0.2%29%2F14b8a6%2F2%2F0.4%2F0%2F1%2F1%2Fpng" style="object-fit: contain" width="72" height="72"></a></td>
<td align="center"><a href="https://www.gravatar.com/avatar/8d924f842e67d03be5d0812563e8d672?s=256&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FBA%2F256%2Frgba%2834%2C197%2C94%2C0.2%29%2F22c55e%2F2%2F0.4%2F0%2F1%2F1%2Fpng"><img src="https://www.gravatar.com/avatar/8d924f842e67d03be5d0812563e8d672?s=256&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FBA%2F256%2Frgba%2834%2C197%2C94%2C0.2%29%2F22c55e%2F2%2F0.4%2F0%2F1%2F1%2Fpng" style="object-fit: contain" width="72" height="72"></a></td>
<td align="center"><a href="https://www.gravatar.com/avatar/f29327647a9cff5c69618bae420792ea?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FAP%2F128%2Frgba%2814%2C165%2C233%2C0.2%29%2F0ea5e9%2F2%2F0.4%2F0%2F1%2F1%2Fpng"><img src="https://www.gravatar.com/avatar/f29327647a9cff5c69618bae420792ea?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FAP%2F128%2Frgba%2814%2C165%2C233%2C0.2%29%2F0ea5e9%2F2%2F0.4%2F0%2F1%2F1%2Fpng" style="object-fit: contain" width="72" height="72"></a></td>
<td align="center"><a href="https://ui-avatars.com/api/BP/128/1d4ed833/1d4ed8/2/0.4/0/1/1/svg"><img src="https://ui-avatars.com/api/BP/128/1d4ed833/1d4ed8/2/0.4/0/1/1/svg" style="object-fit: contain" width="72" height="72"></a></td>
<td align="center"><a href="https://ui-avatars.com/api/TB/128/84cc1633/84cc16/2/0.4/0/1/1/svg"><img src="https://ui-avatars.com/api/TB/128/84cc1633/84cc16/2/0.4/0/1/1/svg" style="object-fit: contain" width="72" height="72"></a></td>
<td align="center"><a href="https://www.gravatar.com/avatar/de3fe73f6cd2adaac3a8a1fa04d4d80f?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FCC%2F128%2Frgba%28249%2C115%2C22%2C0.2%29%2Ff97316%2F2%2F0.4%2F0%2F1%2F1%2Fpng"><img src="https://www.gravatar.com/avatar/de3fe73f6cd2adaac3a8a1fa04d4d80f?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FCC%2F128%2Frgba%28249%2C115%2C22%2C0.2%29%2Ff97316%2F2%2F0.4%2F0%2F1%2F1%2Fpng" style="object-fit: contain" width="72" height="72"></a></td>
<td align="center"><a href="https://ui-avatars.com/api/KJ/128/10b98133/10b981/2/0.4/0/1/1/svg"><img src="https://ui-avatars.com/api/KJ/128/10b98133/10b981/2/0.4/0/1/1/svg" style="object-fit: contain" width="72" height="72"></a></td>
<td align="center"><a href="https://www.gravatar.com/avatar/21a241aa10ee457a5f6b72aca98a4860?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FWW%2F128%2Frgba%2834%2C197%2C94%2C0.2%29%2F22c55e%2F2%2F0.4%2F0%2F1%2F1%2Fpng"><img src="https://www.gravatar.com/avatar/21a241aa10ee457a5f6b72aca98a4860?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FWW%2F128%2Frgba%2834%2C197%2C94%2C0.2%29%2F22c55e%2F2%2F0.4%2F0%2F1%2F1%2Fpng" style="object-fit: contain" width="72" height="72"></a></td>
</tr>
</table>

## Install

```bash
pip install ui-avatars
```

## Usage

```python
from ui_avatars import avatar_url

avatar_url(name="Ada Lovelace", email="ada@example.com")
# Gravatar photo, falling back to generated initials

avatar_url(name="Ada Lovelace")
# straight ui-avatars.com URL, no Gravatar lookup

avatar_url(email="ada@example.com")
# initials from the first two letters of the email

avatar_url(name="Ada Lovelace", alpha=0.75, size=256, rounded=True)
# pass any of the options as one-off overrides

avatar_url(name="Ada Lovelace", mask="hexagon", format="webp")
# crop the image to a hexagon and serve webp via wsrv.nl

avatar_url(name="Ada Lovelace", email="ada@example.com", source="libravatar")
# look up the photo on Libravatar instead of Gravatar

avatar_url(email="ada@example.com", host="example.com", source="secure.gravatar.com")
# override hostnames to use custom/self-hosted servers
```

## Options

| Name | Default | Description |
| :-- | :-- | :-- |
| `alpha` | `0.2` | Background opacity (`0` to `1`) |
| `background` | | Pin the background color |
| `bold` | `True` | Bold the initials |
| `colors` | `RAINBOW_500` | List of hex values or `(background, text)` tuples |
| `font_color` | | Pin the text color |
| `font_size` | `0.4` | Size of the initials (`0.1` to `1`) |
| `format` | | Image format, e.g. `png`, `svg`, and other [formats](https://wsrv.nl/docs/format) |
| `host` | `ui-avatars.com` | User initials avatars host |
| `length` | `2` | Number of initials |
| `mask` | | Shape mask, e.g. `hexagon`, `pentagon`, `square`, and other [masks](https://wsrv.nl/docs/mask) |
| `proxy` | `wsrv.nl` | Proxy for masks, rounding, and extra formats |
| `region` | | Service region, e.g. `eu` or `na` (ignored if `host` is set) |
| `rounded` | `False` | Round the image (ignored if `mask` is set) |
| `size` | `128` | Image size in pixels |
| `source` | `gravatar` | Photo source, e.g. `gravatar`, `libravatar`, or any compatible host |
| `uppercase` | `True` | Uppercase the initials |

## Configuration

Configure the shared `avatars` instance that `avatar_url()` uses, or construct your own:

```python
from ui_avatars import avatar_url, avatars, Avatars

avatars.configure(colors=["#1d4ed8", "#b91c1c"], size=256, rounded=True)
avatar_url(name="Ada Lovelace", email="ada@example.com")

my_avatars = Avatars(colors=["#1d4ed8", "#b91c1c"], size=256, rounded=True)
my_avatars.build(name="Ada Lovelace", email="ada@example.com")
```

## Colors

The default color palette is [`tailwind_colors`](https://pypi.org/project/tailwind_colors/) `RAINBOW_500`.
Swap it for another scale:

```python
from tailwind_colors import TCH

avatars.configure(colors=TCH.RAINBOW_300)
# or make up your own color palette
avatars.configure(colors=["#f00", "#0f0", "#00f"])
```

Pair colors manually with `(background, text)` tuples.
Set `alpha=1` for solid backgrounds:

```python
avatars.configure(alpha=1, colors=[("#f00", "#fff"), ("#000", "#00f")])
```

To override the palette and force a specific color, pass the `color` argument:

```python
avatar_url(name="Ada Lovelace", email="ada@example.com", color="#f00")
```

To pin the background color, text color, or both, pass `background` and `font_color`:

```python
avatar_url(name="Ada Lovelace", alpha=1, background="#f00", font_color="#000")
```

## Development

```bash
poetry install
poetry run pytest
poetry run ruff check --fix
```

## License

MIT
