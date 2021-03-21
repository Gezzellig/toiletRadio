import vlc

url = 'http://prem1.rockradio.com:80/bluesrock?9555ae7caa92404c73cade1d'
p = vlc.MediaPlayer(url)
p.play()