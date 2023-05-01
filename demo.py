# importing vlc module
import vlc
import time

# importing pafy module - As of the time of this commit, this fork is needed due to latest YT API changes: https://github.com/elig0n/pafy
import pafy


# url of the video
url = "https://www.youtube.com/watch?v=DJ_wEoW8Qcg"

# creating pafy object of the video
video = pafy.new(url)

# getting best stream
best = video.getbest()

# creating vlc media player object
media = vlc.MediaPlayer(best.url)

# start playing video
media.play()

playing = set([1,2,3,4])
play = True
while play:
    time.sleep(0.5)
    state = media.get_state()
    if state in playing:
        continue
    else:
        play = False

