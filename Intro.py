import pygame
import sys
import random
import time
import combine

pygame.init()

SCREEN_WIDTH=900
SCREEN_HEIGHT=650
BG_COLOR = (200,200,200)
RED = (100,0,0)
PINK = (255,0,255)
YELLOW = (255,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
GREEN = (0,200,0)
LIGHT_GREEN = (0,255,0)

RADIUS =25
LINE_WIDTH = 5
ACTIVE_EDGE_COLOR = BLUE

smallfont = pygame.font.SysFont("comicsansms" ,25)
medfont = pygame.font.SysFont("comicsansms" ,50)
largefont = pygame.font.SysFont("comicsansms" ,80)
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),0,32)
pygame.display.set_caption("TOC PROJECT  [Turing machine]")
def text_objects(text,color,size):
    if size=="small":
        textSurface=smallfont.render(text,True,color)

    if size=="medium":
        textSurface=medfont.render(text,True,color)

    if size=="large":
        textSurface=largefont.render(text,True,color)
    return  textSurface,textSurface.get_rect()

def message_to_screen(msg,color,x,y,size="small"):
    textSurf ,textRect = text_objects(msg,color,size)
    textRect.center=x,y
    screen.blit(textSurf,textRect)

def intro():
    while True :  
        screen.fill(BG_COLOR)  
        message_to_screen("This is a semester project of \"theory of computation course\"",BLUE,450,100,"small")
        message_to_screen("It  simulates visual of turing machine that ditect ",BLUE,450,125,"small")
        message_to_screen("whether a string is palindrome or not ",BLUE,450,150,"small")

        message_to_screen("Here input should be a binary string of 0 and 1",BLUE,450,180,"small")
        pygame.display.update()    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:             
                    combine.fun()

if __name__ == "__main__":
    intro()
