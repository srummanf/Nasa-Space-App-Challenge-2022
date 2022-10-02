import copy
import sys
import kivy
from kivy.app import App
from kivy.core.audio import SoundLoader
import os
import pygame
import random
import math

from pygame_functions import *
from pygame import mixer

programIcon =pygame.image.load(os.path.join("Assets","spaceship_red.png"))

pygame.display.set_icon(programIcon)



pygame.init()

out, inp =0,0
input = []
output=[]
bulletImg=pygame.image.load(os.path.join("Assets","red-rocket.png"))
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=0.7
bullet_state="ready"
GG_font=pygame.font.Font('freesansbold.ttf',64)
score_value=0

playerImg=pygame.image.load(os.path.join("Assets","spaceship_yellow.png"))
playerX=370
playerY=480
playerX_change=0

enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]

    

score_state="unlocked"

width =88
height=600
screen=pygame.display.set_mode((width,height))

background =pygame.image.load(os.path.join("Assets","space-bg-1.png"))

# music=SoundLoader.load('background.wav')
# mixer.music.load('background.wav')
# mixer.music.play(-1)

pygame.display.set_caption("Save the Earth")

font = pygame.font.SysFont("comicsans",30)
smallfont = pygame.font.System("comicsans",14)
darkerblue=(0,128,255)
lightblue=(0,180,255)
white=(255,255,255)

num_of_enemies=4
def playagain_button(msg,x,y,width,height,hovercolor,defaultcolor,out,inp):
    mouse = pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed(3)
    if x+width > mouse[0] > x and y + height > mouse[1]>y:
        pygame.draw.rect(screen,hovercolor,(x,y,width,height))
        if click[0]==1:
            main_game(out,inp)

    else:
        pygame.draw.rect(screen,defaultcolor,(x,y,width,height))

    playagain_button_text=smallfont.render(msg,True,white)
    screen.blit(playagain_button_text,(316,396))

def startover_button(msg,x,y,width,height,hovercolor,defaultcolor):
    mouse = pygame.mouse.get_pos()
    
    click=pygame.mouse.get_pressed(3)
    if x+width>mouse[0]> x and y+ height>mouse[1]>y:
        pygame.draw.rect(screen,hovercolor,(x,y,width,height))
        if click[0]==1:
            start_menu()
    else:
        pygame.draw.rect(screen,defaultcolor,(x,y,width,height))
    startover_button_text=smallfont.render(msg,True,white)
    screen.blit(startover_button_text,(800 - 177,7))

def create_button(msg,x,y,width,height,hovercolor,defaultcolor): 
    mouse = pygame.mouse.get_pos()
    
    click=pygame.mouse.get_pressed(3)
    if x+width>mouse[0]> x and y+ height>mouse[1]>y:
        pygame.draw.rect(screen,hovercolor,(x,y,width,height))
        if click[0]==1:
            question_screen()    
    else:
        pygame.draw.rect(screen,hovercolor,(x,y,width,height))     

    start_button_text=smallfont.render(msg,True,white)
    screen.blit(start_button_text,(int(555+(width/2)),int(y+(y/2))))
    
def start_menu():

    startText= font.render("The Defenders of Earth", True, white)

    while True:

        screen.fill((0,0,0))

        screen.blit(background,(0,0))
        screen.blit(startText,((width-startText.get_width())/2,200))
        create_button("Click here to start!",width -180,7,175,26,lightblue,darkerblue)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update()

def new_button(msg,x,y,width,height,hovercolor,defaultcolor,out,inp):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed(3)
    if x+width > mouse[8]>x and y+height>mouse[1]>y:
        pygame.draw.rect(screen,hovercolor,(x,y,width,height))
        if click[0] ==1:
            main_game(out,inp)
        else:
            pygame.draw.rect(screen,defaultcolor,(x,y,width,height))
        start_button_text = smallfont.render(msg,True,white)
        screen.blit(start_button_text,(int(555+(width/2)),int(y+(y/2))))

def question_screen():

    global answerBox
    

    width=800
    height=600
    screen= pygame.display.set_mode((width,height))

    screen.fill((0,0,0))


    

    while True:

        screen.fill((0,0,0))

        screen.blit(background,(0,0))

        new_button("Click Here to Play!",width - 180,7,175,26,lightblue,darkerblue,output,input)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

