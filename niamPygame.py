import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800,600))

clock = pygame.time.Clock()

done = False

imageCount = 8

my_image = pygame.image.load("static/Eq1.png")
my_image_x = 0
my_image_y = 0
screen.blit(my_image, (my_image_x, my_image_y))

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pass

        pygame.display.flip()
        
