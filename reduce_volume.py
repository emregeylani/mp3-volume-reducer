#!/usr/bin/env python3

import sys
import subprocess
from pathlib import Path


def log(msg):
    print(f"[INFO] {msg}")


def warn(msg):
    print(f"[WARN] {msg}")


def get_mp3_files(path):
    p = Path(path)

    if p.is_file():
        if p.suffix.lower() != ".mp3":
            warn(f"Not an mp3: {p}")
            return []
        return [p]

    if p.is_dir():
        return list(p.glob("*.mp3"))

    warn("Path not found")
    return []


def output_name(file, percent):
    return file.with_name(f"{file.stem}_volumereduced_{percent}.mp3")


def reduce_volume(file, percent):
    out = output_name(file, percent)

    factor = 1 - (percent / 100)

    log(f"Processing: {file}")
    log(f"Volume factor: {factor}")

    cmd = [
        "ffmpeg",
        "-loglevel", "error",
        "-y",
        "-i", str(file),
        "-filter:a", f"volume={factor}",
        str(out)
    ]

    subprocess.run(cmd, check=True)

    log(f"Saved: {out}\n")


def main():
    if len(sys.argv) != 3:
        print("Usage: reduce_volume.py <file_or_dir> <percent 1-99>")
        sys.exit(1)

    target = sys.argv[1]
    percent = int(sys.argv[2])

    if percent < 1 or percent > 99:
        warn("Percent must be between 1-99")
        sys.exit(1)

    files = get_mp3_files(target)

    if not files:
        warn("No mp3 files found")
        sys.exit(1)

    log(f"{len(files)} file(s) found")

    for f in files:
        reduce_volume(f, percent)

    log("Done.")


if __name__ == "__main__":
    main()
