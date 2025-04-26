''' '''

from pytube import YouTube

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video Downloaded Successfully!")
    except Exception as e:
        print("Error:", e)

url = "https://www.youtube.com/watch?v=TKt2ZodI7FI"
save_path = "C:/Users/Hamro Computers/Pictures/TWC/Programming/Projects"
download_video(url, save_path)
