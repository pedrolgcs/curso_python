import pygame

pygame.init()
pygame.mixer.music.load('./008.mp3')
pygame.mixer.music.play()
pygame.event.wait()