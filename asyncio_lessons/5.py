
async def download_file(url):
    print(f'load - {url}')


image_downloader = download_file('https://gg.com/image')
music_downloader = download_file('https://gg.com/music')


coroutines = [image_downloader, music_downloader]

if __name__ == '__main__':
    while True:
        for coroutine in coroutines.copy():
            try:
                coroutine.send(None)
            except StopIteration:
                coroutines.remove(coroutine)
        if len(coroutines) == 0:
            break
