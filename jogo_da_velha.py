# Importa a biblioteca pygame para o script
import pygame

# pygame configuração 
pygame.init()# inicialização do pygame
pygame.font.init()#inicialização do pacote de fontes no pygame


screen = pygame.display.set_mode((600, 600)) # definição do tamanho da tela do jogo 
clock = pygame.time.Clock() #Bliblioteca de tempo
running = True 
pygame.display.set_caption("Jogo Da Velha")


cor_fundo = 1 
#cor_fundo = 2
fonte_quadrinhos = pygame.font.SysFont('Comic Sans Ms', 60)#importar fontes
personagem_x = fonte_quadrinhos.render('X', True, 'red')
personagem_y = fonte_quadrinhos.render('O', True, 'red')
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

  #Desenha tabuleiro                  
  #                                   Origem        Destino
  #                                   ( x ,  y)  ( x , y )  
    pygame.draw.line(screen, 'white', (200, 0), (200, 600), 10)
    pygame.draw.line(screen, 'white', (400, 0), (400, 600), 10)
    pygame.draw.line(screen, 'white', (0, 200), (600, 200), 10)
    pygame.draw.line(screen, 'white', (0, 400), (600, 400), 10)
    
    if cor_fundo == 1:           #  x | y
         screen.blit(personagem_x,(80, 60))
         screen.blit(personagem_x,(460, 260))
         screen.blit(personagem_x,(280, 60))
    elif cor_fundo == 2:
         screen.blit(personagem_y,(460, 460))
         screen.blit(personagem_y,(60, 260))
         screen.blit(personagem_y,(460, 60))
        
    pygame.display.flip()

    clock.tick(60)  # limita FPS para 60

pygame.quit()