import scrapetube
from pytube import YouTube
from pytube.innertube import _default_clients
import os
import json
import unicodedata

#to make sure age restricted videos can be downloaded using the pytube library
_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]

json_file_path = 'videos.json'

#function to make sure that there are no illegal characters in the video filename
def sanitize_filename(filename):
    # Replace invalid characters with underscores
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    
    # Normalize the filename to remove or replace non-ASCII characters
    filename = unicodedata.normalize('NFKD', filename).encode('ascii', 'ignore').decode('ascii')
    
    return filename

#checks json file
def check(json_file_path, string_to_check):
    string_to_check = sanitize_filename(string_to_check)
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as file:
            video_data = json.load(file)
            for video in video_data:
                if video['name'] == string_to_check:
                    print(f"Match found: {string_to_check}")
                    return True
                else:
                    print(f"No match found for: {string_to_check}")
    return False

#writes to json file
def write(json_file_path, video_title, video_path):
    video_entry = {
        "name": video_title,
        "path": video_path
    }
    
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r+') as file:
            video_data = json.load(file)
            video_data.append(video_entry)
            file.seek(0)
            json.dump(video_data, file, indent=4)
    else:
        with open(json_file_path, 'w') as file:
            json.dump([video_entry], file, indent=4)

#download the video from the video id
def download(video_id, video_title):

    # generates video link based on the video id that we scraped
    link = f"https://www.youtube.com/watch?v={video_id}"
    print(f"Starting download of {video_id}")

    title = sanitize_filename(video_title)

    video_path = os.path.join('videos', f"{title}.mp4")

    #using the pytube library to download the video by video link
    YouTube(link).streams.get_highest_resolution().download(output_path='videos', filename=f"{title}.mp4")
    #YouTube(link).streams.first().download( filename=f"{video_title}.mp4")
    print(f"Downloaded {video_id}")
    
    return video_path

# using scrapetube to get the channel that we want to scrape using scrapetube library
# limit = the number of videos to pull up
# sleep = the number of seconds between clicks if im not mistaken (they recommend to use higher to prevent from getting blocked)
# sort by = newest to get the latest videos
# content-type = filters only normal videos and removes all shorts, and other things
videos = scrapetube.get_channel(channel_username="Foxsoccer", limit=20, sleep=10, sort_by='newest', content_type="videos")

highlight_videos = []


for video in videos:
    # get the title for each video
    title = video['title']['runs'][0]['text']
    # get the video id for each video
    video_id = video['videoId']
    
    # filters the videos with either highlights or penalty and euro in the title
    # this is  done to follow the foxsoccer channel naming scheme where this filters the exact videos that we want to download
    if ("Highlights" in title or "Full Penalty Shootout" in title) and "UEFA Euro 2024" in title:
        highlight_videos.append(video)
        print(video_id, title)
        
        #checks the json file if the video is already downloaded,  if not downloaded then it downloads it 
        if not check(json_file_path, title): 
            print("Must download this")
            video_path = download(video_id, title)
            write(json_file_path, title, video_path)
