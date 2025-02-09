from downloader import download_audio
from transcript import generate_transcript
from config import API_KEY

def main():
    youtube_url = input("Enter YouTube URL: ")
    audio_file = download_audio(youtube_url)
    transcript = generate_transcript(audio_file, API_KEY)
    print("Generated Transcript:", transcript)

if __name__=="__main__":
    main()