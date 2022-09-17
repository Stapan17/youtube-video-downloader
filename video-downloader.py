# By default it will download video with high quality!!!
# However it can be customizable.

from pytube import YouTube 

SAVE_PATH = "./"

link=input("Enter YT link: ")

try:
    yt = YouTube(link)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
    print('Video Downloaded!!!')
except:
    print("Connection Error!!!")
