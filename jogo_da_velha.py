# Importa a biblioteca pygame para o script
import pygame

# pygame configuração 
pygame.init()# inicialização do pygame
pygame.font.init()#inicialização do pacote de fontes no pygame


screen = pygame.display.set_mode((600, 600)) # definição do tamanho da tela do jogo 
pygame.display.set_caption("Jogo Da Velha") 
clock = pygame.time.Clock() #Bliblioteca de tempo

fonte_quadrinhos = pygame.font.SysFont('Comic Sans Ms', 100)#importar fontes
running = True

personagem_x = fonte_quadrinhos.render('X', True, 'red')
personagem_o = fonte_quadrinhos.render('O', True, 'green')

jogador_atual = personagem_x #inicializa o jogo com x

rodadas = 0 
tabuleiro_desenhado = False
cordenada_x = 0
cordenada_y = 0

q1 = ''
q2 = ''
q3 = ''
q4 = ''
q5 = ''
q6 = ''
q7 = ''
q8 = ''
q9 = ''

def desenha_tabuleiro(espessura, cor):
    #Desenha tabuleiro                  
  #                                   Origem        Destino
  #                                   ( x ,  y)  ( x , y )  
    pygame.draw.line(screen, cor , (200, 0), (200, 600), espessura)
    pygame.draw.line(screen, cor , (400, 0), (400, 600), espessura)
    pygame.draw.line(screen, cor , (0, 200), (600, 200), espessura)
    pygame.draw.line(screen, cor , (0, 400), (600, 400), espessura)
  
     
   
def faz_jogada():
   
    global q1, q2, q3, q4, q5, q6, q7, q8, q9
    status = True
    if q1 == '' and cordenada_x > 0 and cordenada_x < 200 and cordenada_y < 200:
        screen.blit(jogador_atual,(60, 30)) #primeira 
        q1 = jogador_atual
    
    elif q2 == '' and cordenada_x >= 200 and cordenada_x < 400 and cordenada_y < 200:
        screen.blit(jogador_atual,(260, 30)) #segunda
        q2 = jogador_atual
    elif  q3 == '' and cordenada_x >= 400 and cordenada_y < 200:
        screen.blit(jogador_atual,(460, 30)) #terceira
        q3 = jogador_atual   
    elif q4 == '' and cordenada_x < 200 and cordenada_y >= 200 and cordenada_y < 400:
        screen.blit(jogador_atual,(60, 230)) #quarta
        q4 = jogador_atual
    elif q5 == '' and cordenada_x >= 200 and cordenada_x < 400 and cordenada_y >= 200 and cordenada_y < 400:
        screen.blit(jogador_atual,(260, 230)) #quinto
        q5 = jogador_atual
    elif q6 == '' and cordenada_x >= 400 and cordenada_y >= 200 and cordenada_y < 400:
        screen.blit(jogador_atual,(460, 230)) #sexto
        q6 = jogador_atual
    elif q7 == '' and cordenada_x < 200 and cordenada_y >= 400:
        screen.blit(jogador_atual,(60, 430)) #setimo
        q7 = jogador_atual
    elif q8 == '' and cordenada_x >= 200 and cordenada_x < 400 and cordenada_y >= 400:
        screen.blit(jogador_atual,(260, 430)) #oitavo
        q8 = jogador_atual
    elif q9 == '' and cordenada_x >= 400 and cordenada_y >= 400:
        screen.blit(jogador_atual,(460, 430)) #nono
        q9 = jogador_atual
    else:
        status = False
    
    return status        

def check_vencedor():
    status = False
    if q1 == q2 == q3 != '':
        pygame.draw.line(screen, 'white' , (50, 100), (550, 100), 10)
        status = True
    elif q4 == q5 == q6 != '':
        pygame.draw.line(screen, 'white' , (50, 300), (550, 300), 10)
        status = True
    elif q7 == q8 == q9 != '':
        pygame.draw.line(screen, 'white' , (50, 500), (550, 500), 10)
        status = True
    elif q1 == q4 == q7 != '':
        pygame.draw.line(screen, 'white' , (100, 50), (100, 550), 10)
        status = True
    elif q2 == q5 == q8 != '':
        pygame.draw.line(screen, 'white' , (300, 50), (300, 550), 10)
        status = True                
    elif q3 == q6 == q9 != '':
        pygame.draw.line(screen, 'white' , (500, 50), (500, 550), 10)
        status = True
    elif q1 == q5 == q9 != '':
        pygame.draw.line(screen, 'white' , (50, 50), (550, 550), 10)
        status = True
    elif q3 == q5 == q7 != '':
        pygame.draw.line(screen, 'white' , (550, 50), (50, 550), 10)
        status = True
    return status
    

while running:
    # Controle de eventos 
    # 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            cordenada_x = pos [0]
            cordenada_y = pos [1]
            
            if(rodadas >= 9):
                screen.fill('black')
                rodadas = 0
                cordenada_x = 0
                cordenada_y = 0
                jogador_atual = personagem_x
                tabuleiro_desenhado = False
                break
            if(faz_jogada()):
                rodadas = rodadas + 1
                if jogador_atual == personagem_x:
                    jogador_atual = personagem_o
                else:
                    jogador_atual = personagem_x
                if (check_vencedor()):
                    rodadas = 9    

                
                     

    if tabuleiro_desenhado == False:

        desenha_tabuleiro(20, 'gray')
        q1 = ''
        q2 = ''
        q3 = ''
        q4 = ''
        q5 = ''
        q6 = ''
        q7 = ''
        q8 = ''
        q9 = ''
    
    if tabuleiro_desenhado == False:
        desenha_tabuleiro(10, 'blue' )
        tabuleiro_desenhado = True
    
            #     primeira linha   
     
    pygame.display.flip()

    clock.tick(60)  # limita FPS para 60

pygame.quit()