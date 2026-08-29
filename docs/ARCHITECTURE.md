# 70 TV architecture

## Rendering graph

`TextMask` is the single source of text, font, size, tracking and opacity. Every color layer is derived from that mask, so editing the text updates the complete construction at once.

### Front face

`CreamColor` is a full-frame Fusion Background limited by `TextMask`. It produces the cream front face.

### Orange extrusion

`OrangeStep1`, `OrangeStep2` and `OrangeStep3` offset the text mask by progressively larger amounts. The masks are combined and applied to `OrangeColor`, producing a continuous-looking stepped orange depth.

### Brown depth

`BrownStep` uses the largest offset. It masks `BrownColor` and creates the deepest shadow layer.

### Composite

`MergeDepth` places orange over brown. `MergeFace` adds the cream face. `EntryTransform` applies the animated scale to the complete composite, so all layers remain aligned.

### Timing

`EntryScale` is a Bezier spline with keys at frames 0, 11 and 18. `EntryOpacity` fades the mask between frames 0 and 12. `TimeStretch` preserves the animation while allowing the title clip to have an arbitrary practical duration.

## Inspector interface

The macro exposes only production-facing controls through `InstanceInput` entries. Animation internals and layer offsets remain protected inside the group to keep the Edit-page Inspector concise.

## Resolution independence

Fusion tools use the timeline format through `UseFrameFormatSettings = 1`. Positions and offsets are normalized, allowing the title to scale with different timeline resolutions.

