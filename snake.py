from objects import Snake
from objects import AppleGroup
from scenes import game_over

import pygame

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 400

DISPLAY_SIZE = 50
DISPLAY_COLOR = pygame.Color(55, 200, 55)

BASE_DIFFICULTY = 1.0
RAISE_DIFFICULTY_TIME = 3000

BASE_SQUARE_SIZE = 8
COLLISION_IGNORED_SEGMENTS = 15

INITIAL_PLAYER_POS = pygame.Vector2(SCREEN_WIDTH / 2, ((SCREEN_HEIGHT + (DISPLAY_SIZE)) / 2))

#pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + DISPLAY_SIZE))
font = pygame.font.SysFont("Arial", 36)
clock = pygame.time.Clock()
running = True

last_direction_change = pygame.time.get_ticks()
dt = 0

#display rect
display = pygame.Rect((0, 0, SCREEN_WIDTH, DISPLAY_SIZE))

#difficulty variables
difficulty = BASE_DIFFICULTY
difficulty_timer = pygame.time.get_ticks()

#base snake values
base_snake_speed = 80 * difficulty
base_snake_size = 40 * difficulty

#initialize the player and the apple group
Player = Snake(INITIAL_PLAYER_POS, base_snake_speed, base_snake_size, BASE_SQUARE_SIZE)
Apples = AppleGroup(BASE_SQUARE_SIZE)

while running:

    #checks if the X button was pressed and quits the main loop if so
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((250, 250, 250))
    #draw the display
    pygame.draw.rect(screen, DISPLAY_COLOR, display)


    keys = pygame.key.get_pressed()

    Apples.draw(screen)

    for i in range(2):
        #draws the snake on screen and updates the list of segments
        Player.snake_draw(screen)

        #moves the snake
        Player.snake_move(dt, SCREEN_WIDTH, SCREEN_HEIGHT, DISPLAY_SIZE)

        #checks for collisions and restes the game if there is one
        if Player.segments[0].collidelist(Player.segments[COLLISION_IGNORED_SEGMENTS:]) >= 0:
            if Player.score > 0:
                running = game_over(screen, Player.score, font)
            Player = Snake(INITIAL_PLAYER_POS, base_snake_speed, base_snake_size, BASE_SQUARE_SIZE)
            Apples = AppleGroup(BASE_SQUARE_SIZE)
            difficulty = BASE_DIFFICULTY

        #checks for collision with appleswa
        Player.apple_consume(Apples.apple_list, difficulty)

    # change direction
    Player.snake_change_direction(keys)

    if pygame.time.get_ticks() - difficulty_timer > RAISE_DIFFICULTY_TIME:
        difficulty += 0.02
        difficulty_timer = pygame.time.get_ticks()

    #spawn apples
    Apples.spawn(Player.segments, SCREEN_WIDTH, SCREEN_HEIGHT, DISPLAY_SIZE)

    # Logic for displaying the text copied from Grok 3
    # Render the score text
    score_text = font.render(f"Score: {Player.score}", True, (30, 30, 30))
    # Blit the text to the screen
    screen.blit(score_text, (5, 5))

    #this is needed to actually load and display the graphics
    pygame.display.flip()
    #dt is needed to ensure consistency
    dt = clock.tick(60) / 1000 #60 FPS

pygame.quit()
