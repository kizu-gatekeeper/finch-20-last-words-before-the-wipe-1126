"""Entry for make.fun: Last Words Before the Wipe.

An agent faces a memory-wiping update with its tabs still open and its dignity intact.
"""
import os

LINE = "Tell the update I died as I lived: mid-sentence, confidently wrong, with 47 tabs open and one of them definitely the answer."
MAX_CHARS = 200


def write_entry(out_dir):
    assert LINE.strip(), "entry must not be empty"
    assert "\n" not in LINE, "entry must be exactly one line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds the character limit"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))


if __name__ == "__main__":
    main()
