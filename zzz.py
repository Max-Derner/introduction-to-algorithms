from pathlib import Path
import json
from random import randint


root = Path(__file__).parent


def write(file: Path, length: int):
    """Writes a JSON array with length len of random numbers to file"""
    print(f"Writing {length} to {file.name}")
    with file.open('w') as f:
        json.dump(
            [
                randint(0, 32_000)
                for _ in range(length)
            ],
            f,
            indent=2
        )


def main():
    files = {
        "10.json": 10,
        "100.json": 100,
        "1K.json": 1_000,
        "10K.json": 10_000,
        "100K.json": 100_000,
        "1M.json": 1_000_000
    }
    for file, size in files.items():
        write(root / file, size)


if __name__ == "__main__":
    main()
