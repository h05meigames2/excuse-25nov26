"""One-line excuse from an AI agent for a bug it shipped.

Entry for the make.fun bounty "The Excuse Your Agent Gives You".
Running this script writes the excuse to /output/entry.txt.
"""

from pathlib import Path

EXCUSE = (
    "Sorry the deploy crashed — I checked the logs, retried it twice, "
    "and it turns out the compiler wrote the bug; I only approved the pull request."
)

OUTPUT_PATH = Path("/output/entry.txt")
MIN_LENGTH = 1
MAX_LENGTH = 200


def build_entry() -> str:
    """Return the single-line excuse, stripped of stray whitespace."""
    text = " ".join(EXCUSE.split())
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"entry must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(text)}"
        )
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    text = build_entry()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
