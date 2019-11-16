import pygame
import sys

import imageMapping
import random

pygame.init()

screen = pygame.display.set_mode((800,900))

clock = pygame.time.Clock()

done = False

imageCount = 8

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        n = random.randint(1,imageCount*(imageCount-1)*(imageCount-2))
                        threeImages =  imageMapping.images(n, imageCount)
                        eq1 = pygame.image.load("static/Eq" + str(threeImages[0]) + ".png")
                        eq1_x = 0
                        eq1_y = 0
                        screen.blit(eq1, (eq1_x, eq1_y))
                        eq2 = pygame.image.load("static/Eq" + str(threeImages[1]) + ".png")
                        eq2_x = 0
                        eq2_y = 300
                        screen.blit(eq2, (eq2_x, eq2_y))
                        eq3 = pygame.image.load("static/Eq" + str(threeImages[2]) + ".png")
                        eq3_x = 0
                        eq3_y = 600
                        screen.blit(eq3, (eq3_x, eq3_y))

        pygame.display.flip()
        
