import pygame


WIDTH = 1920
HEIGHT = 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
player_pos = HALF_WIDTH, HALF_HEIGHT
player_speed = 2
player_angle = 0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (122, 122, 122)

pygame.init()
clock = pygame.time.Clock()

class Player:
    def __int__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

# @property
# def pos (self):
#     return (self.x, self.y)

    # def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= player_speed
        elif keys[pygame.K_s]:
            self.y += player_speed
        elif keys[pygame.K_a]:
            self.x -= player_speed
        elif keys[pygame.K_d]:
            self.x += player_speed
player = Player()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    # player.movement()

    screen.fill(BLACK)
    player = pygame.draw.circle(screen, WHITE, player_pos, 12)

    pygame.display.flip()
    clock.tick(FPS)
