import os
import uuid
import subprocess

def download_audio(youtube_url, output_folder="audio_files"):
    os.makedirs(output_folder, exist_ok=True)
    unique_id = str(uuid.uuid4())[:8]
    output_template = os.path.join(output_folder, f"%(title)s_{unique_id}.%(ext)s")
    command = ["yt-dlp", "--extract-audio", "--audio-format", "m4a", "--output", output_template, youtube_url]
    subprocess.run(command, check=True)
    return output_template