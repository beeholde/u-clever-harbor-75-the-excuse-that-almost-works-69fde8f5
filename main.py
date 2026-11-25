"""The Excuse That Almost Works — entry program.

Writes one line (the excuse a gamer texts the boss to skip work on
GTA 6 launch week) to /output/entry.txt. Standard library only.
"""

import os
from pathlib import Path

LINE = "Sorry, my driving test got moved to 9:30, miss it and I lose the fee and the slot."


def main() -> None:
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
