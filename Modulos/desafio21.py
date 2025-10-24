import pygame
import time

pygame.init()
pygame.mixer.music.load("audio.mp3")
pygame.mixer.music.play()

# Espera até a música terminar
while pygame.mixer.music.get_busy():
    time.sleep(1)