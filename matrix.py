import pygame
import random
import sys

# Inicializar o Pygame
pygame.init()

# Definir dimensões da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix Effect")

# Cores
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Fonte
FONT_SIZE = 20
font = pygame.font.SysFont('Consolas', FONT_SIZE)

# Caracteres possíveis
characters = "アァイィウエオカキクケコサシスセソタチツテトナニヌネノABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Calcular número de colunas
columns = int(WIDTH / FONT_SIZE)
drops = [0 for _ in range(columns)]  # Posição Y de cada coluna

clock = pygame.time.Clock()

while True:
    # Encerrar se fechar a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Pintar fundo com transparência
    screen.fill((0, 0, 0, 10))

    for i in range(len(drops)):
        char = random.choice(characters)
        text = font.render(char, True, GREEN)
        x = i * FONT_SIZE
        y = drops[i] * FONT_SIZE

        # Desenhar caractere
        screen.blit(text, (x, y))

        # Atualizar posição
        if y > HEIGHT or random.random() > 0.95:
            drops[i] = 0
        else:
            drops[i] += 1

    pygame.display.flip()
    clock.tick(30)
