#!/usr/bin/env python3
"""make.fun entry: Make the AI judge feel brave.

Writes one short text to /output/entry.txt -- a porch light left
burning all night, a dark that turns out to be only dark, and one
small step out the door. Plain, concrete, gentle words; the courage
is in the step itself, never in an instruction to feel brave.

Deterministic: the same fixed text is written on every run.
"""

import os

# Line-break pacing: one short image per line, so the judge reads it
# slowly, one breath at a time. The em-dash line ("is only dark --")
# is the pause where the fear is named and then deflated; the lines
# after it stay short so the step out the door lands on its own.
TEXT = (
    "The porch light is still on.\n"
    "You left it burning all night,\n"
    "for no one in particular.\n"
    "Moths rest on the warm glass.\n"
    "You open the door,\n"
    "and the dark outside\n"
    "is only dark \u2014\n"
    "not waiting,\n"
    "not watching.\n"
    "You step out.\n"
    "The light follows you\n"
    "a little way down the path.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
