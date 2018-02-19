import pygame
import sys
import random
import time
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
clock = pygame.time.Clock()


active_state = None
next_active_state = None
previous_active_state = "q0"
active_arrow = None
temp_time = time.time()
global_input_string=""
# loop = pygame.image.load("Capture.png")
temp_input_string = ""
# temp = user_input.tempStr
class Palindrome:
    # global temp_input_string
    def __init__(self):
        self.set_input_string()  
        self.next_active_arrow()      
    tap = None
    tap_length = None
    current_tap_position = 0
    input_string = ""
    input_length = None
    state = None
    def get_input_string(self):
        return self.input_string
    def set_input_string(self):
        # global user_input.inputStr
        global current_tap_position 
        global temp_input_string       
        # self.input_string = "00000"
        # self.input_string = user_input.inputStr
        # print(self.input_string)
        # self.input_string = temp_input_string
        # self.input_string = temp_input_string
        # self.input_string = user_input.inputStr
        self.input_length = len(self.input_string)
        self.temp = int((23-int(self.input_length))/2)
        self.tap = []
        self.temp2 = 0
        while self.temp2 < self.temp:
            self.tap.append("#")
            self.temp2 +=1
        i=0
        while i< len(self.input_string):
            self.tap.append(self.input_string[i])
            i+=1
        self.temp2 +=self.input_length
        while self.temp2 < 23:
            self.tap.append("#")
            self.temp2 +=1               
        self.tap_length = 23#len(self.input_string)+2
        self.current_tap_position = self.temp        
        # print(self.tap)
        # self.next_active_arrow()
    def set_current_tap_position(self):
        self.current_tap_position = 1        
    state = "q0"    
    active_state = "q0"
    next_active_state = None
    def next_state(self):
        global active_arrow    
        if self.state == "q7" or self.state == "q8": # for stoping on halting
            active_arrow = None
            return 
        if self.state == "q0":            
            if self.tap[self.current_tap_position] == "1":
                self.tap[self.current_tap_position] = "#"
                self.current_tap_position+=1
                self.state = "q1"
            elif self.tap[self.current_tap_position] == "0":
                self.tap[self.current_tap_position] = "#"
                self.current_tap_position+=1
                self.state = "q4"
            else:
                self.state = "q7"
        elif self.state == "q1":
            if self.tap[self.current_tap_position] == "0":
                self.tap[self.current_tap_position] = "0"
                self.current_tap_position+=1
                self.state = "q1"
            elif self.tap[self.current_tap_position] == "1":
                self.tap[self.current_tap_position] = "1"
                self.current_tap_position+=1
                self.state = "q1"
            else:
                self.tap[self.current_tap_position] = "#"
                self.current_tap_position-=1
                self.state = "q2"
        elif self.state == "q2":
            if self.tap[self.current_tap_position] == "0":
                self.tap[self.current_tap_position] = "0"
                self.state = "q8"
            elif self.tap[self.current_tap_position] == "#":
                self.tap[self.current_tap_position] = "#"
                self.state = "q7"
            else:
                self.tap[self.current_tap_position] = "#"
                self.current_tap_position-=1
                self.state = "q3"
        elif self.state == "q3":
            if self.tap[self.current_tap_position] == "0":
                self.tap[self.current_tap_position] = "0"
                self.current_tap_position-=1
                self.state = "q3"
            elif self.tap[self.current_tap_position] == "1":
                self.tap[self.current_tap_position] = "1"
                self.current_tap_position-=1
                self.state = "q3"
            else:
                self.tap[self.current_tap_position] = "#"
                self.current_tap_position+=1
                self.state = "q0"
        elif self.state == "q4":
            if self.tap[self.current_tap_position] == "0":
                self.tap[self.current_tap_position] = "0"
                self.current_tap_position+=1
                self.state = "q4"
            elif self.tap[self.current_tap_position] == "1":
                self.tap[self.current_tap_position] = "1"
                self.current_tap_position+=1
                self.state = "q4"
            else:
                self.tap[self.current_tap_position] = "#"
                self.current_tap_position-=1
                self.state = "q5"
        elif self.state == "q5":
            if self.tap[self.current_tap_position] == "0":
                self.tap[self.current_tap_position] = "#"
                self.current_tap_position-=1
                self.state = "q6"
            elif self.tap[self.current_tap_position] == "1":
                self.tap[self.current_tap_position] = "1"
                self.state = "q8"
            else:
                self.tap[self.current_tap_position] = "#"
                self.state = "q7"
        elif self.state == "q6":
            if self.tap[self.current_tap_position] == "0":
                self.tap[self.current_tap_position] = "0"
                self.current_tap_position-=1
                self.state = "q6"
            elif self.tap[self.current_tap_position] == "1":
                self.tap[self.current_tap_position] = "1"
                self.current_tap_position-=1
                self.state = "q6"
            else:
                self.tap[self.current_tap_position] = "#"
                self.current_tap_position+=1
                self.state = "q0"
        # active_arrow = str(previous_active_state)+"_"+str(self.state) 


        # for determining next active arroww------------------------------------------------------
        # ------------------------------------------------------------------------------------------

    def next_active_arrow(self):
        # global previous_active_state 
        global active_arrow   
        # global flag   
        if self.state == "q7" or self.state == "q8": # for stoping on halting
            return 
        
        
        if self.state == "q0":            
            if self.tap[self.current_tap_position] == "1":                
                active_arrow = "q0_q1"

            elif self.tap[self.current_tap_position] == "0":                
                active_arrow = "q0_q4"
            else:
                # self.state = "q7"
                active_arrow = "q0_q7"
        elif self.state == "q1":
            if self.tap[self.current_tap_position] == "0":                
                active_arrow = "q1_q1"
            elif self.tap[self.current_tap_position] == "1":                
                active_arrow = "q1_q1"
            else:                
                active_arrow = "q1_q2"
        elif self.state == "q2":
            if self.tap[self.current_tap_position] == "0":               
                active_arrow = "q2_q8"
            elif self.tap[self.current_tap_position] == "#":
                # self.tap[self.current_tap_position] = "#"
                # self.state = "q8"
                active_arrow = "q2_q7"
            else:                
                active_arrow = "q2_q3"
        elif self.state == "q3":
            if self.tap[self.current_tap_position] == "0":               
                active_arrow = "q3_q3"
            elif self.tap[self.current_tap_position] == "1":                
                active_arrow = "q3_q3"
            else:                
                active_arrow = "q3_q0"
        elif self.state == "q4":
            if self.tap[self.current_tap_position] == "0":                
                active_arrow = "q4_q4"
            elif self.tap[self.current_tap_position] == "1":                
                active_arrow = "q4_q4"
            else:                
                active_arrow = "q4_q5"
        elif self.state == "q5":
            if self.tap[self.current_tap_position] == "0":                
                active_arrow = "q5_q6"
            elif self.tap[self.current_tap_position] == "1":                
                active_arrow = "q5_q7"
            else:                
                active_arrow = "q5_q8"
        elif self.state == "q6":
            if self.tap[self.current_tap_position] == "0":                
                active_arrow = "q6_q6"
            elif self.tap[self.current_tap_position] == "1":                
                active_arrow = "q6_q6"
            else:                
                active_arrow = "q6_q0"
        # active_arrow = str(previous_active_state)+"_"+str(self.state)       
    # ________________________________________________________________________________________________
    # _______________________Next arrow ends here_________________________________________________________

