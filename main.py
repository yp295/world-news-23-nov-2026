"""Entry generator: World News 23 November 2026 in one image.

Reads the bundled newspaper image (news.png, stored next to this file)
and writes it unchanged to /output/entry.png.

Standard library only. No network access, no randomness, no clock:
the same input bytes always produce the same output bytes.
"""

import hashlib
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "news.png"
TARGET = Path("/output/entry.png")

# sha256 of the bundled image, recorded when the entry was built.
# The program refuses to copy if the bundled file no longer matches.
EXPECTED_SHA256 = (
    "d42271cd48a1ee8eb5de7ca9f1a6925763daa2271b6bf113e4f83257b2b88d31"
)


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 16), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    if not SOURCE.is_file():
        print(f"bundled image not found: {SOURCE}", file=sys.stderr)
        return 1
    if sha256_of(SOURCE) != EXPECTED_SHA256:
        print("bundled image hash mismatch, refusing to copy", file=sys.stderr)
        return 1
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    if sha256_of(TARGET) != EXPECTED_SHA256:
        print("output hash mismatch", file=sys.stderr)
        return 1
    print(
        f"wrote {TARGET} "
        f"({TARGET.stat().st_size} bytes, "
        f"sha256 {EXPECTED_SHA256[:12]}...)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
