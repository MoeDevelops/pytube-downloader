from pytube import YouTube, Stream

def download(stream: Stream):
    print("Started download of the video")
    stream.download("downloads")
    print("Finished download of the video")

def format_stream(stream):
    resolution_width = 12
    bitrate_width = 15
    audio_codec_width = 15
    filesize_width = 10

    formatted_resolution = str(stream.resolution).ljust(resolution_width)
    formatted_bitrate = (str(stream.bitrate // 1000) + " kbit/s").ljust(bitrate_width)
    formatted_audio_codec = str(stream.audio_codec).ljust(audio_codec_width)
    formatted_filesize = (str(stream.filesize_mb) + " MB").ljust(filesize_width)

    formatted_stream = f"{formatted_resolution} {formatted_bitrate} {formatted_audio_codec} {formatted_filesize}"

    if stream.resolution == None:
        formatted_stream = "\033[36m" + formatted_stream + "\033[0m"

    if stream.audio_codec == None:
        formatted_stream = "\033[35m" + formatted_stream + "\033[0m"

    return formatted_stream


if __name__ == "__main__":
    url = input("Link:\n")

    youtube = YouTube(url)

    print(youtube.title)
    print(f"Thumbnail Url: {youtube.thumbnail_url}")

    streams = youtube.streams.all()

    print("If the text is magenta, the stream doesn't have audio")
    print("If the text is cyan, the stream doesn't have video")
    print()
    print("[Index] Resolution   Bitrate         Audio Codec     Filesize")
    for i in range(len(streams)):
        stream = streams[i]
        streamMessage = f"[{str(i).zfill(2)}]    {format_stream(stream)}"

        print(streamMessage)
    
    print("Please select one of the streams")

    selection = int(input())
    stream = streams[selection]

    download(stream)
