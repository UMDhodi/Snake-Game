import pygame
import random

# Initialize the game
pygame.init()

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the width and height of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Set the clock for the game
clock = pygame.time.Clock()

# Set the font for the game
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

# Define the snake's size and speed
snake_block = 20
snake_speed = 6

# Define the functions for displaying the snake and the score
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])

def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, WHITE)
    screen.blit(value, [10, 10])

# Define the main game loop
def game_loop():
    game_over = False
    game_close = False

    # Initialize the starting position of the snake
    x1 = screen_width / 2
    y1 = screen_height / 2

    # Initialize the change in position of the snake
    x1_change = 0
    y1_change = 0

    # Create an empty list to store the snake's body
    snake_list = []
    length_of_snake = 1

    # Generate the initial position of the food
    foodx = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, RED)
            message_width = message.get_width()
            message_height = message.get_height()
            screen.blit(message, [screen_width / 6, screen_height / 3])
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check if the snake hits the boundaries of the screen
        if x1 >= screen_width - snake_block or x1 < 0 or y1 >= screen_height - snake_block or y1 < 0:
            game_close = True

        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if the snake hits itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Display the snake and the score
        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        # Check if the snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0
            length_of_snake += 1

        # Set the speed of the game
        clock.tick(snake_speed)

    pygame.quit()

# Run the game loop
game_loop()
