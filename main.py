"""Entry for make.fun "Invent a Word We Need".

Writes the coined word and its one-line definition to entry.txt.
Deterministic: no network, no randomness, no clock.
"""

import os
import stat

ENTRY = (
    "doorjog: The awkward half-jog you break into when someone holds "
    "a door open for you from too far away."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, 0o644)
    print(ENTRY)


if __name__ == "__main__":
    main()
