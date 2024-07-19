# Need to have FFmpeg installed for post processing and other features
# The code still works without FFmpeg installed but has limitations
import yt_dlp

# Step 2: Download YouTube video
def download_audio_from_youtube(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',  # YouTube video title as the filename
        'quiet': True,  # Suppress output
        'no_warnings': True,  # Suppress warnings
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Prompt the user to enter a YouTube video URL
url = input("Enter the YouTube video URL: ")
download_audio_from_youtube(url)
print("Audio downloaded and converted to MP3 format.")
