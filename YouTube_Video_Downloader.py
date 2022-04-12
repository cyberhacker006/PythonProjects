from pytube import YouTube
link = input("Enter a video link: ")
yt = YouTube(link)
video = yt.streams.get_highest_resolution()
save_path = r"C:\Users\Youtube"
video.download(save_path)
