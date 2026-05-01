"""
read_lines.py — A lazy file reader using generator + yield (Day 2 practice)

Demonstrates the `yield` keyword and lazy evaluation. Each line is read
and yielded one at a time, so memory footprint stays constant regardless
of file size.

Why this matters in medical imaging:
- Loading thousands of DICOM slices into a list = OOM risk
- Generator allows processing one slice at a time

Day 2 of Phase 1 study (radiology residency reapplication 2026-2027)
"""

from typing import Generator


def read_lines(path: str) -> Generator[str, None, None]:
    """Yield one stripped line at a time from the file at `path`."""
    print(f"  [body] opening {path}")
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            print(f"  [body] about to yield: {line.rstrip()!r}")
            yield line.rstrip('\n')
    print(f"  [body] finished, file closed")


if __name__ == '__main__':
    import os

    # Create a small test file
    test_file = 'sample.txt'
    with open(test_file, 'w', encoding='utf-8') as f:
        for i in range(1, 6):
            f.write(f"Line {i}\n")

    # Step 1: Calling the generator function
    print("=== Step 1: Calling read_lines() ===")
    gen = read_lines(test_file)
    print(f"Got: {gen}")
    print(f"Type: {type(gen).__name__}")
    print("(Notice: body did NOT execute yet)\n")

    # Step 2: Pull two values via next()
    print("=== Step 2: First two next() calls ===")
    print(f"first  -> {next(gen)}")
    print(f"second -> {next(gen)}\n")

    # Step 3: Continue with for loop (state preserved)
    print("=== Step 3: Continuing with for loop ===")
    for line in gen:
        print(f"got -> {line}")

    # Cleanup
    os.remove(test_file)