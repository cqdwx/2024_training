def make_album(artist, album_title, tracks=None):
    album = {'artist': artist, 'album_title': album_title}
    if tracks:
        album['tracks'] = tracks
    return album

# 创建三个不同专辑的字典并打印返回的值
print(make_album('Michael Jackson', 'Thriller'))
print(make_album('The Beatles', 'Abbey Road', 17))
print(make_album('Pink Floyd', 'The Dark Side of the Moon', 10))
