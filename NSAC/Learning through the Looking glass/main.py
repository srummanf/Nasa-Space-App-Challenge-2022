import pygame
import os
import pygame.gfxdraw
import sys
import time
import random
pygame.font.init()
pygame.mixer.init()
pygame.init()
import tkinter as tk
from tkinter import *
import subprocess



health_font = pygame.font.SysFont('comicsans', 40)
fps=60
width, height = 900, 500
win = pygame.display.set_mode((width, height))
spaceship_width, spaceship_height = 55, 40
space_image = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "space-bg-1.png")), (width, height))

start = pygame.image.load(os.path.join("Assets","start2.png"))
savetheearth = pygame.image.load(os.path.join("Assets","savetheearth.png"))
space_clasher = pygame.image.load(os.path.join("Assets","space_clasher.png"))
options = pygame.image.load(os.path.join("Assets","options.png"))
credits = pygame.image.load(os.path.join("Assets","credits.png"))
jwst = pygame.image.load(os.path.join("Assets","jwst.png"))



class Button:
    def __init__(self,x,y,image, flag):
        self.flag = flag
        self.image = image
        self.rect  = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw_button(self):
        action = False
        
        event = pygame.event.poll()
        
        
        win.blit(self.image, (self.rect.x, self.rect.y)) 
        if self.flag == 0:
            pygame.display.update()
        return action

def draw_window():
    game_name = health_font.render("Celestial", 1,(200,200,200))
    win.blit(space_image,(0,0))
    win.blit(game_name,((width/2)-110, 10))
    
def main():
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
                
        start_button1 = Button(50,200,start,1)
        start_button2 = Button(350,200,savetheearth,1)
        start_button3 = Button(650,200,space_clasher,1)
        start_button4 = Button(50,340,options,1)
        start_button5 = Button(350,340,jwst,1)
        start_button6 = Button(650,340,credits,0)
        
        
        start_button1.draw_button()
        start_button2.draw_button()
        start_button3.draw_button()
        start_button4.draw_button()
        start_button5.draw_button()
        start_button6.draw_button()
        t=0
        pos=pygame.mouse.get_pos()
        left, middle, right = pygame.mouse.get_pressed()
        if(start_button1.rect.collidepoint(pos)):
            if(left):
                t=1
                if (t==1 and start_button1.clicked==False):
                    print('cli')
                    start_button1.clicked = True
                    action =True
                    subprocess.call((os.path.join("Scripts","script2.py")), shell=True)
                    t=0
                
        if pygame.mouse.get_pressed()[0] == 0:
            start_button1.clicked = False
            
        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()
