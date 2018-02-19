import pygame
import sys
import random
import time
import combine
import About_us
import Intro
import user_input
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

def button(text,x,y,width,height,inactive_color,active_color,action = None):
    global flag
    global temp_time
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > cur[0] > x and y+height > cur[1] > y:
        pygame.draw.rect(screen,active_color,(x,y,width,height))
        if click[0]==1 and action != None:           
            if action == "Intro":               
                Intro.intro()                
            if action == "Palindrome":
            	# combine.fun()
                user_input.get_input()
                # print(user_input.inputStr)           	
            if action == "About us":
            	About_us.about_us()      

    else:
        pygame.draw.rect(screen,inactive_color,(x,y,width,height))
    text_to_button(text,BLACK,x,y,width,height)
    
def text_to_button(msg,color,buttonx,buttony,buttonwidth,buttonheight,size = "small"):
    textSurf,textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)),buttony+(buttonheight/2))
    screen.blit(textSurf,textRect)

def text_objects(text,color,size):
    if size=="small":
        textSurface=smallfont.render(text,True,color)

    if size=="medium":
        textSurface=medfont.render(text,True,color)

    if size=="large":
        textSurface=largefont.render(text,True,color)
    return  textSurface,textSurface.get_rect()


while True :  
    screen.fill(BG_COLOR)
    button("Intro",350,100,250,40,LIGHT_GREEN,GREEN,"Intro")
    button("Palindrome Detection",350,180,250,40,LIGHT_GREEN,GREEN,"Palindrome")
    button("About us",350,260,250,40,LIGHT_GREEN,GREEN,"About us")   
    pygame.display.update()    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()   
        if event.type == pygame.KEYDOWN:
        	if event.key == pygame.K_c:        		
        		combine.fun()
