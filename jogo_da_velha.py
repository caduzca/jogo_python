# Importa a biblioteca pygame para o script
import pygame

# pygame configuração 
pygame.init()# inicialização do pygame
pygame.font.init()#inicialização do pacote de fontes no pygame


screen = pygame.display.set_mode((600, 600)) # definição do tamanho da tela do jogo 
clock = pygame.time.Clock() #Bliblioteca de tempo
running = True 
pygame.display.set_caption("Jogo Da Velha")

rodadas = 0 
fonte_quadrinhos = pygame.font.SysFont('Comic Sans Ms', 100)#importar fontes
personagem_x = fonte_quadrinhos.render('X', True, 'red')
personagem_o = fonte_quadrinhos.render('O', True, 'green')

jogador_atual = personagem_x #inicializa o jogo com x

cordenada_x = 0
cordenada_y = 0 

while running:
    # Controle de eventos 
    # 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: #Evento que indica que o click do mouse
            print('clicou')
            pos = pygame.mouse.get_pos()
            print('eixo x:', pos[0])
            print('eixo y:', pos[1])
            cordenada_x = pos [0]
            cordenada_y = pos [1]  
            rodadas = rodadas + 1
            if(rodadas >= 10):
                screen.fill('black')
                rodadas = 0
            
            if rodadas != 1:
                if jogador_atual == personagem_x:
                    jogador_atual = personagem_o
                else:
                    jogador_atual = personagem_x
            else:
                jogador_atual = personagem_x    
                 

  #Desenha tabuleiro                  
  #                                   Origem        Destino
  #                                   ( x ,  y)  ( x , y )  
    pygame.draw.line(screen, 'white', (200, 0), (200, 600), 10)
    pygame.draw.line(screen, 'white', (400, 0), (400, 600), 10)
    pygame.draw.line(screen, 'white', (0, 200), (600, 200), 10)
    pygame.draw.line(screen, 'white', (0, 400), (600,  400), 10)
    
        #     primeira linha   
     
    if cordenada_x > 0 and cordenada_x < 200 and cordenada_y < 200:
        screen.blit(jogador_atual,(60, 30)) #primeira 
    
    elif cordenada_x >= 200 and cordenada_x < 400 and cordenada_y < 200:
         screen.blit(jogador_atual,(260, 30)) #segunda
    
    elif cordenada_x >= 400 and cordenada_y < 200:
        screen.blit(jogador_atual,(460, 30)) #terceira
    
    elif cordenada_x < 200 and cordenada_y >= 200 and cordenada_y < 400:
        screen.blit(jogador_atual,(60, 230)) #quarta
    
    elif cordenada_x >= 200 and cordenada_x < 400 and cordenada_y >= 200 and cordenada_y < 400:
        screen.blit(jogador_atual,(260, 230)) #quinto
    
    elif cordenada_x >= 400 and cordenada_y >= 200 and cordenada_y < 400:
        screen.blit(jogador_atual,(460, 230)) #sexto
    
    elif cordenada_x < 200 and cordenada_y >= 400:
        screen.blit(jogador_atual,(60, 430)) #setimo
    
    elif cordenada_x >= 200 and cordenada_x < 400 and cordenada_y >= 400:
        screen.blit(jogador_atual,(260, 430)) #oitavo
    
    elif cordenada_x >= 400 and cordenada_y >= 400:
        screen.blit(jogador_atual,(460, 430)) #nono

    
    
    pygame.display.flip()

    clock.tick(60)  # limita FPS para 60

pygame.quit()