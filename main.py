from pytube import YouTube, Stream

def download(stream: Stream):
    print("Started download of the video")
    stream.download("downloads")
    print("Finished download of the video")

def format_stream(stream: Stream):
    resolution_width = max(len(str(stream.resolution)), 12)
    bitrate_width = max(len(str(stream.bitrate)), 15)
    audio_codec_width = max(len(str(stream.audio_codec)), 15)
    filesize_width = max(len(str(stream.filesize_mb)), 0)

    formatted_resolution = str(stream.resolution).ljust(resolution_width)
    formatted_bitrate = (str(stream.bitrate // 1000) + " kbit/s").ljust(bitrate_width)
    formatted_audio_codec = str(stream.audio_codec).ljust(audio_codec_width)
    formatted_filesize = (str(stream.filesize_mb) + " MB").ljust(filesize_width)

    return f"{formatted_resolution} {formatted_bitrate} {formatted_audio_codec} {formatted_filesize}"

if __name__ == "__main__":
    url = input("Link:\n")

    youtube = YouTube(url)

    print(youtube.title)
    print(f"Thumbnail Url: {youtube.thumbnail_url}")

    streams = youtube.streams.all()
    
    print("[Index] Resolution   Bitrate         Audio Codec     Filesize")
    for i in range(len(streams)):
        stream = streams[i]
        print(f"[{str(i).zfill(2)}]    {format_stream(stream)}")

    print("Please select one of the streams")
    
    selection = int(input())
    stream = streams[selection]

    download(stream)
