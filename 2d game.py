
#2d game 
import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Shooting Game 🔫")

# Colors
WHITE = (255, 255, 255)
RED = (255, 1, 0)
BLUE = (0, 1, 255)

# Player settings
player_size = 45
player_x = WIDTH // 2
player_y = HEIGHT - player_size - 10
player_speed = 8

# Bullet settings
bullets = []
bullet_speed = 10

# Enemy settings
enemies = []
enemy_size = 45
enemy_speed = 5

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont(None, 40)

# Score
score = 0

# Game loop
running = True
while running:
    clock.tick(80)  # 60 FPS
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        bullets.append([player_x + player_size//2 - 5, player_y])

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    # Move and draw bullets
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        pygame.draw.rect(screen, RED, (bullet[0], bullet[1], 10, 20))
        if bullet[1] < 0:
            bullets.remove(bullet)

    # Spawn enemies
    if random.randint(1, 50) == 1:
        enemy_x = random.randint(0, WIDTH - enemy_size)
        enemies.append([enemy_x, 0])

    # Move and draw enemies
    for enemy in enemies[:]:
        enemy[1] += enemy_speed
        pygame.draw.rect(screen, (0, 255, 0), (enemy[0], enemy[1], enemy_size, enemy_size))

        # Collision with player
        if (player_x < enemy[0] + enemy_size and
            player_x + player_size > enemy[0] and
            player_y < enemy[1] + enemy_size and
            player_y + player_size > enemy[1]):
            print("Game Over!")
            pygame.quit()
            sys.exit()

        # Enemy off screen
        if enemy[1] > HEIGHT:
            if enemy in enemies:
                enemies.remove(enemy)

        # Bullet collision
        for bullet in bullets[:]:
            if (bullet[0] < enemy[0] + enemy_size and
                bullet[0] + 10 > enemy[0] and
                bullet[1] < enemy[1] + enemy_size and
                bullet[1] + 20 > enemy[1]):
                if bullet in bullets:
                    bullets.remove(bullet)
                if enemy in enemies:
                    enemies.remove(enemy)
                score += 1

    # Draw score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
