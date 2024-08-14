import pygame
import sys
from random import uniform

# setup 

pygame.init()
pygame.display.set_caption('Pong')
s_w, s_h = 1280, 720
screen = pygame.display.set_mode((s_w, s_h))
clock = pygame.time.Clock()
running = True
dt = 0 

# classes 

class Player1(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.Surface([120, 20])
        self.image.fill('white')
        self.rect = self.image.get_frect(midbottom = (s_w / 2, s_h))
        self.direction = pygame.Vector2()
        self.speed = 450

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        if self.rect.left < 0:
            self.rect.left = 0
        
        if self.rect.right > s_w:
            self.rect.right = s_w

class Player2(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.Surface([120, 20])
        self.image.fill('white')
        self.rect = self.image.get_frect(midtop = (s_w / 2, 0))
        self.direction = pygame.Vector2()
        self.speed = 450

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > s_w:
            self.rect.right = s_w

class Ball(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.Surface([30, 30])
        self.image.fill('green')
        self.rect = self.image.get_frect(center = (s_w / 2, s_h / 2))
        self.velocity = pygame.Vector2(uniform(-1, 1), uniform(-1, 1)).normalize() * 17
        self.speed = 17

    def update(self, dt):
        self.rect.center += self.velocity * self.speed * dt

        if self.rect.left <= 0 or self.rect.right >= s_w:
            self.velocity.x *= -1
            self.rect.centerx = max(min(self.rect.centerx, s_w - 1), 1)

        if self.rect.top <= 0 or self.rect.bottom >= s_h:
            self.reset()

        if pygame.sprite.spritecollide(ball, player_sprites, False):
            self.velocity.y *= -1
            self.rect.centerx += self.velocity.x * self.speed * dt
            self.speed += 1
        print(self.speed)

    def reset(self):
        self.rect.center = (s_w / 2, s_h / 2)
        self.velocity = pygame.Vector2(uniform(-1, 1), uniform(-1, 1)).normalize() * self.speed
        self.speed = 17

# sprites

all_sprites = pygame.sprite.Group()
player_sprites = pygame.sprite.Group()
ball_sprites = pygame.sprite.Group()

player1 = Player1((all_sprites, player_sprites))
player2 = Player2((all_sprites, player_sprites))
ball = Ball((all_sprites, ball_sprites))

# main

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            s_w, s_h = event.w, event.h 
            screen = pygame.display.set_mode((s_w, s_h), pygame.RESIZABLE)

    screen.fill('black')

    all_sprites.update(dt)
    all_sprites.draw(screen)

    dt = clock.tick(144) / 1000
    pygame.display.flip()

pygame.quit()
sys.exit()
