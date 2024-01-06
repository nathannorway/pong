#Author Nathan Norway
import pygame
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

#set up game
pygame.init()
window_w , window_h = 1280,720
screen_h = 820
window = pygame.display.set_mode((window_w,screen_h))
background = pygame.image.load('assets/images/ntntable.jpg').convert()
background = pygame.transform.scale(background,(window_w,window_h))
clock = pygame.time.Clock()
running = True

#create paddles
playerOne = Paddle(50,(window_h // 2 - 60), 10, 120,window_w,window_h)
playerTwo = Paddle(window_w - 60, window_h // 2 - 60, 10,120,window_w,window_h)
ball = Ball(window_w // 2, window_h //2 , 10)
scoreboard = Scoreboard(window)

#collision check function
def check_collision(ball,paddle):
    return ball.rect.colliderect(paddle.rect)


#game loop
while running: 
    #poll for events
    #pygame.QUIT event means user clicked X to close your window

    #loop to check for game state. 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerTwo.moving_up = True
            elif event.key == pygame.K_DOWN:
                playerTwo.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                playerTwo.moving_up = False
            elif event.key == pygame.K_DOWN:
                playerTwo.moving_down = False

   
    
    #Updating the game state
    playerTwo.move()
    playerOne.move_ntn(ball)
    ball.move()

    #check for collisions
    if check_collision(ball,playerTwo):
        ball.bounce('x')
    elif check_collision(ball,playerOne):
        ball.bounce('x')
    
    #check for scores
    if ball.x - ball.radius <= 0:
        scoreboard.increment_score("playerTwo")
        ball.reset()
    
    if ball.x + ball.radius >= window_w:
        scoreboard.increment_score("playerOne")
        ball.reset()



    #render game here
    window.blit(background, (0,+100))
    playerOne.draw(window)
    playerTwo.draw(window)
    ball.draw(window)
    scoreboard.render()
    

    #flip display to put your work on screen 
    pygame.display.flip()

    clock.tick(60) #limits FPS to 60

pygame.quit()