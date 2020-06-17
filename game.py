#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://github.com/edoardottt
https://edoardoottavianelli.it
"""

#=============IMPORT=============
import pygame


#=============PREPARATION============
pygame.init()

WIDTH = 1200
HEIGHT = 600
BORDER = 20
WHITE = pygame.Color("white")
BLACK = pygame.Color("black")
GREEN = pygame.Color("green")
BLUE = pygame.Color("blue")
VELOCITY = 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))

#-------Ball-------
class Ball:
    
    RADIUS = 15
    
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    
    def show(self,color):
        pygame.draw.circle(screen, color, (self.x, self.y), self.RADIUS)
        
    def update(self, paddle_y, paddle_WIDTH, paddle_HEIGHT):
        newx = self.x + self.vx
        newy = self.y + self.vy
        
        if paddle_y - paddle_HEIGHT//2 < newy and newy < paddle_y + paddle_HEIGHT//2 and newx >= WIDTH - paddle_WIDTH - self.RADIUS:
            self.vx = - self.vx
        
        if newx < BORDER + self.RADIUS:
            self.vx = - self.vx
        elif newy < BORDER + self.RADIUS or newy > HEIGHT - BORDER - self.RADIUS:
            self.vy = - self.vy
        else:
            self.show(BLACK)
            self.x += self.vx
            self.y += self.vy
            self.show(GREEN)
        
#-------Paddle-------
class Paddle:
    WIDTH = 20
    HEIGHT = 100
    
    def __init__(self,y):
        self.y = y
        
    def show(self, colour):
        pygame.draw.rect(screen, colour, pygame.Rect((WIDTH - self.WIDTH, self.y - self.HEIGHT//2),(self.WIDTH,self.HEIGHT)))
        
    def update(self):
        mouse = pygame.mouse.get_pos()[1]
        if not(mouse - self.HEIGHT//2 <= BORDER or mouse + self.HEIGHT//2 >= HEIGHT - BORDER):
            self.show(BLACK)
            self.y = mouse
            self.show(BLUE)
        elif mouse + self.HEIGHT//2 <= BORDER:
            self.y = self.HEIGHT//2 + BORDER
        else:
            self.y = HEIGHT -self.HEIGHT//2 - BORDER

paddle = Paddle(HEIGHT//2)
        
ball = Ball(WIDTH - Ball.RADIUS - paddle.WIDTH, HEIGHT//2, -VELOCITY, -VELOCITY)

#top border
pygame.draw.rect(screen, WHITE ,pygame.Rect((0,0),(WIDTH,BORDER)))

#left border
pygame.draw.rect(screen, WHITE ,pygame.Rect(0,0,BORDER,HEIGHT))

#bottom border
pygame.draw.rect(screen, WHITE ,pygame.Rect(0,HEIGHT - BORDER,WIDTH,BORDER))

ball.show(GREEN)

paddle.show(BLUE)

#=============GAME============
while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT: break
    
    ball.update(paddle.y, paddle.WIDTH, paddle.HEIGHT)
    
    paddle.update()
    
    #refresh
    pygame.display.flip()

pygame.quit()