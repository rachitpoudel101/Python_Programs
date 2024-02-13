from pytube import YouTube

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=save_path)
        print("Download successful!")
    except Exception as e:
        print("An error occurred:", str(e))

def main():
    video_url = input("Enter the YouTube video URL: ")
    save_path = input("Enter the directory path to save the video: ")
    download_video(video_url, save_path)

if __name__ == "__main__":
    main()