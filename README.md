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
<td align="center"><a href="https://ui-avatars.com/api/Ada%20Lovelace/128/f9731633/f97316/2/0.4/0/1/1/svg"><img src="https://ui-avatars.com/api/Ada%20Lovelace/128/f9731633/f97316/2/0.4/0/1/1/svg" width="72" height="72"></a></td>
<td align="center"><a href="https://www.gravatar.com/avatar/7487baad7b087cb03cc4ccf7d044c150?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FSteve%2F128%2Frgba%28236%2C72%2C153%2C0.2%29%2Fec4899%2F2%2F0.4%2F0%2F1%2F1%2Fpng"><img src="https://www.gravatar.com/avatar/7487baad7b087cb03cc4ccf7d044c150?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FSteve%2F128%2Frgba%28236%2C72%2C153%2C0.2%29%2Fec4899%2F2%2F0.4%2F0%2F1%2F1%2Fpng" width="72" height="72"></a></td>
<td align="center"><a href="https://ui-avatars.com/api/Alan%20Turing/128/84cc1633/84cc16/2/0.4/0/1/1/svg"><img src="https://ui-avatars.com/api/Alan%20Turing/128/84cc1633/84cc16/2/0.4/0/1/1/svg" width="72" height="72"></a></td>
<td align="center"><a href="https://ui-avatars.com/api/Linus%20Torvalds/128/06b6d433/06b6d4/2/0.4/0/1/1/svg"><img src="https://ui-avatars.com/api/Linus%20Torvalds/128/06b6d433/06b6d4/2/0.4/0/1/1/svg" width="72" height="72"></a></td>
<td align="center"><a href="https://www.gravatar.com/avatar/629999fcb3f6a928abe5f65ed0ab09c2?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FPaul%2520Irish%2F128%2Frgba%2859%2C130%2C246%2C0.2%29%2F3b82f6%2F2%2F0.4%2F0%2F1%2F1%2Fpng"><img src="https://www.gravatar.com/avatar/629999fcb3f6a928abe5f65ed0ab09c2?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FPaul%2520Irish%2F128%2Frgba%2859%2C130%2C246%2C0.2%29%2F3b82f6%2F2%2F0.4%2F0%2F1%2F1%2Fpng" width="72" height="72"></a></td>
<td align="center"><a href="https://ui-avatars.com/api/Margaret%20Hamilton/128/3b82f633/3b82f6/2/0.4/0/1/1/svg"><img src="https://ui-avatars.com/api/Margaret%20Hamilton/128/3b82f633/3b82f6/2/0.4/0/1/1/svg" width="72" height="72"></a></td>
<td align="center"><a href="https://www.gravatar.com/avatar/3869e93ce6b2a22e37cf13281d9e6f75?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FLea%2520Verou%2F128%2Frgba%28139%2C92%2C246%2C0.2%29%2F8b5cf6%2F2%2F0.4%2F0%2F1%2F1%2Fpng"><img src="https://www.gravatar.com/avatar/3869e93ce6b2a22e37cf13281d9e6f75?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FLea%2520Verou%2F128%2Frgba%28139%2C92%2C246%2C0.2%29%2F8b5cf6%2F2%2F0.4%2F0%2F1%2F1%2Fpng" width="72" height="72"></a></td>
<td align="center"><a href="https://www.gravatar.com/avatar/047f2332cde3730f1ed661eebb0c5686?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FGuido%2520van%2520Rossum%2F128%2Frgba%28139%2C92%2C246%2C0.2%29%2F8b5cf6%2F2%2F0.4%2F0%2F1%2F1%2Fpng"><img src="https://www.gravatar.com/avatar/047f2332cde3730f1ed661eebb0c5686?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FGuido%2520van%2520Rossum%2F128%2Frgba%28139%2C92%2C246%2C0.2%29%2F8b5cf6%2F2%2F0.4%2F0%2F1%2F1%2Fpng" width="72" height="72"></a></td>
</tr>
<tr>
<td align="center"><a href="https://www.gravatar.com/avatar/b8605bc56f7d1249560eb40f7cc69001?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FCassidy%2520Williams%2F128%2Frgba%2820%2C184%2C166%2C0.2%29%2F14b8a6%2F2%2F0.4%2F0%2F1%2F1%2Fpng"><img src="https://www.gravatar.com/avatar/b8605bc56f7d1249560eb40f7cc69001?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FCassidy%2520Williams%2F128%2Frgba%2820%2C184%2C166%2C0.2%29%2F14b8a6%2F2%2F0.4%2F0%2F1%2F1%2Fpng" width="72" height="72"></a></td>
<td align="center"><a href="https://www.gravatar.com/avatar/8d924f842e67d03be5d0812563e8d672?s=256&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FBig%2520Avatar%2F256%2Frgba%2834%2C197%2C94%2C0.2%29%2F22c55e%2F2%2F0.4%2F0%2F1%2F1%2Fpng"><img src="https://www.gravatar.com/avatar/8d924f842e67d03be5d0812563e8d672?s=256&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FBig%2520Avatar%2F256%2Frgba%2834%2C197%2C94%2C0.2%29%2F22c55e%2F2%2F0.4%2F0%2F1%2F1%2Fpng" width="72" height="72"></a></td>
<td align="center"><a href="https://www.gravatar.com/avatar/de3fe73f6cd2adaac3a8a1fa04d4d80f?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FChris%2520Coyier%2F128%2Frgba%28249%2C115%2C22%2C0.2%29%2Ff97316%2F2%2F0.4%2F0%2F1%2F1%2Fpng"><img src="https://www.gravatar.com/avatar/de3fe73f6cd2adaac3a8a1fa04d4d80f?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FChris%2520Coyier%2F128%2Frgba%28249%2C115%2C22%2C0.2%29%2Ff97316%2F2%2F0.4%2F0%2F1%2F1%2Fpng" width="72" height="72"></a></td>
<td align="center"><a href="https://ui-avatars.com/api/Brand%20Palette/128/1d4ed833/1d4ed8/2/0.4/0/1/1/svg"><img src="https://ui-avatars.com/api/Brand%20Palette/128/1d4ed833/1d4ed8/2/0.4/0/1/1/svg" width="72" height="72"></a></td>
<td align="center"><a href="https://ui-avatars.com/api/Tim%20Berners-Lee/128/84cc1633/84cc16/2/0.4/0/1/1/svg"><img src="https://ui-avatars.com/api/Tim%20Berners-Lee/128/84cc1633/84cc16/2/0.4/0/1/1/svg" width="72" height="72"></a></td>
<td align="center"><a href="https://www.gravatar.com/avatar/21a241aa10ee457a5f6b72aca98a4860?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FWade%2520Williams%2F128%2Frgba%2834%2C197%2C94%2C0.2%29%2F22c55e%2F2%2F0.4%2F0%2F1%2F1%2Fpng"><img src="https://www.gravatar.com/avatar/21a241aa10ee457a5f6b72aca98a4860?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FWade%2520Williams%2F128%2Frgba%2834%2C197%2C94%2C0.2%29%2F22c55e%2F2%2F0.4%2F0%2F1%2F1%2Fpng" width="72" height="72"></a></td>
<td align="center"><a href="https://ui-avatars.com/api/Katherine%20Johnson/128/10b98133/10b981/2/0.4/0/1/1/svg"><img src="https://ui-avatars.com/api/Katherine%20Johnson/128/10b98133/10b981/2/0.4/0/1/1/svg" width="72" height="72"></a></td>
<td align="center"><a href="https://www.gravatar.com/avatar/f1e3ab214a976a39cfd713bc93deb10f?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FTJ%2520Holowaychuk%2F128%2Frgba%2814%2C165%2C233%2C0.2%29%2F0ea5e9%2F2%2F0.4%2F0%2F1%2F1%2Fpng"><img src="https://www.gravatar.com/avatar/f1e3ab214a976a39cfd713bc93deb10f?s=128&d=https%3A%2F%2Fui-avatars.com%2Fapi%2FTJ%2520Holowaychuk%2F128%2Frgba%2814%2C165%2C233%2C0.2%29%2F0ea5e9%2F2%2F0.4%2F0%2F1%2F1%2Fpng" width="72" height="72"></a></td>
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
# alpha, size, and ui-avatars.com rendering options as one-off overrides

