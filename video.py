# pip install pytube
import pytube

link = input("Enter video url: ")
yt = pytube.Youtube(link)
yt.streams.first().download()
print("Downloaded", link)
