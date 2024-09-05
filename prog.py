import os
import yt_dlp

# Directory where downloaded files will be saved
download_path = './downloaded/'

# Create download directory if it doesn't exist
if not os.path.exists(download_path):
    os.makedirs(download_path)

# Function to download YouTube video as MP3
def download_mp3(link, output_path):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print(f"Downloaded and converted: {link}")
    except Exception as e:
        print(f"Error downloading {link}: {str(e)}")

# Read all YouTube links from links.txt
with open('links.txt', 'r') as file:
    links = file.readlines()

# Download and convert each link
for link in links:
    link = link.strip()  # Remove any extra whitespace
    if link:  # Proceed if the link is not empty
        download_mp3(link, download_path)