def main_game(out,inp):
    width=1200
    height=600
    screen = pygame.display.set_mode((pygame.width,height))

    

    enemyImg.append(pygame.image.load(os.path.join("Assets","spaceship_red.png")))
    enemyImg.append(pygame.image.load(os.path.join("Assets","spaceship_red.png")))
    enemyImg.append(pygame.image.load(os.path.join("Assets","spaceship_red.png")))
    enemyImg.append(pygame.image.load(os.path.join("Assets","spaceship_red.png")))

    for i in range(num_of_enemies):
        enemyX.append(random.randint(0,735))
        enemyY.append(random.randint(20,100))
        enemyX_change.append(0.3)
        enemyY_change.append(30)

    font = pygame.font.SysFont("comicsans",30)
    smallfont = pygame.font.SysFont("comicsans",14)
    white=(255,255,255)

    
    font=pygame.font.Font('freesansbold.ttf',32)

    testX=10
    testY=10

    

def show_score (x,y):
    score = font.render("Score:"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over_screen():
    width=800
    height=600
    screen = pygame.display.set_mode((width,height))

    screen.fill((0,0,0))

    screen.blit(background,(0,0))

    while True:
        GG_text= GG_font.render(f"You got {score_value}/{len(out)}Correct",True,(255,255,255))
        screen.blit(GG_text,(100,250))

        for j in range (num_of_enemies):
            enemyY[j]=2000
        playagain_button("Click here to play again" ,300,390,200,30, lightblue, darkerblue, out, inp)
        startover_button("Click here to start over" ,800-180,7,170,26, lightblue, darkerblue)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()

        pygame.display.update()

def player(x,y):
    screen.blit(playerImg, (x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y)) 

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg, (x+16,y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance= math.sqrt((math.pow(enemyX- bulletX, 2)) + math.pow(enemyY- bulletY, 2))
    if distance<28:
        return True

    return False

letter_list = []
image_dict= {enemyImg[0]: 'A', enemyImg[1]: 'B', enemyImg[2]: 'C', enemyImg[3]: 'D'}

class Question:
    def __init__(self, prompt, answer, enemy,letter, other_answer1, other_answer2, other_answer3, other_letter1, other_letter2, other_letter3):

        self.prompt= prompt
        self.answer= answer
        self.enemy= enemy
        self.letter= letter 
        self.other_answer1= other_answer1
        self.other_answer2= other_answer2
        self.other_answer3= other_answer3
        self.other_letter1= other_letter1
        self.other_letter2= other_letter2
        self.other_letter3= other_letter3

    enemy_val= []

    for n in range(len(out)):
        enemy_val.append(enemyImg[random.randint(0,3)])
        letter_list.append(image_dict[enemy_val[n]])

    print(letter_list)

    o1_answer= []
    o2_answer= []
    o3_answer= []

    for n in range(len(out)):
        o1_answer.append(out[random.randint(0, (len(out)-1))])
        o2_answer.append(out[random.randint(0, (len(out)-1))])
        o3_answer.append(out[random.randint(0, (len(out)-1))])

        while o1_answer[n]== out[n]:
            del o1_answer[n]
            o1_answer.append(out[random.randint(0, (len(out)-1))])

        while o2_answer[n]== out[n] or o2_answer[n]== o1_answer[n]:
            del o2_answer[n]
            o2_answer.append(out[random.randint(0, (len(out)-1))])

        while o3_answer[n]== out[n] or o3_answer[n]== o2_answer[n] or o3_answer[n]== o1_answer[n]:
            del o3_answer[n]
            o3_answer.append(out[random.randint(0, (len(out)-1))])

    print(o1_answer)
    print(o2_answer)
    print(o3_answer)

    Letter_List= ['A', 'B', 'C', 'D']
    o1_letter= []
    o2_letter= []
    o3_letter= []

    for n in range(len(out)):
        o1_letter.append(Letter_List[random.randint(0,3)])
        o2_letter.append(Letter_List[random.randint(0,3)])
        o3_letter.append(Letter_List[random.randint(0,3)])

    o1_int= 0
    o2_int= 0
    o3_int= 0

    for o1 in o1_letter[:]:
        while o1_letter[o1_int]== letter_list[o1_int]:
            del o1_letter[o1_int]
            o1_letter.insert(o1_int, Letter_List[random.randint(0,3)])
        o1_int += 1

    for o2 in o2_letter[:]:
        while o2_letter[o2_int]== letter_list[o2_int] or o2_letter[o2_int]== o1_letter[o2_int]:
            del o2_letter[o1_int]
            o2_letter.insert(o2_int, Letter_List[random.randint(0,3)])
        o2_int += 1

    for o3 in o3_letter[:]:
        while o3_letter[o3_int]== letter_list[o3_int] or o3_letter[o3_int]== o2_letter[o3_int] or o3_letter[o3_int]== o1_letter[o3_int]:
            del o3_letter[o3_int]
            o3_letter.insert(o3_int, Letter_List[random.randint(0,3)])
        o3_int += 1

    questions= [] # WE WILL ADD ALL THE QUESTIONS
    answers = [] #  WE WILL SAVE THE ASNWER KEY OVER HERE
    for n in range(len(out)):
        questions.append(Question(inp[n], out[n], enemy_val[n], letter_list[n], o1_answer[n], o2_answer[n], o3_answer[n], o1_letter[n], o2_letter[n], o3_letter[n]))

    print(questions)

    int_index=1 
    index= questions[int_index]
    real_index=0
    Rindex= questions[real_index]
    let_index=1
    Lindex= questions[let_index]
    end_index=0

    QuestionText= font.render(f"{questions[0].prompt}:", True, white)
    AnswerText= smallfont.render(f"{questions[0].answer}", True, white)

    Other1Text= smallfont.render(f"{questions[0].other_answer1}", True, white)
    Other2Text= smallfont.render(f"{questions[0].other_answer2}", True, white)
    Other3Text= smallfont.render(f"{questions[0].other_answer3}", True, white)

    LetterText= smallfont.render(f"{questions[0].letter}", True, white)

    Letter1Text= smallfont.render(f"{questions[0].other_letter1}", True, white)
    Letter2Text= smallfont.render(f"{questions[0].other_letter2}", True, white)
    Letter3Text= smallfont.render(f"{questions[0].other_letter3}", True, white)

    while True:
        screen.fill(0,0,0)
        screen.blit(background,[0,0])

        order_dict={'A':58, 'B':78, 'C':93, 'D':110}

        screen.blit(QuestionText, (800,10))
        screen.blit(AnswerText, (800, order_dict[Rindex.letter]))

        screen.blit(Other1Text, (800, order_dict[Rindex.other_letter1]))
        screen.blit(Other2Text, (800, order_dict[Rindex.other_letter2]))
        screen.blit(Other3Text, (800, order_dict[Rindex.other_letter3]))

        screen.blit(LetterText, (800, order_dict[Rindex.letter]))

        screen.blit(Letter1Text, (800, order_dict[Rindex.other_letter1]))
        screen.blit(Letter2Text, (800, order_dict[Rindex.other_letter2]))
        screen.blit(Letter3Text, (800, order_dict[Rindex.other_letter3]))

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_LEFT:
                    playerX_change= -0.4
                if event.key== pygame.K_RIGHT:
                    playerX_change= 0.4
                if event.key== pygame.K_SPACE:
                    if bullet_state is "ready":
                        bulletSound= mixer.Sound("Gun+Silencer.mp3")
                        bulletSound.play()

                        bulletX= playerX
                        bullet_state= "fire"
                        screen.blit(bulletImg, (bulletX+16,  bulletY+10))
                        fire_bullet(bulletX, bulletY)

            if event.type== pygame.KEYIP:
                if event.key== pygame.K_LEFT or event.key== pygame.K_RIGHT:
                    playerX_change=0

            playerX += playerX_change

            if playerX <=0:
                playerX=0
            elif playerX >=736:
                playerX=736

            for i in range(num_of_enemies):
                if enemyY[i]>440 or end_index >= (len(questions)):
                    game_over_screen()
                    break
                enemyX[i] += enemyX_change[i]
                if enemyX[i]<=0:
                    enemyX_change[i]=0.3
                    enemyY[i]+= enemyY_change[i]
                elif enemyX[i]>= 736:
                    enemyX_change[i]= -0.3
                    enemyY[I]+= enemyY_change[i]

                collision= isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
                if collision:
                    explosion_sound= mixer.sound('explosion.wav')
                    explosion_sound.play()
                    bulletY= 489
                    bullet_state= "ready"

                if Rindex.enemy != enemyImg[i]:
                    score_value= score_value
                    score_state= "locked"

                if Rindex.enemy== enemyImg[i]:
                    end_index +=1

                    if score_state== "locked":
                        score_value= score_value
                        score_state= "unlocked"
                    else:
                        score_value +=1

                    QuestionText= font.render(f"{index.prompt}:", True, white)

                    AnswerText= smallfont.render(f"{index.answer}", True, white)

                    Other1Text= smallfont.render(f"{index.other_answer1}:", True, white)
                    Other2Text= smallfont.render(f"{index.other_answer2}:", True, white)
                    Other3Text= smallfont.render(f"{index.other_answer3}:", True, white)

                    LetterText= smallfont.render(f"{Lindex.letter}:", True, white)
                    Lother1Text= smallfont.render(f"{Lindex.other_letter1}:", True, white)
                    Lother2Text= smallfont.render(f"{Lindex.other_letter2}:", True, white)
                    Lother3Text= smallfont.render(f"{Lindex.other_letter3}:", True, white)

                    if int_index>= (len(questions)-1):
                        index= questions[int_index]
                        Lindex= questions[let_index]
                        if real_index >= (len(questions)-1):
                            Rindex= questions[real_index]

                            enemyX[0]= random.randint(0, 735)
                            enemyY[0]= random.randint(50, 100)
                            enemy(enemyX[0], enemyY[0], 0)

                            enemyX[1]= random.randint(0, 735)
                            enemyY[1]= random.randint(50, 100)
                            enemy(enemyX[1], enemyY[1], 1)

                            enemyX[2]= random.randint(0, 735)
                            enemyY[2]= random.randint(50, 100)
                            enemy(enemyX[2], enemyY[2], 2)

                            enemyX[3]= random.randint(0, 735)
                            enemyY[3]= random.randint(50, 100)
                            enemy(enemyX[3], enemyY[3], 3)

                        else:
                            real_index +=1
                            Rindex= questions[real_index]

                            enemyX[0]= random.randint(0,735)
                            enemyY[0]= random.randint(50,100)
                            enemy(enemyX[0], enemyY[0], 0)

                            enemyX[1]= random.randint(0,735)
                            enemyY[1]= random.randint(50,100)
                            enemy(enemyX[1], enemyY[1], 1)

                            enemyX[2]= random.randint(0,735)
                            enemyY[2]= random.randint(50,100)
                            enemy(enemyX[2], enemyY[2], 2)

                            enemyX[3]= random.randint(0,735)
                            enemyY[3]= random.randint(50,100)
                            enemy(enemyX[3], enemyY[3], 3)

                    else:
                        int_index += 1
                        index= questions[int_index]

                        real_index +=1
                        Rindex= questions[real_index]

                        let_index +=1
                        Lindex= questions[let_index]

                        enemyX[0]= random.randint(0,735)
                        enemyY[0]= random.randint(50,100)
                        enemy(enemyX[0], enemyY[0], 0)

                        enemyX[1]= random.randint(0,735)
                        enemyY[1]= random.randint(50,100)
                        enemy(enemyX[1], enemyY[1], 1)

                        enemyX[2]= random.randint(0,735)
                        enemyY[2]= random.randint(50,100)
                        enemy(enemyX[2], enemyY[2], 2)

                        enemyX[3]= random.randint(0,735)
                        enemyY[3]= random.randint(50,100)
                        enemy(enemyX[3], enemyY[3], 3)

                enemyX[i]= random.randint(0,735)
                enemyY[i]= random.randint(50,100)

            enemy(enemyX[i], enemyY[i], i)
        if bulletY <=0:
            bulletY= 480
            bullet_state= "ready"
        if bullet_state is "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        show_score(testX, testY)
        pygame.display.update()

while True:
    start_menu()
    for event in pygame.event.get():
        if event.type== pyagme.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()