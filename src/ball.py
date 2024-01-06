#ball class file
import pygame
import random



class Ball:
    #init
    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        self.original_x = x
        self.original_y = y + 100
        self.radius = radius
        self.color = 255,255,255  #White 255,255,255

        #set speed
        self.x_velocity = 5
        self.y_velocity = 5
        self.accel_bump = .5


        self.rect = pygame.Rect(x-radius,y-radius,radius*2,radius*2)

         #define ball movement
    
    def move(self):
        #update position
        self.x += self.x_velocity
        self.y += self.y_velocity


        if self.y - self.radius <= 100 or self.y + self.radius >= 820:
            self.bounce('y')

        if self.x - self.radius <= 0 or self.x + self.radius >= 1280:
            self.bounce('x')
       
        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        pygame.time.delay(1000)

        self.x_velocity = random.uniform(-5,5)
        self.y_velocity = random.uniform(-5,5)
        if self.x_velocity == 0: self.x_velocity = -3
        if self.y_velocity == 0: self.y_velocity = 3

        


    #function to create the paddles in game window
    def draw(self,window):
        pygame.draw.circle(window,self.color,(self.x,self.y),self.radius)


    def bounce(self,axis):
        if axis == 'x':
            self.x_velocity = -self.x_velocity 
            if self.x_velocity >=0:
                self.x_velocity += self.accel_bump
            else:
                self.x_velocity -= self.accel_bump
            
        elif axis == 'y':
            self.y_velocity = -self.y_velocity