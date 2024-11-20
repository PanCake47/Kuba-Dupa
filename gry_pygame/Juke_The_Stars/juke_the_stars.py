import pygame
import time 
import random
pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kuba Dupa Projects")

BG = pygame.transform.scale(pygame.image.load('BG.png'), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60 
PLAYER_VELOCITY = 5

STAR_WIDTH = 15
STAR_HEIGHT = 15
STAR_VELOCITY = 5

FONT = pygame.font.SysFont('comicsans', 30)
high_score = 0  

STAR_IMAGE = pygame.image.load('star.png')
STAR_IMAGE = pygame.transform.scale(STAR_IMAGE, (STAR_WIDTH, STAR_HEIGHT))

PLAYER_IMAGE = pygame.image.load('player.png')
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))

isJump = False
jumpCount = 10

def draw(player, elapsed_time, stars, high_score):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f'Time: {round(elapsed_time)}s', 1, 'white')
    WIN.blit(time_text, (10, 10))
    
    high_score_text = FONT.render(f'High Score: {round(high_score)}s', 1, 'white')
    WIN.blit(high_score_text, (10, 40))
    
    WIN.blit(PLAYER_IMAGE, (player.x, player.y))

    for star in stars:
        WIN.blit(STAR_IMAGE, (star.x, star.y))
    
    pygame.display.update()

def draw_end_screen():
    WIN.blit(BG, (0, 0))
    lost_text = FONT.render('You Lost!', 1, 'white')
    WIN.blit(lost_text, (WIDTH / 2 - lost_text.get_width() / 2, HEIGHT / 2 - lost_text.get_height() / 2))
    
    button_text = FONT.render('Play Again', 1, 'white')
    button_rect = pygame.Rect(WIDTH / 2 - button_text.get_width() / 2, HEIGHT / 2 + 50, button_text.get_width(), button_text.get_height())
    pygame.draw.rect(WIN, 'blue', button_rect)
    WIN.blit(button_text, (button_rect.x, button_rect.y))
    
    pygame.display.update()
    return button_rect

def main():
    global jumpCount
    global isJump
    global high_score  
    
    run = True
    while run:
        player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
        clock = pygame.time.Clock()
        start_time = time.time()
        elapsed_time = 0
        star_add_increment = 2000
        star_count = 0
        stars = []
        hit = False
        
        while not hit:
            star_count += clock.tick(60)
            elapsed_time = time.time() - start_time

            if star_count >= star_add_increment:
                for _ in range(3):
                    star_x = random.randint(0, WIDTH - STAR_WIDTH)
                    star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                    stars.append(star)
                
                star_add_increment = max(200, star_add_increment - 50)
                star_count = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and player.x - PLAYER_VELOCITY >= 0:
                player.x -= PLAYER_VELOCITY   
            if keys[pygame.K_d] and player.x + PLAYER_VELOCITY + player.width <= WIDTH:
                player.x += PLAYER_VELOCITY
            if not(isJump):
                if keys[pygame.K_SPACE]:
                    isJump = True
            else:
                if jumpCount >= -10:
                    player.y -= (jumpCount * abs(jumpCount)) 
                    jumpCount -= 1
                else: 
                    jumpCount = 10         
                    isJump = False
     
            for star in stars[:]:
                star.y += STAR_VELOCITY
                if star.y > HEIGHT:
                    stars.remove(star)
                elif star.y + star.height >= player.y and star.colliderect(player):
                    stars.remove(star)
                    hit = True
                    break

            if hit:
                if elapsed_time > high_score:
                    high_score = elapsed_time  
                break

            draw(player, elapsed_time, stars, high_score)

        button_rect = draw_end_screen()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        hit = False
                        break
            if not hit:
                break
            pygame.time.delay(100)
            

if __name__ == '__main__':
    main()

    
