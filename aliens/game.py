import pygame
import sys
from settings import settings
from ship import ship

#pi.greeting()
def run_game():
    #inicializamos el proyecto y corremos

    pygame.init()

    ai_settings = settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")



    #set background color
    bg_color = (230,230,230)
    

    new_ship = ship(screen)
    # Start the main loop for the game.
    while (True):
        # Watch for keyboard and mouse events.
        screen.fill(ai_settings.bg_color)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sys.exit()
        
        new_ship.blitime()
        # Make the most recently drawn screen visible.
        pygame.display.flip()
run_game()