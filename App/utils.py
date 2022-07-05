import youtube_dl


def dl_yt(url):
    ydl = youtube_dl.YoutubeDL({})

    with ydl:
        ydl.download([str(url)])


from pytube import YouTube
def pytube_dl(url):
    yt = YouTube(str(url))
    video = yt.streams.filter(file_extension='mp4').first()
    video.download()

