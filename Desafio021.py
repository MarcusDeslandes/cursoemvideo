import pygame
pygame.init()
pygame.mixer.music.load('jankenpo.mp3')
pygame.mixer.music.play()
pygame.event.wait()
pygame.time.delay(5000)
