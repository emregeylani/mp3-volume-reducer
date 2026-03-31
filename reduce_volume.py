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


def get_output_dir(path, percent):
    p = Path(path)
    base = p.parent if p.is_file() else p
    return base / f"reduced_volume_{percent}"


def output_path(file, out_dir):
    return out_dir / file.name


def reduce_volume(file, percent, out_dir):
    out = output_path(file, out_dir)

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

    out_dir = get_output_dir(target, percent)
    out_dir.mkdir(exist_ok=True)

    log(f"{len(files)} file(s) found")
    log(f"Output directory: {out_dir}")

    for f in files:
        reduce_volume(f, percent, out_dir)

    log("Done.")


if __name__ == "__main__":
    main()