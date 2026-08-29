# Contributing

Contributions, compatibility reports and design variants are welcome.

## Before opening a pull request

1. Keep the template dependency-free: standard Fusion tools only.
2. Preserve the editable Inspector controls unless the change is explicitly breaking.
3. Keep the internal package path as `Edit/Titles/70 TV.setting`.
4. Run the validator:

   ```bash
   python3 tools/validate_release.py
   ```

5. Update `CHANGELOG.md` when behavior or controls change.
6. Include the exact Resolve version, edition and operating system used for visual testing.

## Design variants

For a materially different design, consider adding a new title rather than replacing the visual identity of `70 TV`. Reusable variants should keep their own source `.setting`, thumbnail and release notes.

## Bug reports

Please include:

- DaVinci Resolve version and build.
- Free or Studio edition.
- Operating system and display server where relevant.
- Whether the `.drfx` or `.setting` installation method was used.
- Screenshot or error text.
- Timeline resolution and frame rate.

