# 70 TV

A reusable **DaVinci Resolve 21** Fusion title inspired by 1970s television graphics.

![70 TV preview](docs/70-TV-preview.png)

> The preview uses a presentation background. The installed title has a transparent background.

## Features

- Editable main text, font, style, size, tracking and position.
- Editable cream, orange and brown palette.
- Multi-layer stepped extrusion.
- Soft 18-frame entrance with a 105.5% overshoot.
- Transparent background and custom Effects Library thumbnail.
- Keyframe Stretcher keeps the entrance intact when the clip duration changes.
- No third-party Fusion plugins or bundled media.

## Installation

Download `70 TV.drfx` from [Releases](https://github.com/pacoestrada/70-tv-fusion-title/releases/latest), open a Resolve project, go to the **Fusion** page and drag the file onto the page. Confirm installation, then find **70 TV** under **Edit → Effects Library → Titles**.

For a manual Linux installation, copy [`src/70 TV.setting`](src/70%20TV.setting) to:

```text
~/.local/share/DaVinciResolve/Fusion/Templates/Edit/Titles/
```

Restart Resolve after a manual installation.

## Font

The default typeface is **Montserrat Alternates Bold**. The font file is not bundled. Montserrat is available under the [SIL Open Font License 1.1](https://github.com/JulietaUla/Montserrat/blob/master/OFL.txt). Any installed heavy font can be selected from the Inspector.

## Compatibility and validation

Verified with **DaVinci Resolve Studio 21.0.3 on Linux**. The title only uses standard Fusion tools. The `.setting` was accepted by Fusion's embedded Lua parser and loaded by `bmd.readfile`; all internal references and the `.drfx` structure were also checked. Portable checks run through GitHub Actions on every change.

See the detailed [Spanish README](README.md), [architecture notes](docs/ARCHITECTURE.md), and [validation report](VALIDATION.md).

## License and trademarks

Design, direction and publication: **Paco Estrada**. Implementation and documentation were developed with assistance from OpenAI Codex.

Released under the [MIT License](LICENSE). DaVinci Resolve and Blackmagic Design are trademarks of Blackmagic Design Pty. Ltd. This independent project is not affiliated with, sponsored by, or endorsed by Blackmagic Design.

