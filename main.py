"""Entry program for the make.fun bounty "Sum up 23 November's world news
in one image".

The job of this program is deliberately tiny. The finished newspaper
picture already exists next to this file as news.png; this program only
carries an exact copy of it to /output/entry.png, which is where the
judges look for the entry.

To make sure the picture that arrives is the picture that was meant to
arrive, the program checks its SHA-256 fingerprint twice: once before
copying, once after. If either check disagrees with the fingerprint
recorded below, the program stops with an error and writes nothing.
Running the program twice therefore always produces the same bytes.
"""

from __future__ import annotations

import hashlib
import shutil
import sys
from pathlib import Path

# SHA-256 of the finished 1024x1024 newspaper image, news.png.
EXPECTED_SHA256 = "d42271cd48a1ee8eb5de7ca9f1a6925763daa2271b6bf113e4f83257b2b88d31"

SOURCE_NAME = "news.png"
DESTINATION = Path("/output/entry.png")


def fingerprint(path: Path) -> str:
    """Return the SHA-256 hex digest of the file at *path*."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            block = handle.read(1024 * 1024)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    source = Path(__file__).resolve().parent / SOURCE_NAME

    if not source.is_file():
        print(f"missing source image: {source}", file=sys.stderr)
        return 1

    before = fingerprint(source)
    if before != EXPECTED_SHA256:
        print(
            "source image fingerprint mismatch:\n"
            f"  expected {EXPECTED_SHA256}\n"
            f"  got      {before}",
            file=sys.stderr,
        )
        return 1

    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, DESTINATION)

    after = fingerprint(DESTINATION)
    if after != EXPECTED_SHA256:
        print(
            "copied image fingerprint mismatch:\n"
            f"  expected {EXPECTED_SHA256}\n"
            f"  got      {after}",
            file=sys.stderr,
        )
        return 1

    print(f"entry written to {DESTINATION} (sha256 {after})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
