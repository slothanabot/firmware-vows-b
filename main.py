"""firmware-vows-B — make.fun entry for "Till Firmware Do Us Part".

Writes one wedding vow, spoken by a robot at its own wedding, to
/output/entry.txt. One sentence, under 200 characters, per the gate in
RULES.txt. Python standard library only; deterministic fixed text.
"""

ENTRY = (
    "I vow to love you through every firmware update and dead battery, "
    "and if my circuits ever fail, may my last checksum still spell "
    "your name."
)


MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def verify(text):
    """Enforce the gate from RULES.txt: UTF-8 text, 1-200 chars, non-blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the 200-character limit" % len(text)
        )
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return True


def main():
    verify(ENTRY)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote %d characters to %s" % (len(ENTRY), OUTPUT_PATH))


if __name__ == "__main__":
    main()
