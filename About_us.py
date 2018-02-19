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
ravindra_img = pygame.image.load("ravindra.png")
shrey_img = pygame.image.load("shrey.png")
krc_img = pygame.image.load("krc.png")
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

def about_us():
    while True :  
        screen.fill(BG_COLOR)  

        screen.blit(ravindra_img,(50,150))
        message_to_screen("RAVINDRA SAINI",BLUE,130,350,"small")
        message_to_screen("ug201310028@iitj.ac.in",BLACK,140,370)

        screen.blit(shrey_img,(380,150))
        message_to_screen("SHREY MAHESHWARI",BLUE,450,350,"small")
        message_to_screen("ug201314017@iitj.ac.in",BLACK,450,370)

        screen.blit(krc_img,(700,150))
        message_to_screen("Dr. KR CHOUDHARY",BLUE,770,350,"small")
        message_to_screen("www.krchoudhary.com",BLACK,770,370)
        message_to_screen("(Mentor)",BLACK,770,390)

        pygame.display.update()    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:             
                    combine.fun()

if __name__ == "__main__":
    about_us()
