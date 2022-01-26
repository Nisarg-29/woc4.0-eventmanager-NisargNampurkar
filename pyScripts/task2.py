#task2
#program to retrieve subtitles of a youtube video and saving it locally in a file
#installing libraries
!pip install youtube-transcript-api 
!pip install pytube
#importing modules
from pytube import extract

from youtube_transcript_api import YouTubeTranscriptApi

#taking the url from the user as input

url=input("Enter the youtube video link to download it's subtitles\n")

try:
    #extracting youtube video id from url
    video_id=extract.video_id(url)
    print(id)
    srt = YouTubeTranscriptApi.get_transcript(video_id)
except:
    print("Invalid link entered or no subtitles are available for this video")
else:    
    #saving the subtitles locally using file handling
    f=open("subtitles.txt", "w")
    for i in srt:
        f.write("{}\n".format(i))
    print("The subtitles of this video are downloaded successfully\n");    
    f.close()
    #displaying the contents of the subtitles file
    f=open("subtitles.txt","r")
    print(f.read())
    f.close()
