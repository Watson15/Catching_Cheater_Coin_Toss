import pygame
from dumbmenu import *
pygame.init()

# Just a few static variables
red   = 255,  0,  0
green =   0,255,  0
blue  =   0,  0,255

size = width, height = 340,240	
screen = pygame.display.set_mode(size)
screen.fill(blue)
pygame.display.update()
pygame.key.set_repeat(500,30)

print dumbmenu(screen, [
                        'Start Game',
                        'Options',
                        'Manual',
                        'Show Highscore',
                        'Quit Game'], 64,64,32,1.4,green,blue,red)
pygame.quit()
