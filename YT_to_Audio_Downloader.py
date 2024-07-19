# YouTube Audio Downloader By Cale Aldunate

"""
This script downloads the highest quality audio from a YouTube video 
as an MP4A file. 

You can modify the script to download MP3 audio by changing the 'format' 
parameter in the ydl_opts dictionary.

"""

import yt_dlp

def download_audio_from_youtube(url):
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/bestvideo[ext=m4a]+bestaudio[ext=m4a]',  # Target MP4A audio, can change to mp3 if preferred
        'outtmpl': '%(title)s.%(ext)s',  
        'quiet': True,
        'no_warnings': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Prompt the user to enter a YouTube video URL
url = input("Enter the YouTube video URL: ")
download_audio_from_youtube(url)
print("Audio downloaded in the highest quality MP4A available.")



# To download as MP3, change the 'format' parameter to:
# 'format': 'audio/mp3' 