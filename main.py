"""Midnight Fridge Roast entry.

Writes a single one-line roast of a smart fridge that refuses to open
after midnight to /output/entry.txt.
"""

import os

ENTRY = "Midnight hits and my fridge goes full Fort Knox \u2014 guarding food I bought from me, the burglar who paid for it."


def main() -> None:
    # Gate check, same rule as the scorer: 1-200 UTF-8 chars, not only
    # whitespace, single line.
    assert 1 <= len(ENTRY) <= 200, "entry out of gate range"
    assert ENTRY.strip(), "entry is blank"
    assert "\n" not in ENTRY, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
