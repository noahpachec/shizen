from pathlib import Path
import subprocess

folder = Path("mined_recordings")

video_extensions = {".mp4", ".mov", ".mkv", ".avi", ".webm"}

for video in folder.iterdir():
    if video.suffix.lower() in video_extensions:
        output = video.with_suffix(".mp3")

        print(f"Converting {video.name} -> {output.name}")

        subprocess.run([
            "ffmpeg",
            "-i", str(video),
            "-vn",
            "-q:a", "2",
            str(output)
        ], check=True)