"""
Six Words, One Story entry: "We buried his phone. It buzzed."

A complete horror micro-story in six words — setup, pivot, twist.
"""
import os
import pathlib

STORY = "We buried his phone. It buzzed."


def main() -> None:
    output_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry = output_dir / "entry.txt"
    entry.write_bytes(STORY.encode("utf-8"))
    print(entry)


if __name__ == "__main__":
    main()
