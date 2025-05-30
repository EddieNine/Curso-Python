import pygame
import random
import sys

# Inicializa todos os módulos do Pygame
pygame.init()

# Define o tamanho da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix Effect")  # Título da janela

# Define as cores
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Define o tamanho da fonte e carrega uma fonte monoespaçada
FONT_SIZE = 20
font = pygame.font.SysFont('Consolas', FONT_SIZE)

# Lista de caracteres para simular o efeito Matrix
characters = "アァイィウエオカキクケコサシスセソタチツテトナニヌネノABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Calcula quantas colunas cabem na tela com base no tamanho da fonte
columns = int(WIDTH / FONT_SIZE)

# Lista que armazena a posição vertical (Y) de cada coluna (inicia em 0)
drops = [0 for _ in range(columns)]

# Controlador de frames
clock = pygame.time.Clock()

# Loop principal do programa
while True:
    # Verifica se o usuário clicou para fechar a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Preenche a tela com preto (efeito de "rastro" será criado ao não limpar completamente)
    screen.fill((0, 0, 0, 10))  # Cor preta, último valor não afeta no fill (RGBA não usado aqui)

    # Percorre todas as colunas
    for i in range(len(drops)):
        # Escolhe um caractere aleatório
        char = random.choice(characters)
        # Renderiza o caractere na cor verde
        text = font.render(char, True, GREEN)
        # Define a posição X e Y onde o caractere será desenhado
        x = i * FONT_SIZE
        y = drops[i] * FONT_SIZE

        # Desenha o caractere na tela
        screen.blit(text, (x, y))

        # Se o caractere saiu da tela ou aleatoriamente com probabilidade de 5%
        if y > HEIGHT or random.random() > 0.95:
            # Reinicia a posição da gota para o topo
            drops[i] = 0
        else:
            # Faz a "gota" descer uma linha
            drops[i] += 1

    # Atualiza o conteúdo da janela
    pygame.display.flip()

    # Limita a quantidade de frames por segundo para 30
    clock.tick(30)
