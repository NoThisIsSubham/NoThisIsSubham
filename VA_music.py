from pygame import mixer

playing = False
paused = False

def play_it(file):
    global playing
    
    stop_it()
    mixer.init()
    if not playing:
        mixer.music.load(file)
        mixer.music.play()
        playing = True


def pause_n_unpause():
    global playing, paused

    if playing:
        mixer.music.pause()
        playing = False
        paused = True

    elif paused:
        mixer.music.unpause()       
        playing = True
        paused = False


def stop_it():
    global playing, paused

    if playing:
        mixer.music.fadeout(600)
        playing = False
        
    elif paused:
        mixer.music.stop()       
        paused = False
