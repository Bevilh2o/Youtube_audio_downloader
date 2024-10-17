# Audio Downloader and Converter

This script allows users to download audio from YouTube videos and convert it to MP3 format. The script uses `yt-dlp` for downloading and `ffmpeg` for conversion.

## Features

- Downloads audio in `m4a` format.
- Extracts the audio bitrate and maintains it during conversion to MP3.
- Sanitizes filenames to remove invalid characters.
- Automatically uses the video title as the name for the output MP3 file.

## Requirements

- Python 3.x
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg](https://ffmpeg.org/)

## Installation

1. Download and install Python if not already installed.
2. Install `yt-dlp` using pip:
   ```bash
   pip install yt-dlp
   ```
3. Download FFmpeg and set the paths in the script accordingly. **It's important to modify the application paths in the script to match your local installation.**

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script:
   ```bash
   python your_script_name.py
   ```
4. When prompted, paste the URL of the YouTube video.

## License

This project is licensed under the MIT License.
