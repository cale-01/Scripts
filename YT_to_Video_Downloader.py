# YouTube Video Downloader By Cale Aldunate
# This script functions on other platforms with video content, 
# and the same applies to the audio downloader script on GitHub

"""
This script downloads the highest quality video from a YouTube video 
as an MP4 file.
"""

import yt_dlp

def download_video_from_youtube(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Target best video and audio
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': True,
        'no_warnings': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Prompt the user to enter a YouTube video URL
url = input("Enter the YouTube video URL: ")
download_video_from_youtube(url)
print("Video downloaded in the highest quality available.")
