import magneturi

def torrent_to_magnet(torrent_file_path):
    magnet_link = magneturi.from_torrent_file(torrent_file_path)
    return magnet_link

magnet_link = torrent_to_magnet('image.torrent')

print("Magnet Link:", magnet_link)
