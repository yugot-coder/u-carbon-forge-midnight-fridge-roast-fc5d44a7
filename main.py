"""Midnight Fridge Roast — entry program.

Reads entry.txt (one line of text roasting a smart fridge that refuses to
open after midnight), validates it against the competition gate, writes it
to /output/entry.txt and prints it exactly.

Standard library only.
"""

import os

MAX_CHARS = 200


def check_gate(text):
    """Validate one entry against the competition gate.

    The gate: UTF-8 text of 1 to 200 characters, not only white space.
    Returns the cleaned text, or raises ValueError with the reason.
    """
    if not text:
        raise ValueError("entry is empty")
    if text.strip() == "":
        raise ValueError("entry is only white space")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the 200 limit" % len(text)
        )
    return text


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), encoding="utf-8") as f:
        text = check_gate(f.read().strip())

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)

    print(text)


if __name__ == "__main__":
    main()
