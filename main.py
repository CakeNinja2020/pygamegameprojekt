import pygame
import time
import random
from comet import comet_class

pygame.init()

# Display settings
screen_width = 1200
screen_height = 675
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Definitely not SpaceINvaders")
icon = pygame.image.load('icon1.png')
pygame.display.set_icon(icon)

# Background Image
background = pygame.image.load('bg/29.png')

comet = [pygame.image.load('cmt/1.png'), pygame.image.load('cmt/2.png'), pygame.image.load('cmt/3.png'),
         pygame.image.load('cmt/4.png'), pygame.image.load('cmt/5.png'), pygame.image.load('cmt/6.png'),
         pygame.image.load('cmt/7.png'), pygame.image.load('cmt/8.png'), pygame.image.load('cmt/9.png'),
         pygame.image.load('cmt/10.png')]
world_destroyer = []

# Sound Files
sound_click = pygame.mixer.Sound('sounds/click.wav')

# Main menu buttons
distance_between_buttons = (screen_height / 10)/2
# Name
name_resolution = [750, 250]
name_image = pygame.image.load('name4.png')
name_imageXL = (screen_width / 2) - (name_resolution[0] / 2)
name_imageYU = distance_between_buttons
# D - dark, L - light, C - Clicked
start_button_resolution = [172, 96]
start_button_passive = pygame.image.load('startD1.png')
start_button_active = pygame.image.load('startL6.png')
start_button_down = pygame.image.load('startC1.png')
start_buttonXL = (screen_width / 2) - (start_button_resolution[0] / 2)
start_buttonXR = (screen_width / 2) + (start_button_resolution[0] / 2)
start_buttonYU = name_imageYU + name_resolution[1] + distance_between_buttons*2
start_buttonYD = start_buttonYU + start_button_resolution[1]
# 172, 96
settings_button_resolution = [205, 72]
settings_button_passive = pygame.image.load('settingsD3.png')
settings_button_active = pygame.image.load('settingsL4.png')
settings_buttonXL = (screen_width / 2) - (settings_button_resolution[0] / 2)
settings_buttonXR = (screen_width / 2) + (settings_button_resolution[0] / 2)
settings_buttonYU = start_buttonYD + distance_between_buttons
settings_buttonYD = settings_buttonYU + settings_button_resolution[1]
# 200, 72
quit_button_resolution = [116, 58]
quit_button_passive = pygame.image.load('quitD3.png')
quit_button_active = pygame.image.load('quitL3.png')
quit_buttonXL = (screen_width / 2) - (quit_button_resolution[0] / 2)
quit_buttonXR = (screen_width / 2) + (quit_button_resolution[0] / 2)
quit_buttonYU = settings_buttonYD + distance_between_buttons
quit_buttonYD = quit_buttonYU + quit_button_resolution[1]

# Settings Menu
settings_menu_main_resolution = [460,176]
settings_menu_main = pygame.image.load('settingsM3.png')
settings_menu_mainXL = (screen_width/2) - settings_button_resolution[0]
settings_menu_mainYU = distance_between_buttons
# 460,176
settings_back_resolution = [115,48]
settings_back_passive = pygame.image.load('backD1.png')
settings_back_active = pygame.image.load('backL1.png')
settings_backXL = (screen_width/2) - (settings_back_resolution[0]/2)
settings_backXR = settings_backXL + (settings_button_resolution[0]/2)
settings_backYU = settings_menu_mainYU+settings_menu_main_resolution[1]+distance_between_buttons
settings_backYD = settings_backYU + 48
# 115, 48


def destroy_worlds_top():
    world_destroyer.append(comet_class(2000, random.randint((screen_width * -1), screen_height), comet))


for n in range(1):
    destroy_worlds_top()


def main_menu():
    global game_state
    global running

    # background sprite
    screen.blit(background, (0, 0))
    for n in world_destroyer:
        n.upda  te()
        if n.x < -166 or n.y > 899:
            world_destroyer.remove(n)
            destroy_worlds_top()

    for n in world_destroyer:
        n.draw(screen)
    screen.blit(name_image, (name_imageXL, name_imageYU))

    mouse = pygame.mouse.get_pos()
    # Start Button check
    if start_buttonXR > mouse[0] > start_buttonXL and start_buttonYD > mouse[1] > start_buttonYU:
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.blit(start_button_down, (start_buttonXL - 86, start_buttonYU))
            screen.blit(settings_button_passive, (settings_buttonXL, settings_buttonYU))
            screen.blit(quit_button_passive, (quit_buttonXL, quit_buttonYU))
            game_state = "game"

        else:
            screen.blit(start_button_active, (start_buttonXL, start_buttonYU))
            screen.blit(settings_button_passive, (settings_buttonXL, settings_buttonYU))
            screen.blit(quit_button_passive, (quit_buttonXL, quit_buttonYU))
    # settings button check
    elif settings_buttonXR > mouse[0] > settings_buttonXL and settings_buttonYD > mouse[1] > settings_buttonYU:
        if event.type == pygame.MOUSEBUTTONDOWN:
            game_state = "settings"
        else:
            screen.blit(settings_button_active, (settings_buttonXL, settings_buttonYU))
            screen.blit(start_button_passive, (start_buttonXL, start_buttonYU))
            screen.blit(quit_button_passive, (quit_buttonXL, quit_buttonYU))

    elif quit_buttonXR > mouse[0] > quit_buttonXL and quit_buttonYD > mouse[1] > quit_buttonYU:
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = False
        else:
            screen.blit(quit_button_active, (quit_buttonXL, quit_buttonYU))
            screen.blit(start_button_passive, (start_buttonXL, start_buttonYU))
            screen.blit(settings_button_passive, (settings_buttonXL, settings_buttonYU))


    else:
        screen.blit(start_button_passive, (start_buttonXL, start_buttonYU))
        screen.blit(settings_button_passive, (settings_buttonXL, settings_buttonYU))
        screen.blit(quit_button_passive, (quit_buttonXL, quit_buttonYU))


def settings_menu():
    global game_state
    global background_count

    screen.blit(background, (0, 0))
    for n in world_destroyer:
        n.update()
        if n.x < -166 or n.y > 899:
            world_destroyer.remove(n)
            destroy_worlds_top()

    for n in world_destroyer:
        n.draw(screen)

    screen.blit(settings_menu_main, (settings_menu_mainXL,settings_menu_mainYU))
    mouse = pygame.mouse.get_pos()
    if settings_backXL < mouse[0] < settings_backXR and settings_backYU < mouse[1] < settings_backYD:
        if event.type == pygame.MOUSEBUTTONDOWN:
            game_state = "main"
        else:
            screen.blit(settings_back_active, (settings_backXL, settings_backYU))
    else:
        screen.blit(settings_back_passive, (settings_backXL, settings_backYU))


def level_menu():
    global game_state
    global rocket_count
    screen.blit(background[29], (0, 0))
    if rocket_count >= 3:
        rocket_count = 0
    screen.blit(rocket[rocket_count], (386, 600))
    rocket_count += 1


# vi skal finde på en måde at lave forskellige levels... arbejder på det


game_state = "main"

# Game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        sound_click.play()

    if game_state == "main":
        main_menu()
    if game_state == "settings":
        settings_menu()
    if game_state == "game":
        level_menu()
    # Skifte game_state til de forskellige levels på en måde.
    else:
        pass

    pygame.display.update()
