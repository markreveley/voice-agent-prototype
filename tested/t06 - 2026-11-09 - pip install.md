# T06 - pip install

**Date:** November 9, 2026 **Run by:** Claude, in a Claude app voice chat with Mark

## What was run

1. pip install --quiet cowsay
2. pip install --quiet --break-system-packages cowsay, then imported cowsay and printed output.

## Raw output

- Run 1: exit code 1, refused as an externally managed environment (PEP 668). Import failed.
- Run 2: exit code 0. cowsay imported and printed "pip works".

## Observations

- Packages install from PyPI, but only with --break-system-packages.