avatar_url(name="Ada Lovelace", color="#dc2626")
# pick a specific color, skipping the palette

avatar_url(name="Ada Lovelace", alpha=1, background="#000")
# pin the background, let the text color rotate with the palette

avatar_url(name="Ada Lovelace", font_color="#fff")
# pin the text color, let the background rotate with the palette

avatar_url(name="Ada Lovelace", email="ada@example.com", format="png")
# force png or svg, note Gravatar errors for svg default images

avatar_url(name="Ada Lovelace", email="ada@example.com", source="libravatar")
# look up the photo on Libravatar instead of Gravatar

avatar_url(name="Ada Lovelace", email="ada@example.com", source="secure.gravatar.com")
# use a custom Gravatar-compatible photo source

avatar_url(name="Ada Lovelace", region="eu")
# use the EU ui-avatars.com endpoint for generated initials

avatar_url(name="Ada Lovelace", host="avatars.example.com")
# use a custom or self-hosted UI Avatars endpoint

avatar_url(name="Ada Lovelace", mask="hexagon")
# crop the image to a hexagon via wsrv.nl

avatar_url(name="Ada Lovelace", format="webp", proxy="images.example.com")
# use a self-hosted wsrv.nl instance instead of the public api
```

## Configuration

Reconfigure the shared `avatars` instance once, at startup, to change the palette for
every call:

```python
from ui_avatars import avatars

avatars.configure(colors=["#1d4ed8", "#b91c1c"], size=256, rounded=True)
```

Or build your own instance instead:

```python
from ui_avatars import Avatars

avatars = Avatars(colors=["#1d4ed8", "#b91c1c"], size=256)
avatars.build(name="Ada Lovelace", email="ada@example.com")
```

The default palette is [`tailwind_colors`](https://pypi.org/project/tailwind_colors/)'s
`RAINBOW_500`. You can swap the whole palette like so:

```python
from tailwind_colors import TCH

avatars.configure(colors=TCH.RAINBOW_300)
```

For an independent background/text color instead of one tinted from the other, use a
`(background, text)` tuple as a `colors` entry — `alpha` still applies to whichever
background results:

```python
avatars.configure(colors=[("#fee2e2", "#ef4444"), ("#ffedd5", "#f97316")])
```

## Development

```bash
poetry install
poetry run pytest
poetry run ruff check .
```

## License

MIT
