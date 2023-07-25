# Coin Flip
# Version: 1.0
# (c) 2010
# By Gio Di Russo
# "Dumbmenu" Library + Module by Astorek and found via Pygame.org

import sys, os, random
import pygame
import pygame.locals
import dumbmenu
from random import randrange
import moviepy
import moviepy.editor
import moviepy.video.fx.all as vfx

def rand50():
        return ((int)(randrange(0, 2)) & 1)
    
def rand75():
    return (rand50() & rand50())^1

class Quarter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.quarter_image_head = pygame.image.load('Quarter Heads.jpg').convert()
        self.quarter_image_tail = pygame.image.load('Quarter Tails.jpg').convert()
        self.image = self.quarter_image_head
        self.rect = self.image.get_rect()
        self.heads = 1
        self.count_heads = 0
        self.count_tails = 0
    
    def update(self):
        if self.heads == 1:
            self.image = self.quarter_image_head
        else:
            self.image = self.quarter_image_tail
    
    def flip_coin(self):
        print("You flip the Quarter")
        self.heads = rand75()
        
        if self.heads == 1:
            self.count_heads+=1
        else:
            self.count_tails+=1
        print(f"Heads flipped: {self.count_heads} and Tails flipped: {self.count_tails} Total flips: {self.count_tails + self.count_heads}")
    
    def move(self, x, y):
        self.rect = pygame.Rect(x, y, self.rect[2], self.rect[3])

class Copper_Penny(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.CP_image_head = pygame.image.load('Copper Penny Heads.jpg').convert()
        self.CP_image_tail = pygame.image.load('Copper Penny Tails.jpg').convert()
        self.image = self.CP_image_head
        self.rect = self.image.get_rect()
        self.heads = 1
        self.count_heads = 0
        self.count_tails = 0
    
    def update(self):
        if self.heads == 1:
            self.image = self.CP_image_head
            pygame.display.set_caption('`you flipped heads!`')
        else:
            self.image = self.CP_image_tail
            pygame.display.set_caption('`you flipped tails!`')
    
    def flip_coin(self):
        print("You flip the Penny")
        self.heads = rand75()
        clip = moviepy.editor.VideoFileClip('spedup.mp4')
        #final = clip.set_fps(clip.fps * 10)
        #final = final.fx(vfx.speedx, 10)
        #final.write_videofile('spedup.mp4')
        clip = clip.resize(0.4)
        clip.preview()
        if self.heads == 1:
            self.count_heads+=1
        else:
            self.count_tails+=1
        print(f"Heads flipped: {self.count_heads} and Tails flipped: {self.count_tails} Total flips: {self.count_tails + self.count_heads}")
    
    
    def move(self, x, y):
        self.rect = pygame.Rect(x, y, self.rect[2], self.rect[3])

def Qmain():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Coin Flip')
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    font = pygame.font.Font(None, 36)
    text = font.render("Click to flip the coin!!!", 1, (10, 10, 10))
    textpos = text.get_rect(centerx=background.get_width()/2)
    background.blit(text, textpos)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    qQuarter = Quarter()
    x = 250 - (qQuarter.rect[2]/2)
    y = 250 - (qQuarter.rect[3]/2)
    qQuarter.move(x, y)
    allsprites = pygame.sprite.RenderPlain((qQuarter))
    clock = pygame.time.Clock()
    while 1:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                qQuarter.flip_coin()
        allsprites.update()
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()

def CPmain():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Coin Flip')
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    font = pygame.font.Font(None, 36)
    text = font.render("Click to flip the coin!!!", 1, (10, 10, 10))
    textpos = text.get_rect(centerx=background.get_width()/2)
    background.blit(text, textpos)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    CP = Copper_Penny()
    x = 250 - (CP.rect[2]/2)
    y = 250 - (CP.rect[3]/2)
    CP.move(x, y)
    allsprites = pygame.sprite.RenderPlain((CP))
    clock = pygame.time.Clock()
    while 1:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                CP.flip_coin()
        allsprites.update()
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()

def menu1():
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.update()
    '''a = dumbmenu(screen, [
        'Quarter',
        'Copper Penny'], 100, 100, 70, 1.4, (255, 255, 255), (0, 0, 0), (255, 0, 0), False)
        '''
    a=1
    if a == 0:
        Qmain()
    elif a == 1:
        CPmain()


menu1()
