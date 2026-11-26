#!/usr/bin/env python3
"""
# Entry validated: output is 1-240 chars, exactly one line, deterministic.
Printer's comeback: the machine that watches every 'quick question'
balloon into a 47-page deck and times it, deadpan.
"""
import os
import sys

LINE = "5:59 PM: 'quick question' becomes a 47-page deck. I timed it. You're welcome."

def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")

    content = LINE + "\n"
    
    # Validate: 1-240 chars total including newline, not only whitespace, exactly one line
    if not (1 <= len(content) <= 240 and content.strip() and content.count("\n") == 1):
        raise ValueError("Content validation failed")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Wrote {output_path} ({len(content)} chars)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
