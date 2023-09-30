import pygame
from sys import exit

# Inicializa o pygame
pygame.init()

# Cria a tela
tamanho = (960, 540)
tela = pygame.display.set_mode(tamanho)


# Define o título da janela
pygame.display.set_caption("ChuvaMortal")

# Importa os arquivos necessarios
# Carrega as imagens de plano de fundo
plano_fundo = pygame.image.load('assets/fundo/Night-Background8.png').convert()
fundo_estrelas = pygame.image.load('assets/fundo/Night-Background7.png').convert_alpha()
fundo_estrelas_2 = pygame.image.load('assets/fundo/Night-Background6.png').convert_alpha()
fundo_estrelas_3 = pygame.image.load('assets/fundo/Night-Background5.png').convert_alpha()
fundo_rochas = pygame.image.load('assets/fundo/Night-Background4.png').convert_alpha()
fundo_chao = pygame.image.load('assets/fundo/Night-Background3.png').convert_alpha()
fundo_lua = pygame.image.load('assets/fundo/Night-Background2.png').convert_alpha()
fundo_rochas_voadoras = pygame.image.load('assets/fundo/Night-Background1.png').convert_alpha()

#Transforma as imagens de fundo para o tamanho da tela
plano_fundo = pygame.transform.scale(plano_fundo, tamanho)
fundo_estrelas = pygame.transform.scale(fundo_estrelas, tamanho)
fundo_estrelas_2 = pygame.transform.scale(fundo_estrelas_2, tamanho)
fundo_estrelas_3 = pygame.transform.scale(fundo_estrelas_3, tamanho)
fundo_rochas = pygame.transform.scale(fundo_rochas, tamanho)
fundo_chao = pygame.transform.scale(fundo_chao, tamanho)
fundo_lua = pygame.transform.scale(fundo_lua, tamanho)
fundo_rochas_voadoras = pygame.transform.scale(fundo_rochas_voadoras, tamanho)

# Carrega as imagens do personagem parado
jogador_index = 0
jogador_parado_surfaces = []

for imagem in range(1, 14):
    img=pygame.image.load(f'assets/jogador/parado/Hero Boy Idle{imagem}.png').convert_alpha()
    jogador_parado_surfaces.append(img)

# Importa o personagem

#jogador_parado_surf = pygame.image.load('assets/jogador/parado/Hero Boy Idle1.png').convert_alpha()
jogador_parado_rect = jogador_parado_surfaces[jogador_index].get_rect( center =(100,430))
jogador_voando_rect = jogador_parado_rect
movimento_personagem = 0
direcao_personagem = 0
# Carrega as imagens do personagem voando
jogador_voando_surfaces = []

for imagem in range(1, 9):
    img=pygame.image.load(f'assets/jogador/voar/Hero Boy Fly{imagem}.png').convert_alpha()
    jogador_voando_surfaces.append(img)
    


# Cria o relógio para controlar o FPS
relogio = pygame.time.Clock()

#Loop principal do jogo


while True:
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_RIGHT:
            movimento_personagem = 2
            tela.blit(jogador_parado_surfaces[int(jogador_index)],jogador_parado_rect)
            direcao_personagem = 1
            #jogador_voando_surfaces = pygame.transform.flip(jogador_voando_surfaces, True, False)
        if evento.key == pygame.K_LEFT:
            movimento_personagem = -2
            direcao_personagem = 0
            tela.blit(jogador_parado_surfaces[int(jogador_index)],jogador_parado_rect)
        if evento.key == pygame.K_DOWN:
            movimento_personagem = 0
            tela.blit(jogador_parado_surfaces[int(jogador_index)],jogador_parado_rect)
        
    tela.blit(plano_fundo, (0,0))
    tela.blit(fundo_estrelas, (0,0))
    tela.blit(fundo_estrelas_2, (0,0))
    tela.blit(fundo_estrelas_3, (0,0))
    tela.blit(fundo_rochas, (0,0))
    tela.blit(fundo_chao, (0,0))
    tela.blit(fundo_lua, (0,0))
    tela.blit(fundo_rochas_voadoras, (0,0))

    #Desenha o jogador parado na tela
    jogador_parado_rect.x += movimento_personagem
    jogador_voando_rect.x += movimento_personagem

    if direcao_personagem ==1:
        jogador = pygame.transform.flip(jogador_voando_surfaces[int(jogador_index)], True, False)
    else:
        jogador = jogador_voando_surfaces[int(jogador_index)]

    if movimento_personagem == 0:
        tela.blit(jogador_parado_surfaces[int(jogador_index)],jogador_parado_rect)

    elif movimento_personagem > 0:
        tela.blit(jogador_voando_surfaces[int(jogador_index)],jogador_voando_rect)
    elif movimento_personagem < 0:
        tela.blit(jogador_voando_surfaces[int(jogador_index)],jogador_voando_rect)
        
    jogador_index += 0.05
    if jogador_index > len(jogador_parado_surfaces) -1:
        jogador_index = 0
    if jogador_index > len(jogador_voando_surfaces) -1:
        jogador_index = 0
    

    # Atualiza a tela com o conteudo
    pygame.display.update()

    # Define a quantidade de frame por s
    relogio.tick(60)

jogador_index = 0