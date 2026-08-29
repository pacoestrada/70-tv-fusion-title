# Validation report

## Release under test

- Version: `1.0.0`
- Host: DaVinci Resolve Studio `21.0.3.0007`
- Operating system: Linux
- Validation date: `2026-08-29`

## Native Fusion validation

The standalone setting was checked with the Lua runtime shipped with Fusion 21:

1. `loadstring` accepted the complete `.setting` as a Fusion table expression.
2. `bmd.readfile` loaded the settings table.
3. The returned table contained `Tools.TV70`.
4. `ActiveTool` resolved to `TV70`.
5. The nested graph contained the expected `TextMask` tool.

## Structural validation

- 16 internal tool definitions found.
- 16 distinct `SourceOp` references found.
- Every `SourceOp` resolves to a defined internal tool.
- Inspector controls for main text, size and all three colors are present.
- Overshoot keyframe at frame 11 has a value of `1.055`.
- Settle keyframe at frame 18 has a value of `1.0`.
- Opacity animation runs from frame 0 to frame 12.

## Bundle validation

The `.drfx` archive passed ZIP integrity checks and contains only:

```text
Edit/
Edit/Titles/
Edit/Titles/70 TV.setting
Edit/Titles/70 TV.wide.png
Edit/Titles/70 TV.wide@2x.png
```

The bundled `.setting` is byte-identical to `src/70 TV.setting`.

## Continuous validation

`tools/validate_release.py` repeats the portable structural and bundle checks in GitHub Actions. Native `bmd.readfile` validation requires a local Fusion/Resolve runtime and therefore is recorded here rather than executed on GitHub-hosted runners.

