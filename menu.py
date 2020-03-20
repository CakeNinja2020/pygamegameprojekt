import pygame


class main_menu:

    title = pygame.image.load('name4.png')

    def __init__(self, screen, mouseX, mouseY):


        self.start_buttonXL = (screen[0] / 2) - (start_button_resolution[0] / 2)
        self.start_buttonXR = (screen[0] / 2) + (start_button_resolution[0] / 2)
        self.start_buttonYU = (screen[1] / 2) - (start_button_resolution[1] / 2)
        self.start_buttonYD = start_buttonYU + start_button_resolution[1]

        self.settings_buttonXL = 350
        self.settings_buttonXR = 550
        self.settings_buttonYU = 520
        self.settings_buttonYD = 592

        self.mouseX = mouseX
        self.mouseY = mouseY

    def buttons(self):
        if self.start_buttonXR > self.mouseX > self.start_buttonXL and self.start_buttonYD > self.mouseY > self.start_buttonYU:
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.blit(start_button_down, (start_buttonXL - 86, start_buttonYU))
                screen.blit(settings_button_passive, (settings_buttonXL, settings_buttonYU + 96))
                game_state = "game"

            else:
                screen.blit(start_button_active, (start_buttonXL, start_buttonYU))
                screen.blit(settings_button_passive, (settings_buttonXL, settings_buttonYU))
        elif settings_buttonXR > mouse[0] > settings_buttonXL and settings_buttonYD > mouse[1] > settings_buttonYU:
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.blit(settings_button_down, (settings_buttonXL - 100, settings_buttonYU))
                screen.blit(start_button_passive, (start_buttonXL, start_buttonYU))
                game_state = "settings"

            else:
                screen.blit(settings_button_active, (settings_buttonXL, settings_buttonYU))
                screen.blit(start_button_passive, (start_buttonXL, start_buttonYU))
        else:
            screen.blit(start_button_passive, (start_buttonXL, start_buttonYU))
            screen.blit(settings_button_passive, (settings_buttonXL, settings_buttonYU))
