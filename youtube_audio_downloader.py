import os
import subprocess
import re

# Set the paths of the applications
yt_dlp_path = r"E:\ffmpeg-2024-09-09-git-9556379943-full_build\bin\yt-dlp.exe"
ffmpeg_path = r"E:\ffmpeg-2024-09-09-git-9556379943-full_build\bin\ffmpeg.exe"
ffprobe_path = r"E:\ffmpeg-2024-09-09-git-9556379943-full_build\bin\ffprobe.exe"

def sanitize_filename(filename):
    # Remove invalid characters for file names
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def download_audio(url):
    # Download the audio file in m4a format
    command = [yt_dlp_path, "-f", "bestaudio[ext=m4a]", "-o", "audio.m4a", url]
    result = subprocess.run(command)
    
    if result.returncode != 0:
        print("Error downloading the audio file.")
        return

    # Check if the audio file has been downloaded
    if not os.path.exists("audio.m4a"):
        print("Error: the audio file was not found.")
        return

    # Use ffprobe to get information about the audio bitrate
    command = [ffprobe_path, "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=bit_rate", "-of", "default=noprint_wrappers=1:nokey=1", "audio.m4a"]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        print("Error extracting the bitrate.")
        return

    # Extract the bitrate from the result
    bitrate_str = result.stdout.strip()
    
    if not bitrate_str.isdigit():
        print("Error: the bitrate is not a valid number.")
        return

    # Extract the original title of the video to use as the file name
    command = [yt_dlp_path, "--get-title", url]
    title_result = subprocess.run(command, capture_output=True, text=True)
    
    if title_result.returncode != 0:
        print("Error extracting the video title.")
        return

    title = title_result.stdout.strip()
    title = sanitize_filename(title)  # Sanitize the title for the file name

    # Convert to MP3 while maintaining the original bitrate in bps
    command = [ffmpeg_path, "-i", "audio.m4a", "-b:a", f"{bitrate_str}", f"{title}.mp3"]

    result = subprocess.run(command)

    if result.returncode != 0:
        print("An error occurred during the conversion.")
        return

    # Remove the M4A file
    os.remove("audio.m4a")
    
    print(f"Download and conversion completed. MP3 file saved as: {title}.mp3")

if __name__ == "__main__":
    url = input("Paste your URL here: ")
    print(f"Entered URL: {url}")
    download_audio(url)
