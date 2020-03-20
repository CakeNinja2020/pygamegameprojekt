import pygame
import time

pygame.init()

# Display settings
screen = pygame.display.set_mode((900, 750))
pygame.display.set_caption("Definitely not SpaceINvaders")
icon = pygame.image.load('icon1.png')
pygame.display.set_icon(icon)

test_sprite = makeSprte