import moviepy.editor as mp
video = mp.VideoFileClip(r"C:\Users\Berkay\OneDrive\Masaüstü\Horizon Forbidden West (Original Soundtrack).mp4")
video.audio.write_audiofile(r"C:\Users\Berkay\OneDrive\Masaüstü\resuult.mp3")