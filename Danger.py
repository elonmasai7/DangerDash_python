import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 20
player_speed = 5

# Obstacles
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacle_frequency = 25  # Lower values increase obstacle frequency

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Danger Dash")
clock = pygame.time.Clock()

# Function to draw the player
def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, player_width, player_height])

# Function to draw obstacles
def draw_obstacle(x, y):
    pygame.draw.rect(screen, RED, [x, y, obstacle_width, obstacle_height])

# Main game loop
def game_loop(player_x):
    obstacles = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed

        # Create obstacles
        if random.randint(1, obstacle_frequency) == 1:
            obstacle_x = random.randint(0, WIDTH - obstacle_width)
            obstacle_y = -obstacle_height
            obstacles.append([obstacle_x, obstacle_y])

        # Update obstacle positions
        for obstacle in obstacles:
            obstacle[1] += obstacle_speed

        # Remove off-screen obstacles
        obstacles = [obstacle for obstacle in obstacles if obstacle[1] < HEIGHT]

        # Collision detection
        for obstacle in obstacles:
            if (
                player_x < obstacle[0] + obstacle_width
                and player_x + player_width > obstacle[0]
                and player_y < obstacle[1] + obstacle_height
                and player_y + player_height > obstacle[1]
            ):
                print("Game Over!")
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the player
        draw_player(player_x, player_y)

        # Draw obstacles
        for obstacle in obstacles:
            draw_obstacle(obstacle[0], obstacle[1])

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

# Run the game loop
game_loop(player_x)
