from pytube import YouTube
from urllib.request import urlopen, Request
from re import findall
from VA_voice import say

def downloader(search_query):
    search_query = "https://www.youtube.com/results?search_query=" + search_query.replace(" ", "%20")

    http_request = Request(url=search_query)        # Creating a request with the specific url
    byte_data = urlopen(http_request)               # fetching the webpage meta data 
    watch_urls = findall(r"/watch\?v=\S{11}", byte_data.read().decode())  # scanning(or reading) and decoding the meta data into actual html, then using regex's findall method to extract all the watch urls from it.
    
    watch_urls = "https://www.youtube.com" + watch_urls[0]    # combining the first watch url with the base homepage url to convert it into a absolute url.


    def stream(watch_url, video_required=False):
        obj = YouTube(url=watch_url)
        download_path = None
        msg = None

        if video_required:
            stream = obj.streams.get_by_itag(22)
            download_path = r"C:\Users\NoThisIsSubham\Videos"
            msg = "Video downloaded successfully"


        else:
            stream= obj.streams.get_audio_only()
            download_path = r"C:\Users\NoThisIsSubham\Music\My Songs"
            msg = "this song has been added to your playlist successfully"

        try:
            say("Downloading has been initialized...")
            stream.download(output_path=download_path) 
            say(msg) 

        except:
            say("Sorry! Downloading has failed")

    stream(watch_urls, video_required=True)


downloader()