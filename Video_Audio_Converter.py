import moviepy.editor as mp
video = mp.VideoFileClip(r"video.mp4")
video.audio.write_audiofile(r"C:\Users\audio.mp3")
