import requests

# retrieve videos
channel_handle = "CeeJayEzz"
api_token = "AIzaSyCxOYKioksl4GPgsKzNdknu6nngliibkyk"
channel_id = "UC6Ow53LcFDzXV2DAqkvzXAA"
api_link = f"https://www.googleapis.com/youtube/v3/channels?key={api_token}&forHandle={channel_handle}&part=contentDetails,statistics,snippet"
response = requests.get(api_link)
data = response.json()
channel_info = data["items"][0]["statistics"]
thumbnail = data["items"][0]["snippet"]["thumbnails"]["high"]["url"]
view_count = channel_info["viewCount"]
sub_count = channel_info["subscriberCount"]
video_count = channel_info["videoCount"]