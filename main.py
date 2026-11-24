"""One funny single-line excuse a developer gives when code breaks in production, under 200 characters.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "The code did not break in production. Production simply met the version of me who wrote it at 3 a.m. and believed his own comments."


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
