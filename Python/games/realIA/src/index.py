# Example file showing a circle moving on screen
import pygame
import random
from criar_json import criar_json

# pygame setup
pygame.init()
x, y = pygame.display.set_mode().get_size() 
screen = pygame.display.set_mode((x-200, y-200))

clock = pygame.time.Clock()
running = True
dt = 0

# Defina o número de jogadores que você deseja criar
num_jogadores = 2  # Altere para o número desejado de jogadores max 1000

# Crie uma lista para armazenar os jogadores
jogadores = []
cores = []
tamanho = []

# Crie os jogadores automaticamente usando um loop
for _ in range(num_jogadores):
    tam = random.randint(2, 20)
    cor_rgb = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    jogador = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    jogadores.append(jogador)
    cores.append(cor_rgb)
    tamanho.append(tam)

arrayPosicoes = []

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:        
            criar_json(arrayPosicoes)
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    def draw_players(jogadores):
        x = 0
        for jogador in jogadores:
            pygame.draw.circle(screen, cores[x], jogador, tamanho[x])
            x += 1

    draw_players(jogadores)

    def move(player_pos, screen_width, screen_height, velocity, dt, tam):
        rand = random.randint(0, 3)
        calcVel = velocity - (tam * 12)
        VxDt = calcVel * dt
        
        if rand == 0:
            player_pos.y -= VxDt
        elif rand == 1:
            player_pos.y += VxDt
        elif rand == 2:
            player_pos.x -= VxDt
        elif rand == 3:
            player_pos.x += VxDt
        
        # Verifique os limites do jogador e ajuste, se necessário
        player_pos.x = max(0, min(player_pos.x, screen_width))
        player_pos.y = max(0, min(player_pos.y, screen_height))
        arrayPosicoes.append({'x': player_pos.x, 'y': player_pos.y})
    # Exemplo de uso:
    # player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    # screen_width = screen.get_width()
    # screen_height = screen.get_height()
    # velocity = 500
    # dt = 0.1
    # move(player_pos, screen_width, screen_height, velocity, dt)

    def movePlayers(jogadores, screen_width, screen_height, velocity, dt):
        y = 0
        for jogador in jogadores:
            move(jogador, screen_width, screen_height, velocity, dt, tamanho[y])
            y += 1

    movePlayers(jogadores, screen.get_width(), screen.get_height(), 300, dt)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()