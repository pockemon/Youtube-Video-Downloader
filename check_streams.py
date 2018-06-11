#Reference file
#To view that what all video streams are available we can check it like this:

from pytube import YouTube
yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
print(yt.streams.all())

#To list only audio streams:
print(yt.streams.filter(only_audio=True).all())

#To list only mp4 streams:
print(yt.streams.filter(subtype='mp4').all())



