import urllib, json, xbmc


def get_pl():
    url = 'http://live.huffingtonpost.com/api/startup.json'
    config = json.loads(urllib.urlopen(url).read())
    if config['data']['live_now']:
        pl = config['data']['sources']['live']['video/hls']
        status = 'live'
    else:
        pl = config['data']['sources']['live_again']['video/hls']
        status = 'again'

    list = urllib.urlopen(pl).read()
    for l in list.split():
        if l.find('1000.m3u8') > 1:
            return l, status

def main():
    player = xbmc.Player()
    playlist = xbmc.PlayList (xbmc.PLAYLIST_VIDEO)
    status = ''
    while True:
        pl, st = get_pl()

        if status != st:
            xbmc.log("huffpost %s playing %s" % (st, pl))
            playlist.add(pl)
            player.play(playlist)
            status = st

        xbmc.sleep(2000)

if __name__ == '__main__':
    main()
