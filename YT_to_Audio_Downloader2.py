# This version downloads the highest quality audio available from the YouTube video without using FFmpeg
import yt_dlp

def download_audio_from_youtube(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',  # Save the file with the YouTube video title as the filename
        'quiet': True,  # Suppress output to keep the console clean
        'no_warnings': True,  # Suppress warnings
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Prompt the user to enter a YouTube video URL
url = input("Enter the YouTube video URL: ")
download_audio_from_youtube(url)
print("Audio downloaded in the highest quality available.")
