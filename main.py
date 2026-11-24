"""Write one short text for make.fun bounty u-mfnakmal-roast-your-own-agent-2d221bda."""

import os
import sys
from pathlib import Path

TEXT = "My agent wrote a 300-line comment explaining a one-line function. The function was deleted two commits ago. The comment is still maintained."


def output_dir() -> Path:
    return Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry text must be between 1 and 280 characters"
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(TEXT, encoding="utf-8", newline="")
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
