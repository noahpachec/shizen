from pathlib import Path
import subprocess

def convert_to_mp3(file, output_dir):

    file = Path(file)

    video_extensions = {".mp4", ".mov", ".mkv", ".avi", ".webm"}

    if file.suffix.lower() not in video_extensions:
        return None

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)


    output = output_dir / file.with_suffix(".mp3").name
    
    print(f"Converting {file.name} -> {output.name}")

    subprocess.run([
        "ffmpeg",
        "-y",
        "-loglevel", "error",
        "-i", str(file),
        "-vn",
        "-q:a", "2",
        str(output)
    ], check=True)

    return output

# folder = Path("mined_recordings")

# video_extensions = {".mp4", ".mov", ".mkv", ".avi", ".webm"}

# for video in folder.iterdir():
#     if video.suffix.lower() in video_extensions:
#         output = video.with_suffix(".mp3")

#         print(f"Converting {video.name} -> {output.name}")

#         subprocess.run([
#             "ffmpeg",
#             "-i", str(video),
#             "-vn",
#             "-q:a", "2",
#             str(output)
#         ], check=True)