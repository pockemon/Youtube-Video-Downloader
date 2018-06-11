#This example will download the highest quality progressive download stream available.

import pytube
link = "https://www.youtube.com/watch?v=opHGwinvsUY"
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()

'''
or
from pytube import YouTube
YouTube("https://www.youtube.com/watch?v=opHGwinvsUY").streams.first().download()
'''
