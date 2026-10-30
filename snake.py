from objects import Snake
from objects import AppleGroup
from scenes import game_over

import pygame
#THERE AREN'T ANY FUNCTION/CLASS DECLARATIONS IN THIS SCRIPT, SO I WON'T USE A MAIN FUNCTION
pygame.init()

STANDARD_FONT = pygame.font.SysFont("Arial", 36)

GAME_AREA_HEIGHT = 400
GAME_AREA_WIDTH = 400
BACKGROUND_COLOR = (250, 250, 250)

SCORE_DISPLAY_SIZE = 50
SCORE_DISPLAY_COLOR = pygame.Color(55, 200, 55)
SCORE_DISPLAY = pygame.Rect((0, 0, GAME_AREA_WIDTH, SCORE_DISPLAY_SIZE))

SCORE_TEXT_COLOR = pygame.Color(30, 30, 30)
SCORE_TEXT_POSITION = (3, 0)

TOTAL_SCREEN_HEIGHT = GAME_AREA_HEIGHT + SCORE_DISPLAY_SIZE
TOTAL_SCREEN_WIDTH = GAME_AREA_WIDTH
GAME_AREA_CENTER = pygame.Vector2(TOTAL_SCREEN_WIDTH / 2, TOTAL_SCREEN_HEIGHT / 2)

BASE_DIFFICULTY = 1.0
RAISE_DIFFICULTY_TIME = 3000
ADDED_DIFFICULTY = 0.02

BASE_SQUARE_SIZE = 8
COLLISION_IGNORED_SEGMENTS = 15
REFRESH_RATE = 2

screen = pygame.display.set_mode((TOTAL_SCREEN_WIDTH, TOTAL_SCREEN_HEIGHT))

clock = pygame.time.Clock()
last_direction_change = pygame.time.get_ticks()
difficulty_timer = pygame.time.get_ticks()
dt = clock.tick(60) / 1000

difficulty = BASE_DIFFICULTY
Player = Snake(GAME_AREA_CENTER, BASE_SQUARE_SIZE, difficulty)
Apples = AppleGroup(BASE_SQUARE_SIZE)

running = True
while running:

    #checks if the X button was pressed and quits the main loop if so
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((BACKGROUND_COLOR))
    #draw the display
    pygame.draw.rect(screen, SCORE_DISPLAY_COLOR, SCORE_DISPLAY)

    keys = pygame.key.get_pressed()

    Apples.draw(screen)

    for i in range(REFRESH_RATE):
        #draws the snake on screen and updates the list of segments
        Player.snake_draw(screen)

        Player.snake_move(dt, GAME_AREA_WIDTH, GAME_AREA_HEIGHT, SCORE_DISPLAY_SIZE)

        #checks for deadly collisions and resets the game if there is one
        if Player.segments[0].collidelist(Player.segments[COLLISION_IGNORED_SEGMENTS:]) >= 0:
            if Player.score > 0:
                running = game_over(screen, Player.score, STANDARD_FONT)
            difficulty = BASE_DIFFICULTY
            Player = Snake(GAME_AREA_CENTER, BASE_SQUARE_SIZE, difficulty)
            Apples = AppleGroup(BASE_SQUARE_SIZE)

        #checks for collision with apples
        Player.apple_consume(Apples.apple_list, difficulty)

    Player.snake_change_direction(keys)

    if pygame.time.get_ticks() - difficulty_timer > RAISE_DIFFICULTY_TIME:
        difficulty += ADDED_DIFFICULTY
        difficulty_timer = pygame.time.get_ticks()

    Apples.spawn(Player.segments, GAME_AREA_WIDTH, GAME_AREA_HEIGHT, SCORE_DISPLAY_SIZE)

    # Render the score text
    score_text = STANDARD_FONT.render(f"Score: {Player.score}", True, SCORE_TEXT_COLOR)
    screen.blit(score_text, SCORE_TEXT_POSITION)

    pygame.display.flip()

    dt = clock.tick(60) / 1000 #60 FPS

pygame.quit()
