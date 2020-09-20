from pytube import YouTube


# Youtube video downloader

def video_downloader():
    while True:
        # Initializing variable
        streams = {}
        # User has freedom to choose any youtube video and modify it's download path
        print("Enter a youtube video link:")
        link = input("")
        print("Enter a path for download")
        path = input("")

        if "/" in path and "youtube" in link:
            # The video will be downloaded
            yt = YouTube(link)
            for n, i in enumerate(yt.streams.filter(progressive=True).all(), start=1):
                print(f"{str(n)}. {str(i)}")
                streams[str(n)] = i
            while True:
                print("Choose of the options")
                option = input("")
                if option in list(streams.keys()):
                    streams.get(option).download(path)
                else:
                    print("Invalid")
        if "/" not in path:
            # The path is invalid
            print("The path is invalid")
            continue
        if "youtube" not in link:
            # The link is invalid
            print("The link is invalid")
            continue


video_downloader()
