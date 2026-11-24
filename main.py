"""One-Liner Laugh Lab entry.

Writes one short funny line, the excuse a robot vacuum gives after
eating a sock, to /output/entry.txt and prints it.
"""

import os

# The line is assembled from parts so each beat can be tuned on its own.
PARTS = [
    "I didn't eat your sock, I adopted it.",
    "It lives in my dustbin now, rent free,",
    "with three other socks I also didn't eat.",
]

MAX_CHARS = 200  # competition cap


def build_line():
    line = " ".join(PARTS)
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, over the {MAX_CHARS} cap")
    return line


def main():
    line = build_line()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
