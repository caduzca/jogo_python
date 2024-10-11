# Importa a biblioteca pygame para o script
import pygame

# pygame configuração 
pygame.init()# inicialização do pygame
pygame.font.init()#inicialização do pacote de fontes no pygame


screen = pygame.display.set_mode((500, 500)) # definição do tamanho da tela do jogo 
clock = pygame.time.Clock() #Bliblioteca de tempo
running = True 
pygame.display.set_caption("Jogo Da Velha")


cor_fundo = 1 
#cor_fundo = 2
fonte_quadrinhos = pygame.font.SysFont('Comic Sans Ms', 30)#importar fontes
personagem_x = fonte_quadrinhos.render('X', True, 'red')
personagem_o = fonte_quadrinhos.render('0', True, 'red')
while running:
    # Controle de eventos 
    # 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: #Evento que indica que o click do mouse
            print('clicou')
            cor_fundo = cor_fundo +1     
            if (cor_fundo > 3):
                cor_fundo = 1

    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("blue")
   

    # RENDER YOUR GAME HERE
    if cor_fundo == 1:
        screen.fill('black')
        screen.blit(personagem_x,(250,250))
    elif cor_fundo == 2:
        screen.fill('black')
        screen.blit(personagem_o,(250,250))
        
    else:
        screen.fill('purple')  
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limita FPS para 60

pygame.quit()