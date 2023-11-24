# '''
# Create music player with keyboard controller. You have to be able to press keyboard: play, 
# stop, next and previous as some keys. Player has to react to the given command appropriately.
# '''

import pygame
import os

pygame.init()

def load_current_song(music_directory, current_song):
    pygame.mixer.music.load(os.path.join(music_directory, music_files[current_song]))

def play_music():
    pygame.mixer.music.play()
    # return True

def continue_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()


def next_song(current_song):
    return (current_song + 1) % len(music_files)

def previous_song(current_song):
    return (current_song - 1) % len(music_files)

pygame.display.set_caption("Simple Music Player")
screen = pygame.display.set_mode((300, 200))

music_directory = "C:/Users/kozha/OneDrive/Рабочий стол/Lab9"

music_files = [f for f in os.listdir(music_directory) if f.endswith(".mp3")]

pygame.mixer.init()

current_song = 0
load_current_song(music_directory, current_song)
playing = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    stop_music()
                    playing = False
                else:
                    play_music()
                    playing = True
            elif event.key == pygame.K_RIGHT:
                current_song = next_song(current_song)
                load_current_song(music_directory, current_song)
                if playing:
                    play_music()
            elif event.key == pygame.K_LEFT:
                current_song = previous_song(current_song)
                load_current_song(music_directory, current_song)
                if playing:
                    play_music()

    pygame.display.flip()

pygame.quit()