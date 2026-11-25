"""The Meeting That Should Have Been One Line — entry program.

Writes the single sentence that could have replaced an entire pointless
meeting to /output/entry.txt. Deterministic: same bytes on every run.

The line kills the meeting outright: the decision was already made, so
the meeting itself was only ever the long way of hearing "no" — a sting
anyone who has sat through a useless meeting recognises at once.
"""

import os


ENTRY = "The answer is no, the answer was always no, and this meeting was the long way of hearing it."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, target)
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
