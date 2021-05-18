from pygame import mixer
mixer.init()
mixer.music.load('main.mp3')
print('Programa FODA')
mixer.music.play()
while(mixer.music.get_busy()): pass
