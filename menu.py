import math
import pygame
from pygame.locals import *
import random
import time

# init do pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
screen.fill((255, 255, 255))

# Titulo e icone
pygame.display.set_caption("Ai Q Fome")
icon = pygame.image.load('fruits.png')
pygame.display.set_icon(icon)

# Variáveis de música
Musica = True
Som = True

# Mapas de Jogo
#mapajogo1 = pygame.image.load("cenario/cozinha_semagua.png").convert()

# Músicas
imfine = pygame.mixer.music.load("Interplanetary Odyssey.ogg")
pygame.mixer.music.play()


# MENU
def menu():
    # Variáveis bool que definem o andamento do menu
    Menu = True
    Controles = False
    Sobre = False
    opc1 = False
    opc2 = False
    opc3 = False
    global Musica
    global Som
    # Imagens de Background
    telainicial = pygame.image.load("TelaMenuComSom.png").convert()
    controles = pygame.image.load("TelaControlesDoJogo.png").convert_alpha()
    sobre = pygame.image.load("TelaSobreOJogo.png").convert_alpha()

    # Imagens
    cabeca = pygame.image.load("apple.png").convert_alpha()
    cabeca2 = pygame.image.load("apple.png").convert_alpha()

    while Menu:
        mouse_position = pygame.mouse.get_pos()
        screen.blit(telainicial, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEMOTION:
                if mouse_position[0] >= 303 and mouse_position[0] <= 495 and mouse_position[1] >= 196 and \
                        mouse_position[1] <= 263:
                    opc1 = True
                else:
                    opc1 = False
                if mouse_position[0] >= 304 and mouse_position[0] <= 494 and mouse_position[1] >= 295 and \
                        mouse_position[1] <= 360:
                    opc2 = True
                else:
                    opc2 = False
                if mouse_position[0] >= 304 and mouse_position[0] <= 495 and mouse_position[1] >= 401 and \
                        mouse_position[1] <= 463:
                    opc3 = True
                else:
                    opc3 = False
            if event.type == MOUSEBUTTONDOWN:
                # Botão de Som
                if mouse_position[0] >= 712 and mouse_position[0] <= 756 and mouse_position[1] >= 512 and \
                        mouse_position[1] <= 570 and Musica == True and Som == True:
                    telainicial = pygame.image.load("TelaMenuSemSom.png").convert()
                    pygame.mixer.music.stop()
                    Som = False
                elif mouse_position[0] >= 712 and mouse_position[0] <= 756 and mouse_position[1] >= 512 and \
                        mouse_position[1] <= 570 and Musica == True and Som == False:
                    telainicial = pygame.image.load("TelaMenuComSom.png").convert()
                    pygame.mixer.music.play()
                    Som = True
                elif mouse_position[0] >= 712 and mouse_position[0] <= 756 and mouse_position[1] >= 512 and \
                        mouse_position[1] <= 570 and Musica == False and Som == False:
                    telainicial = pygame.image.load("TelaMenuComSom.png").convert()
                    pygame.mixer.music.play()
                    Som = True
                elif mouse_position[0] >= 712 and mouse_position[0] <= 756 and mouse_position[1] >= 512 and \
                        mouse_position[1] <= 570 and Musica == False and Som == True:
                    telainicial = pygame.image.load("TelaMenuSemSom.png").convert()
                    pygame.mixer.music.stop()
                    Som = False

                # Botões do Menu _
                if mouse_position[0] >= 303 and mouse_position[0] <= 495 and mouse_position[1] >= 196 and \
                        mouse_position[1] <= 263 and Menu == True:
                    Menu = False
                if mouse_position[0] >= 304 and mouse_position[0] <= 495 and mouse_position[1] >= 401 and \
                        mouse_position[1] <= 463 and Controles == False:
                    Controles = True
                elif mouse_position[0] >= 23 and mouse_position[0] <= 124 and mouse_position[1] >= 541 and mouse_position[
                    1] <= 572 and Controles == True:
                    Controles = False
                if mouse_position[0] >= 304 and mouse_position[0] <= 494 and mouse_position[1] >= 295 and \
                        mouse_position[1] <= 360 and Sobre == False:
                    Sobre = True
                elif mouse_position[0] >= 23 and mouse_position[0] <= 124 and mouse_position[1] >= 541 and mouse_position[
                    1] <= 572 and Sobre == True:
                    Sobre = False

            # Hover Selecionado
            if opc1:
                screen.blit(cabeca, (255, 215))
            if opc2:
                screen.blit(cabeca2, (475, 325))
            if opc3:
                screen.blit(cabeca, (255, 420))

            if Controles:
                screen.blit(controles, (0, 0))
            if Sobre:
                screen.blit(sobre, (0, 0))

            # printar tela
            pygame.display.update()
            clock.tick(30)
