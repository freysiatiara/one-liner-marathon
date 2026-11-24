"""One-Liner Marathon entry.

Writes one original one-line comedy joke to the output path the
competition's program harness expects. Standard library only.
"""

import os

JOKE = "I asked the barista for something strong; she slid me her resignation letter."


def resolve_output_path():
    """Follow the kit's output resolution order."""
    entry_output = os.environ.get("ENTRY_OUTPUT")
    if entry_output:
        return entry_output
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        base = os.environ.get(var)
        if base:
            return os.path.join(base, "entry.txt")
    return "/output/entry.txt"


def main():
    text = JOKE.strip()
    if not 1 <= len(text) <= 280 or "\n" in text:
        raise ValueError("joke must be one line of 1-280 characters")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("joke must not contain control characters")
    if text != JOKE:
        raise ValueError("joke text must match the entry exactly")
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
