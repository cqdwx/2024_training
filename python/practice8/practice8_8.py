def make_album(artist, album_title, tracks=None):
    album = {'artist': artist, 'album_title': album_title}
    if tracks:
        album['tracks'] = tracks
    return album

while True:
    artist = input("请输入歌手名（输入'q'退出）: ")
    if artist == 'q':
        break
    album = input("请输入专辑名（输入'q'退出）: ")
    if album == 'q':
        break
    print(make_album(artist, album))
