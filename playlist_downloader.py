from pytube import Playlist
pl = Playlist("https://www.youtube.com/watch?v=wXcdYBh3hgg&list=PLVuQBUGB87-gomoG36CV4wMZCkGPGKw3p")
#pl.download_all()
# or if you want to download in a specific directory
#print(pl.streams.filter(subtype='mp4').all())
pl.download_all('E:\Youtube-Video-Downloader\Videos')