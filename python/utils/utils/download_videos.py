from pytube import YouTube

youtube = YouTube('https://www.youtube.com/watch?v=Ox_zb2cs9zM&ab_channel=Rocketseat')


stream = youtube.streams.get_by_itag(22)
stream.download(max_retries=10)

for i in youtube.streams.filter(file_extension='mp4'):
    print(i)