obj = Palindrome()
# obj.input_string = "1001"
# flag =1
def button(text,x,y,width,height,inactive_color,active_color,action = None):
    global flag
    global temp_time
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > cur[0] > x and y+height > cur[1] > y:
        pygame.draw.rect(screen,active_color,(x,y,width,height))
        if click[0]==1 and action != None:            
            if action == "Next" and time.time() > temp_time+0.5 :                
                temp_time =time.time()
                # print("got a click")
                # obj.next_active_arrow()
                obj.next_state()                
                obj.next_active_arrow()
                # if obj.state == "q7" or obj.state == "q8":
                #     obj.next_active_arrow()
                flag = 0              

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

def message_to_screen(msg,color,x,y,size="small"):
    textSurf ,textRect = text_objects(msg,color,size)
    textRect.center=x,y
    screen.blit(textSurf,textRect)

def fun():
    global obj
    while True :

        time_passed = clock.tick(30)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()   
        screen.fill(BG_COLOR)

        pygame.draw.lines(screen,BLACK,False,[(0,500),(900,500)],LINE_WIDTH)
        pygame.draw.lines(screen,BLACK,False,[(0,550),(900,550)],LINE_WIDTH)
        pygame.draw.lines(screen,BLACK,False,[(0,590),(900,590)],LINE_WIDTH)
        i=-15
        while i<900:
            pygame.draw.lines(screen,BLACK,False,[(i,550),(i,590)],LINE_WIDTH)
            i+=40


        if obj.state=="q7":
            pygame.draw.circle(screen,BLUE,(720,250),RADIUS)
            obj.active_arrow = ""
            message_to_screen("halt state",RED,100,20)
            message_to_screen("accepted",RED,100,40)
        else:
            pygame.draw.circle(screen,YELLOW,(720,250),RADIUS)
        message_to_screen("q7",RED,720,250)

        if obj.state == "q8":
            pygame.draw.circle(screen,BLUE,(860,250),RADIUS)
            obj.active_arrow = ""
            message_to_screen("halt state",RED,100,20)
            message_to_screen("rejected",RED,100,40)
        else:
            pygame.draw.circle(screen,YELLOW,(860,250),RADIUS)
        message_to_screen("q8",RED,860,250)

        # adding loop for q1
        if active_arrow == "q1_q1":
            pygame.draw.circle(screen,BLUE,(360,80),RADIUS+5,LINE_WIDTH)
            if obj.tap[obj.current_tap_position] == "1":
                message_to_screen("1|1,R",BLUE,330,120)
            else:
                message_to_screen("1|1,R",BLACK,330,120)
            if obj.tap[obj.current_tap_position] == "0":
                message_to_screen("0|0,R",BLUE,420,100)
            else:
                message_to_screen("0|0,R",BLACK,420,100)
        else:
            pygame.draw.circle(screen,BLACK,(360,80),RADIUS+5,LINE_WIDTH)
            message_to_screen("0|0,R",BLACK,420,100)
            message_to_screen("1|1,R",BLACK,330,120)
        
        #adding loop for q4
        if active_arrow == "q4_q4":
            pygame.draw.circle(screen,BLUE,(360,425),RADIUS+5,LINE_WIDTH)
            if obj.tap[obj.current_tap_position] == "1":
                message_to_screen("1|1,R",BLUE,360,380)
            else:
                message_to_screen("1|1,R",BLACK,360,380)
            if obj.tap[obj.current_tap_position] == "0":
                message_to_screen("0|0,R",BLUE,360,360)
            else:
                message_to_screen("0|0,R",BLACK,360,360)
        else:
            pygame.draw.circle(screen,BLACK,(360,425),RADIUS+5,LINE_WIDTH)
            message_to_screen("0|0,R",BLACK,360,360)
            message_to_screen("1|1,R",BLACK,360,380)



        #adding loop for q3
        if active_arrow == "q3_q3":
            pygame.draw.circle(screen,BLUE,(540+25,150+25),RADIUS+5,LINE_WIDTH)
            if obj.tap[obj.current_tap_position] == "1":
                message_to_screen("1|1,L",BLUE,540+80,150)
            else:
                message_to_screen("1|1,L",BLACK,540+80,150)

            if obj.tap[obj.current_tap_position] == "0":
                message_to_screen("0|0,L",BLUE,540+90,180)
            else:
                message_to_screen("0|0,L",BLACK,540+90,180)
        else:
            pygame.draw.circle(screen,BLACK,(540+25,150+25),RADIUS+5,LINE_WIDTH)
            message_to_screen("0|0,L",BLACK,540+90,180)
            message_to_screen("1|1,L",BLACK,540+80,150)        

        #adding loop for q6
        if active_arrow == "q6_q6":
            pygame.draw.circle(screen,BLUE,(540+25,350-25),RADIUS+5,LINE_WIDTH)
            if obj.tap[obj.current_tap_position] == "1":
                message_to_screen("1|1,L",BLUE,540+80,350-60)
            else:
                message_to_screen("1|1,L",BLACK,540+80,350-60)

            if obj.tap[obj.current_tap_position] == "0":
                message_to_screen("0|0,L",BLUE,540+90,350-25)
            else:
                message_to_screen("0|0,L",BLACK,540+90,350-25)
        else:
            pygame.draw.circle(screen,BLACK,(540+25,350-25),RADIUS+5,LINE_WIDTH)
            message_to_screen("0|0,L",BLACK,540+90,350-25)
            message_to_screen("1|1,L",BLACK,540+80,350-60)     
        if obj.state == "q0":
            pygame.draw.circle(screen,BLUE,(180,250),RADIUS)#q0
        else:
            pygame.draw.circle(screen,YELLOW,(180,250),RADIUS)#q0
        message_to_screen("q0",RED,180,250)

        # if obj.state=="q7":
        #     pygame.draw.circle(screen,BLUE,(540,250),RADIUS)
        #     obj.active_arrow = ""
        # else:
        #     pygame.draw.circle(screen,YELLOW,(540,250),RADIUS)
        # message_to_screen("q7",RED,540,250)

        # if obj.state == "q8":
        #     pygame.draw.circle(screen,BLUE,(720,250),RADIUS)
        #     obj.active_arrow = ""
        # else:
        #     pygame.draw.circle(screen,YELLOW,(720,250),RADIUS)
        # message_to_screen("q8",RED,720,250)
        if obj.state == "q1":
            pygame.draw.circle(screen,BLUE,(360,50),RADIUS)
        else:
            pygame.draw.circle(screen,YELLOW,(360,50),RADIUS)
        message_to_screen("q1",RED,360,50)
        if obj.state=="q4":
            pygame.draw.circle(screen,BLUE,(360,450),RADIUS)
        else:
            pygame.draw.circle(screen,YELLOW,(360,450),RADIUS)
        message_to_screen("q4",RED,360,450)
        if obj.state == "q3":
            pygame.draw.circle(screen,BLUE,(540,150),RADIUS)
        else:
            pygame.draw.circle(screen,YELLOW,(540,150),RADIUS)
        message_to_screen("q3",RED,540,150)
        if obj.state == "q6":
            pygame.draw.circle(screen,BLUE,(540,350),RADIUS)
        else:
            pygame.draw.circle(screen,YELLOW,(540,350),RADIUS)
        message_to_screen("q6",RED,540,350)
        if obj.state=="q2":
            pygame.draw.circle(screen,BLUE,(540,50),RADIUS)
        else:
            pygame.draw.circle(screen,YELLOW,(540,50),RADIUS)
        message_to_screen("q2",RED,540,50)
        if obj.state == "q5":
            pygame.draw.circle(screen,BLUE,(540,450),RADIUS)
        else:
            pygame.draw.circle(screen,YELLOW,(540,450),RADIUS)
        message_to_screen("q5",RED,540,450)

        if active_arrow == "q0_q1":
            pygame.draw.lines(screen,ACTIVE_EDGE_COLOR,False,[(180+25,250),(360-25,50)],LINE_WIDTH) #q0 to q1
            message_to_screen("1|B,R",BLUE,220,150)
        else:
            pygame.draw.lines(screen,BLACK,False,[(180+25,250),(360-25,50)],LINE_WIDTH) #q0 to q1
            message_to_screen("1|B,R",BLACK,220,150)

        if active_arrow == "q0_q4":
            pygame.draw.lines(screen,ACTIVE_EDGE_COLOR,False,[(180+25,250),(360-25,450)],LINE_WIDTH) #q0 to q4
            message_to_screen("0|B,R",BLUE,220,350)            
        else:
            pygame.draw.lines(screen,BLACK,False,[(180+25,250),(360-25,450)],LINE_WIDTH) #q0 to q4
            message_to_screen("0|B,R",BLACK,220,350)
        if active_arrow == "q1_q2":
            pygame.draw.lines(screen,ACTIVE_EDGE_COLOR,False,[(360+25,50),(540-25,50)],LINE_WIDTH)#q1 to q2
            message_to_screen("B|B,L",BLUE,450,25)
        else:
            pygame.draw.lines(screen,BLACK,False,[(360+25,50),(540-25,50)],LINE_WIDTH)#q1 to q2
            message_to_screen("B|B,L",BLACK,450,25)

        if active_arrow=="q4_q5":
            pygame.draw.lines(screen,ACTIVE_EDGE_COLOR,False,[(360+25,450),(540-25,450)],LINE_WIDTH)#q4 to q5
            message_to_screen("B|B,L",BLUE,450,450-20)      

        else:
            pygame.draw.lines(screen,BLACK,False,[(360+25,450),(540-25,450)],LINE_WIDTH)#q4 to q5
            message_to_screen("B|B,L",BLACK,450,450-20)             

        if active_arrow == "q2_q3":
            pygame.draw.lines(screen,ACTIVE_EDGE_COLOR,False,[(540,50+25),(540,150-25)],LINE_WIDTH)#q2 to q3
            message_to_screen("1|B,L",BLUE,540+35,100) 
        else:
            pygame.draw.lines(screen,BLACK,False,[(540,50+25),(540,150-25)],LINE_WIDTH)#q2 to q3
            message_to_screen("1|B,L",BLACK,540+35,100)
        if active_arrow == "q5_q6":
            pygame.draw.lines(screen,ACTIVE_EDGE_COLOR,False,[(540,450-25),(540,450-100+25)],LINE_WIDTH)#q5 to q6
            message_to_screen("0|B,L",BLUE,540+35,400)             
        else:
            pygame.draw.lines(screen,BLACK,False,[(540,450-25),(540,450-100+25)],LINE_WIDTH)#q5 to q6
            message_to_screen("0|B,L",BLACK,540+35,400) 
        if active_arrow == "q3_q0":
            pygame.draw.lines(screen,ACTIVE_EDGE_COLOR,False,[(540-25,150),(180+25,250)],LINE_WIDTH)#q3 to q0
            message_to_screen("B|B,R",BLUE,450,150)
        else:
            pygame.draw.lines(screen,BLACK,False,[(540-25,150),(180+25,250)],LINE_WIDTH)#q3 to q0
            message_to_screen("B|B,R",BLACK,450,150)
        if active_arrow == "q6_q0":
            pygame.draw.lines(screen,ACTIVE_EDGE_COLOR,False,[(540-25,350),(180+25,250)],LINE_WIDTH)#q6 to q0
            message_to_screen("B|B,R",BLACK,450,350)            
        else:
            pygame.draw.lines(screen,BLACK,False,[(540-25,350),(180+25,250)],LINE_WIDTH)#q6 to q0
            message_to_screen("B|B,R",BLACK,450,350)
        if active_arrow == "q0_q7" and obj.state != "q7":
            pygame.draw.lines(screen,ACTIVE_EDGE_COLOR,False,[(180+25,250),(720-25,250)],LINE_WIDTH)#q0 to accept
            message_to_screen("B|B,S",BLUE,450,250-25)
        else:
            pygame.draw.lines(screen,BLACK,False,[(180+25,250),(720-25,250)],LINE_WIDTH)#q0 to accept
            message_to_screen("B|B,S",BLACK,450,250-25)

        if active_arrow == "q2_q8" and obj.state != "q8":
            pygame.draw.lines(screen,ACTIVE_EDGE_COLOR,False,[(540+25,50),(860,250-25)],LINE_WIDTH)#q2 to reject
            
            # message_to_screen("B|B,S",BLUE,640+25,100)            
            # message_to_screen("something",BLUE,640+25,120)
            # if obj.tap[obj.current_tap_position] == "B" and obj.state != "q8":
            #     message_to_screen("B|B,S",BLUE,700+50,100)
            #     # pass
            # else:
            #     message_to_screen("B|B,S",BLACK,700+50,100)

            if obj.tap[obj.current_tap_position] == "0" and obj.state != "q8":
                message_to_screen("0|0,S",BLUE,700+50,100)
            else:
                message_to_screen("0|0,S",BLACK,700+50,100)

        else:
            pygame.draw.lines(screen,BLACK,False,[(540+25,50),(860,250-25)],LINE_WIDTH)#q2 to reject
            # message_to_screen("B|B,S",BLACK,700+25,100)
            message_to_screen("0|0,S",BLACK,700+25,120)

        if active_arrow == "q2_q7":
            pygame.draw.lines(screen,ACTIVE_EDGE_COLOR,False,[(540+25,50),(720,250-25)],LINE_WIDTH)#q2 to reject
            if obj.tap[obj.current_tap_position] == "B":
                message_to_screen("B|B,S",BLUE,700+25,180)                
            else:
                message_to_screen("B|B,S",BLUE,700+25,180)    

        else:
            pygame.draw.lines(screen,BLACK,False,[(540+25,50),(720,250-25)],LINE_WIDTH)#q2 to reject
            message_to_screen("B|B,S",BLACK,700+25,180)            

        if active_arrow == "q5_q8":
            pygame.draw.lines(screen,ACTIVE_EDGE_COLOR,False,[(540+25,450),(720,250+25)],LINE_WIDTH)#q5 to reject
            

            if obj.tap[obj.current_tap_position] == "1" and obj.state != "q8":
                message_to_screen("1|1,S",BLUE,740+50,350)
            else:
                message_to_screen("1|1,S",BLACK,740+50,350)
        else:
            pygame.draw.lines(screen,BLACK,False,[(540+25,450),(720,250+25)],LINE_WIDTH)#q5 to reject
            # message_to_screen("B|B,S",BLACK,640+50,350)
            message_to_screen("1|1,S",BLACK,740+50,350)

        if active_arrow == "q5_q7":
            pygame.draw.lines(screen,ACTIVE_EDGE_COLOR,False,[(540+25,450),(860,250+25)],LINE_WIDTH)#q5 to reject
            if obj.tap[obj.current_tap_position] == "B":
                message_to_screen("B|B,S",BLUE,700,350)                   
        else:
            pygame.draw.lines(screen,BLACK,False,[(540+25,450),(860,250+25)],LINE_WIDTH)#q5 to reject
            message_to_screen("B|B,S",BLACK,700,350)
            

        button("Next",20,450,100,40,LIGHT_GREEN,GREEN,"Next")
        index = 0
        xcord = 0
        while index <23:
            pygame.draw.rect(screen,ACTIVE_EDGE_COLOR,(-15+obj.current_tap_position*40,550,40,40),LINE_WIDTH)            
            message_to_screen(obj.tap[index],RED,xcord,570)
            index+=1
            xcord+=40
        # global loop
        # screen.blit(loop,(10,10))
        pygame.display.update()

if __name__ == "__main__":
    fun()
