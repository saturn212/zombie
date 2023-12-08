import pygame
pygame.init()

WIDTH = 800
HEIGHT = 600
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

world = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
         [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1,],
         [1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1,],
         [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1,],
         [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1,],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1,],
         [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
         [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1,],
         [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1,],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,]]

tilesize = 100
world_px = 0
world_py = 0
scroll_speed = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (122, 122, 122)
player_pos = HALF_WIDTH, HALF_HEIGHT
player_speed = 2

class Player:
    def __int__(self):
        self.x, self.y = player_pos
        if keys[pygame.K_w]:
            self.y -= player_speed
        elif keys[pygame.K_s]:
            self.y += player_speed
        elif keys[pygame.K_a]:
            self.x -= player_speed
        elif keys[pygame.K_d]:
            self.x += player_speed

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.flip()
    clock.tick(FPS)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        world_px += scroll_speed
    elif keys[pygame.K_RIGHT]:
        world_px -= scroll_speed
    if keys[pygame.K_UP]:
        world_py += scroll_speed
    elif keys[pygame.K_DOWN]:
        world_py -= scroll_speed

    world_px = min(max(world_px, -len(world[0]) * tilesize + WIDTH), 0)
    world_py = min(max(world_py, -len(world) * tilesize + HEIGHT), 0)


    screen.fill(BLACK)
    for row in range(len(world)):
        for col in range(len(world[row])):
            x = world_px + col * tilesize
            y = world_py + row * tilesize
            if world[row][col] == 1:
                pygame.draw.rect(screen, GRAY, (x, y, tilesize, tilesize), 1)
pygame.QUIT()