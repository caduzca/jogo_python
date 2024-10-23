# Importa a biblioteca pygame para o script
import pygame

# pygame configuração 
pygame.init()# inicialização do pygame
pygame.font.init()#inicialização do pacote de fontes no pygame


screen = pygame.display.set_mode((600, 600)) # definição do tamanho da tela do jogo 
clock = pygame.time.Clock() #Bliblioteca de tempo
running = True 
pygame.display.set_caption("Jogo Da Velha")


apresenta_personagem = 0 
#cor_fundo = 2
fonte_quadrinhos = pygame.font.SysFont('Comic Sans Ms', 100)#importar fontes
personagem_x = fonte_quadrinhos.render('X', True, 'red')
personagem_y = fonte_quadrinhos.render('O', True, 'green')
x = 0
y = 0

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
            x = pos [0]
            y = pos [1]  
            apresenta_personagem = apresenta_personagem +1
            if(apresenta_personagem >= 10):
                screen.fill('black')
                apresenta_personagem = 0

         

  #Desenha tabuleiro                  
  #                                   Origem        Destino
  #                                   ( x ,  y)  ( x , y )  
    pygame.draw.line(screen, 'white', (200, 0), (200, 600), 10)
    pygame.draw.line(screen, 'white', (400, 0), (400, 600), 10)
    pygame.draw.line(screen, 'white', (0, 200), (600, 200), 10)
    pygame.draw.line(screen, 'white', (0, 400), (600, 400), 10)
    
        #     primeira linha   
     
    if x > 0 and x < 200 and y < 200:
        screen.blit(personagem_x,(60, 30)) #primeira 
    
    elif x >= 200 and x < 400 and y < 200:
         screen.blit(personagem_y,(260, 30)) #segunda
    
    elif x >= 400 and y < 200:
        screen.blit(personagem_x,(460, 30)) #terceira
    
    elif x < 200 and y >= 200 and y < 400:
        screen.blit(personagem_y,(60, 230)) #quarta
    
    elif x >= 200 and x < 400 and y >= 200 and y < 400:
        screen.blit(personagem_x,(260, 230)) #quinto
    
    elif x >= 400 and y >= 200 and y < 400:
        screen.blit(personagem_y,(460, 230)) #sexto
    
    elif x < 200 and y >= 400:
        screen.blit(personagem_x,(60, 430)) #setimo
    
    elif x >= 200 and x < 400 and y >= 400:
        screen.blit(personagem_y,(260, 430)) #oitavo
    
    elif x >= 400 and y >= 400:
        screen.blit(personagem_x,(460, 430)) #nono
     





    pygame.display.flip()

    clock.tick(60)  # limita FPS para 60

pygame.quit()