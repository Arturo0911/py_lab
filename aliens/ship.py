import pygame


class ship():

    def __init__(self, screen):

        # inicializa el barco y la coloca en la posicion de inicio
        self.screen = screen

        #carga la imagen y la pone recta
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        # inicia la nave en el centro y dondo de la pantalla
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitime(self):
        #dibuja el barco y su actual localización
        self.screen.blit(self.image, self.rect)