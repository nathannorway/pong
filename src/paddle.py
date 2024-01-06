import pygame
import random

class Paddle:

    #class initialization 
    def __init__(self,x,y,width,height,screen_w,screen_h):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen_h = screen_h + 100
        self.color = 255,255,255  #White 255,255,255
        self.speed = 5
        self.rect = pygame.Rect(x,y,width,height)

        self.moving_up = False
        self.moving_down = False


    #define paddle movement
    def move(self):

        if self.moving_up:
            self.y = max(self.y - self.speed,100)
        if self.moving_down:
            self.y = min(self.y + self.speed, self.screen_h - self.height)
        # Update rect position as well
        self.rect.y = self.y

    
    def move_ntn(self,ball):
        #paddle center
        center = self.y + self.height / 2

        if center < ball.y - self.speed:
            self.y += random.uniform(3,6)
        elif center > ball.y + self.speed:
            self.y -= random.uniform(3,6)


        #set boundary
        self.y = max(min(self.y, self.screen_h - self.height),100)
        self.rect.y = self.y

    #function to create the paddles in game window
    def draw(self,window):
        pygame.draw.rect(window,self.color,self.rect)
