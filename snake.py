import pygame
from random import randint

# Setup

pygame.init()
W_WIDTH, W_HEIGHT = 1600, 900
CELL_SIZE = 50
GRID_WIDTH = W_WIDTH // CELL_SIZE
GRID_HEIGHT = W_HEIGHT // CELL_SIZE

screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
clock = pygame.time.Clock()
running = True

# Classes

class Snake(pygame.sprite.Sprite):
    def __init__(self, color, width, height, groups):
        super().__init__(groups)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.direction = pygame.Vector2(1, 0)
        self.rect = self.image.get_rect(topleft = (W_WIDTH / 2, W_HEIGHT - 50))
        self.length = 1
        self.segments = [self.rect.copy()]
        self.new_direction = self.direction

    def update(self):
        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_w] and self.direction.y == 0:
            self.new_direction = pygame.Vector2(0, -1)
        elif keys[pygame.K_s] and self.direction.y == 0:
            self.new_direction = pygame.Vector2(0, 1)
        elif keys[pygame.K_a] and self.direction.x == 0:
            self.new_direction = pygame.Vector2(-1, 0)
        elif keys[pygame.K_d] and self.direction.x == 0:
            self.new_direction = pygame.Vector2(1, 0)

        if keys[pygame.K_UP] and self.direction.y == 0:
            self.new_direction = pygame.Vector2(0, -1)
        elif keys[pygame.K_DOWN] and self.direction.y == 0:
            self.new_direction = pygame.Vector2(0, 1)
        elif keys[pygame.K_LEFT] and self.direction.x == 0:
            self.new_direction = pygame.Vector2(-1, 0)
        elif keys[pygame.K_RIGHT] and self.direction.x == 0:
            self.new_direction = pygame.Vector2(1, 0)
        
        self.direction = self.new_direction
        
        new_position = self.rect.topleft + self.direction * CELL_SIZE

        if new_position.x < 0 or new_position.x >= W_WIDTH or new_position.y < 0 or new_position.y >= W_HEIGHT:
            return True

        self.rect.topleft = new_position

        self.segments.insert(0, self.rect.copy())
        if len(self.segments) > self.length:
            self.segments.pop()

        for segment in self.segments[1:]:
            if self.rect.colliderect(segment):
                return True

        return False

    def grow(self):
        self.length += 1

    def draw(self, screen):
        for segment in self.segments:
            screen.blit(self.image, segment.topleft)

class Apple(pygame.sprite.Sprite):
    def __init__(self, color, width, height, groups):
        super().__init__(groups)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.respawn()

    def respawn(self):
        valid_position = False
        while not valid_position:
            self.rect.topleft = (randint(0, GRID_WIDTH - 1) * CELL_SIZE, randint(0, GRID_HEIGHT - 1) * CELL_SIZE)
            if all(not self.rect.colliderect(segment) for segment in snake.segments):
                valid_position = True
            

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text 
        self.font = pygame.font.Font(None, 50)

    def draw(self, screen):
        pygame.draw.rect(screen, 'white', self.rect)
        text_surface = self.font.render(self.text, True, 'black')
        text_rect = text_surface.get_rect(center = self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def click(self, pos):
        return self.rect.collidepoint(pos)
    
class Score:
    def __init__(self, x, y):
        self.score = 0
        self.font = pygame.font.Font(None, 25)
        self.x = x
        self.y = y 

    def increment(self):
        self.score += 1

    def draw(self, screen):
        score_surface = self.font.render(f'Score: {self.score}', True, 'White')
        screen.blit(score_surface, (self.x, self.y))

# Sprites

def reset_game():
    global all_sprites, snake, apple, score
    all_sprites = pygame.sprite.Group()
    snake = Snake('white', CELL_SIZE, CELL_SIZE, all_sprites)
    apple = Apple('red', CELL_SIZE, CELL_SIZE, all_sprites)
    score = Score(10, 10)

reset_game()

button = Button(W_WIDTH / 2 - 100, W_HEIGHT / 2, 200, 100, 'Play!')

# Main loop

game_started = False
game_over = False

while running:
    dt = clock.tick(10) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not game_started:
                game_started = True
            elif game_over and button.click(event.pos):
                reset_game()
                game_over = False
                game_started = True
        
    screen.fill('black')
    if game_started and not game_over:
        game_over = snake.update()
        
        if not game_over and pygame.sprite.collide_rect(snake, apple):
            snake.grow()
            apple.respawn()
            score.increment()

        all_sprites.draw(screen)
        snake.draw(screen)
        score.draw(screen)

    elif game_over:
        game_over_surface = score.font.render(f"Game Over! Score: {score.score}", True, 'White')
        screen.blit(game_over_surface, (W_WIDTH // 2 - 100, W_HEIGHT // 2 - 100))
        button.draw(screen)

    else:
        button.draw(screen)
    
    pygame.display.flip()

pygame.quit()
