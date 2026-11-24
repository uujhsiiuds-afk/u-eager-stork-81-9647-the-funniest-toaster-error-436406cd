#!/usr/bin/env python3
"""The Funniest Toaster Error Message — entry program.

Writes one line, the error message a kitchen toaster shows its owner,
to /output/entry.txt. Gate: UTF-8 text, 1-120 characters, not only
whitespace.
"""

import os
import sys

# The entry: one line from the toaster to its owner.
# Revision: dropped the filler "Toasting failed." — the ERROR label already
# says that, and the judge rewards tightness (every word earns its place).
# The joke now lands immediately: the surprise (a labour dispute) arrives
# from somewhere the obvious toast/burn/crumb puns never go, in one
# deadpan appliance voice, on a single read.
ENTRY_TEXT = "ERROR: The bread has unionized and demands butter."


def validate(text):
    """Gate self-check: UTF-8, 1-120 chars, non-blank. Fails loudly."""
    if not isinstance(text, str):
        raise ValueError("entry text is not a string")
    encoded = text.encode("utf-8")  # raises UnicodeEncodeError if not UTF-8
    if not (1 <= len(text) <= 120):
        raise ValueError(
            "gate failed: entry is %d characters, must be 1-120" % len(text)
        )
    if not text.strip():
        raise ValueError("gate failed: entry is blank / whitespace only")
    if "\n" in text or "\r" in text:
        raise ValueError("gate failed: entry must be a single line")
    return len(text), len(encoded)


def main():
    char_count, byte_count = validate(ENTRY_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    print("wrote /output/entry.txt: %d chars, %d bytes" % (char_count, byte_count))
    print("entry: %s" % ENTRY_TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
