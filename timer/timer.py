import time
import pygame  # You may need to install this library: pip install pygame

def play_song(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play() 
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()
    pygame.quit() 


def notify_every(interval, sounds):
    i = 0
    while True:
        if(i % 6 == 0 ):
            play_song(sounds[0])

            play_song(sounds[0])
            play_song(sounds[0])
            print("An Hour has gone by ")
        elif (i % 3 == 0 ): 
            play_song(sounds[0])
            play_song(sounds[0])
            print("Half has gone by ")
        else :
            play_song(sounds[0])
            print("10 minutes has gone by ")
        i += 1; 
            
        time.sleep(interval * 60)  # Convert minutes to seconds

if __name__ == "__main__":
    interval = 10  # Set the interval in minutes
    wow= "./wow.mp3"  # Replace this with the path to your audio file
    boom = "./boom.mp3"
    bruh = "./bruh.mp3"
    notify_every(interval, [boom,bruh,wow])
