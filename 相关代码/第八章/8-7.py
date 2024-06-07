def make_album(artist, title):
    """创建一个包含专辑信息的字典。"""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    return album_dict

album = make_album('metallica', 'ride the lightning')
print(album)
album = make_album('beethoven', 'ninth symphony')
print(album)
album = make_album('willie nelson', 'red-headed stranger')
print(album)


def make_album(artist, title, tracks=0):
    """创建一个包含专辑信息的字典。"""
    album_dict = { 'artist': artist.title(), 'title': title.title(), }
    if tracks: album_dict['tracks'] = tracks
    return album_dict
album = make_album('metallica', 'ride the lightning')
print(album)
album = make_album('beethoven', 'ninth symphony')
print(album)
album = make_album('willie nelson', 'red-headed stranger')
print(album)
album = make_album('iron maiden', 'piece of mind', tracks=8)
print(album)