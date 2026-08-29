#!/usr/bin/env python3
"""Portable structural validator for the 70 TV Fusion title release."""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src" / "70 TV.setting"
BUNDLE = ROOT / "dist" / "70 TV.drfx"
BUNDLE_SETTING = "Edit/Titles/70 TV.setting"
EXPECTED_BUNDLE_FILES = {
    "Edit/Titles/70 TV.setting",
    "Edit/Titles/70 TV.wide.png",
    "Edit/Titles/70 TV.wide@2x.png",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_balanced_delimiters(source: str) -> None:
    pairs = {"{": "}", "[": "]", "(": ")"}
    closing = set(pairs.values())
    stack: list[tuple[str, int]] = []
    quote: str | None = None
    escaped = False

    for index, char in enumerate(source):
        if quote:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
            continue
        if char in {'"', "'"}:
            quote = char
        elif char in pairs:
            stack.append((char, index))
        elif char in closing:
            if not stack:
                fail(f"unexpected closing delimiter {char!r} at byte {index}")
            opening, opening_index = stack.pop()
            if pairs[opening] != char:
                fail(
                    f"delimiter mismatch: {opening!r} at byte {opening_index} "
                    f"closed by {char!r} at byte {index}"
                )
    if quote:
        fail("unterminated string")
    if stack:
        opening, index = stack[-1]
        fail(f"unclosed delimiter {opening!r} at byte {index}")


def validate_setting(source_bytes: bytes) -> None:
    try:
        source = source_bytes.decode("utf-8")
    except UnicodeDecodeError as error:
        fail(f"setting is not valid UTF-8: {error}")

    validate_balanced_delimiters(source)

    tool_pattern = (
        r"(?m)^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*"
        r"(?:TextPlus|Transform|Merge|Background|KeyStretcher|BezierSpline)\s*\{"
    )
    tools = set(re.findall(tool_pattern, source))
    source_ops = set(re.findall(r'SourceOp\s*=\s*"([A-Za-z_][A-Za-z0-9_]*)"', source))
    missing = sorted(source_ops - tools)
    if missing:
        fail("unresolved SourceOp references: " + ", ".join(missing))

    required_fragments = {
        'TV70 = GroupOperator {': "TV70 macro",
        'ActiveTool = "TV70"': "active tool",
        'Name = "Texto principal"': "main text control",
        'Name = "Tamaño"': "size control",
        'Name = "Color crema"': "cream color control",
        'Name = "Color naranja"': "orange color control",
        'Name = "Color marrón"': "brown color control",
        'Font = Input { Value = "Montserrat Alternates", }': "open default font",
        "[11] = { 1.055": "overshoot keyframe",
        "[18] = { 1,": "settle keyframe",
        "TimeStretch = KeyStretcher {": "Keyframe Stretcher",
    }
    for fragment, label in required_fragments.items():
        if fragment not in source:
            fail(f"missing {label}: {fragment}")

    if len(tools) != 16:
        fail(f"expected 16 internal tools, found {len(tools)}")
    if len(source_ops) != 16:
        fail(f"expected 16 distinct SourceOp references, found {len(source_ops)}")


def validate_bundle(source_bytes: bytes) -> None:
    if BUNDLE.suffix != ".drfx":
        fail("bundle extension must be lower-case .drfx")
    if not zipfile.is_zipfile(BUNDLE):
        fail("DRFX is not a valid ZIP archive")

    with zipfile.ZipFile(BUNDLE) as archive:
        bad_member = archive.testzip()
        if bad_member:
            fail(f"corrupt ZIP member: {bad_member}")
        files = {name for name in archive.namelist() if not name.endswith("/")}
        if files != EXPECTED_BUNDLE_FILES:
            missing = EXPECTED_BUNDLE_FILES - files
            extra = files - EXPECTED_BUNDLE_FILES
            fail(f"unexpected bundle content; missing={sorted(missing)}, extra={sorted(extra)}")
        if archive.read(BUNDLE_SETTING) != source_bytes:
            fail("bundled setting differs from src/70 TV.setting")


def main() -> None:
    if not SOURCE.is_file():
        fail(f"missing source file: {SOURCE}")
    if not BUNDLE.is_file():
        fail(f"missing release bundle: {BUNDLE}")

    source_bytes = SOURCE.read_bytes()
    validate_setting(source_bytes)
    validate_bundle(source_bytes)

    print("OK: 70 TV release is structurally valid")
    print("  16 internal tools and 16 resolved SourceOp references")
    print("  Inspector controls and animation keyframes present")
    print("  DRFX integrity, paths, thumbnails and source parity verified")


if __name__ == "__main__":
    main()

