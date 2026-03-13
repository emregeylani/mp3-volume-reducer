# MP3 Volume Reducer

Small Python utility to reduce the volume of MP3 files using **ffmpeg**.

Designed to be simple and dependency-light.

## Features

-   Accepts **single MP3 file** or **directory**
-   Batch processes all `.mp3` files in a folder
-   Volume reduction by **percentage (1--99)**
-   Clear console logs
-   Output filename format:

```{=html}
<!-- -->
```
    original_filename_volumereduced_XX.mp3

Example:

    song.mp3
    → song_volumereduced_30.mp3

## Requirements

-   Python 3
-   ffmpeg

Install ffmpeg on Ubuntu:

``` bash
sudo apt install ffmpeg
```

No Python audio libraries are required.

## Usage

### Reduce volume of a single file

``` bash
python3 reduce_volume.py song.mp3 30
```

### Reduce volume for all MP3 files in a directory

``` bash
python3 reduce_volume.py ./music 30
```

## Parameter Reference

    reduce_volume.py <file_or_directory> <percentage>

  Parameter           Description
  ------------------- --------------------------------------------
  file_or_directory   MP3 file or directory containing MP3 files
  percentage          Volume reduction between **1 and 99**

Example:

    python3 reduce_volume.py podcast.mp3 40

## Behavior

-   Only `.mp3` files are processed
-   Subdirectories are **not scanned**
-   Original files are **never modified**
-   New file is created with `_volumereduced_XX` suffix

## Example Output

    [INFO] 3 file(s) found
    [INFO] Processing: track1.mp3
    [INFO] Volume factor: 0.7
    [INFO] Saved: track1_volumereduced_30.mp3
    [INFO] Done.

## License

MIT
