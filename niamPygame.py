import pygame
import sys

import imageMapping
import random

pygame.init()

screen = pygame.display.set_mode((800,900))

clock = pygame.time.Clock()

done = False

imageCount = 8

equationsFile = open("static/Equations.txt", "r").read().splitlines()

# Redone every game
count = 0
n = random.randint(1,imageCount*(imageCount-1)*(imageCount-2))
threeImages =  imageMapping.images(n, imageCount) # 3-tuple with the 3 id ints
eqImg = [pygame.image.load("static/Eq" + str(threeImages[i]) + ".png") for i in range(0,3) ]
eqTxt = [equationsFile[threeImages[i]-1] for i in range(0,3) ]

while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    count += 1
                    if count > 3:
                        done = True
                        break
                    # Clear screen
                    screen.fill((0,0,0)) 
                    # Add next image
                    screen.blit(eqImg[count-1], (0, 0))

    pygame.display.flip()
        
