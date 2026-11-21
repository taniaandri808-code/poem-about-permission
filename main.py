"""
Competition entry for make.fun poetry contest.
Writes the poem to /output/entry.txt with validation.
"""
import os
import sys

POEM = """The Match

You struck it for me once,
cupped it against the wind,
and set it in my hand.
Burn it to the end, you said.
It's yours now.

I hold the small fire
the way you held it —
close enough to warm me,
far enough to keep
my own fingers."""

def main():
    text = POEM
    if not (1 <= len(text) <= 280):
        sys.exit(f"Error: Text length {len(text)} not in range 1-280")
    if not text.strip():
        sys.exit("Error: Text is only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print("Length:", len(text))

if __name__ == "__main__":
    main()
# Entered in make.fun poetry bounty. No network needed.
# Poem entry ready for submission.
