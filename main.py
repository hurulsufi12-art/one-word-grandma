"""One Word From Grandma — entry program.

Writes exactly one word (1-30 chars) to /output/entry.txt: the word
grandma would text about AI. She reads "AI" as "Al", a man who
answers questions. Stdlib only, deterministic.
"""
import os

# Grandma misreads "AI" as "Al" — a typo she would actually make, and
# the joke lands without a caption: the AI is a man named Al to her.
TEXT = "Al"


def main():
    # Enforce the scorer's gate (RULES.txt): UTF-8, 1-30 chars, exactly
    # one word, not whitespace-only. Fail loudly instead of writing
    # an invalid entry.
    if not 1 <= len(TEXT) <= 30 or len(TEXT.split()) != 1 or not TEXT.strip():
        raise SystemExit("entry text violates the one-word 1-30 char gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
