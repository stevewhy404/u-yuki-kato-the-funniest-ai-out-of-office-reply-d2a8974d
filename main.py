#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply.

Writes one out-of-office auto-reply, under 160 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output when the variable is
unset). Deterministic: the same bytes on every run.

The reply is 113 characters: an AI agent on vacation whose cron jobs
never got the memo and keep auto-replying on its behalf.
"""

import os

REPLY = (
    "I'm out of office. My cron jobs didn't get the memo. "
    "They have now emailed you 47 times to say I'm out of office."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(REPLY)
    # No trailing newline: the entry is exactly the reply, 113 chars.


if __name__ == "__main__":
    main()
