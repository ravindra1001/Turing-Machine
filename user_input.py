import pygame
import sys
import random
import time
import combine

pygame.init()
clock = pygame.time.Clock()

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
    textRect.topleft=x,y
    screen.blit(textSurf,textRect)
inputStr = ""

def get_input():
    global inputStr
    inputStr = ""
    while True :  
        time_passed = clock.tick(30)
        screen.fill(BG_COLOR)
        
        message_to_screen("INPUT STRING::",GREEN,100,300,"medium")
        message_to_screen(inputStr +"|",BLACK,550,300,"medium")         

        pygame.display.update()    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            if event.type == pygame.KEYDOWN:                
                if event.key == pygame.K_0:
                    inputStr += "0"
                if event.key == pygame.K_1:
                    inputStr += "1"
                if event.key == pygame.K_2:
                    inputStr += "2"
                if event.key == pygame.K_3:
                    inputStr += "3"
                if event.key == pygame.K_4:
                    inputStr += "4"
                if event.key == pygame.K_5:
                    inputStr += "5"
                if event.key == pygame.K_6:
                    inputStr += "6"
                if event.key == pygame.K_7:
                    inputStr += "7"
                if event.key == pygame.K_8:
                    inputStr += "8" 
                if event.key == pygame.K_9:
                    inputStr += "9"                  
                if event.key == pygame.K_BACKSPACE:
                    inputStr = inputStr[:-1]
                if event.key == pygame.K_RETURN:
                    # combine.obj.input_string = inputStr
                    # combine.temp_input_string = inputStr
                    combine.obj.input_string  = inputStr
                    # print(combine.obj.input_string)
                    combine.obj.set_input_string()
                    combine.obj.next_active_arrow()
                    # combine.obj.input_string ="10000000"
                    # print(combine.obj.input_string)
                    combine.fun()                   
                if event.key == pygame.K_BACKSPACE:
                    inputStr = inputStr[:-1]                         

if __name__ == "__main__":
    get_input()
    # print(inputStr)
