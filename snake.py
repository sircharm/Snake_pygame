from objects import *

import pygame

#pygame setup
screen_height = 400
screen_width = 400
display_size = 50
pygame.init()
font = pygame.font.SysFont("Arial", 36)
initial_player_pos = pygame.Vector2(screen_width / 2, ((screen_height + (display_size * 2)) / 2))
screen = pygame.display.set_mode((screen_width, screen_height + display_size))
last_direction_change = pygame.time.get_ticks()
clock = pygame.time.Clock()
running = True
dt = 0

#display rect
display = pygame.Rect((0, 0, screen_width, display_size))
display_color = pygame.Color(55, 200, 55)

#difficulty variables
base_difficulty = 1.0
difficulty = base_difficulty
difficulty_timer = pygame.time.get_ticks()
raise_difficult_time = 3000

#base snake values
base_snake_speed = 80 * difficulty
base_snake_size = 40 * difficulty

#basic attributes
square_size = 8
ignored_segments = 15

#initialize the player and the apple group
Player = Snake(initial_player_pos.x, initial_player_pos.y, base_snake_speed, base_snake_size, square_size)
Apples = AppleGroup(square_size)

while running:

    #checks if the X button was pressed and quits the main loop if so
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((250, 250, 250))
    #draw the display
    pygame.draw.rect(screen, display_color, display)


    keys = pygame.key.get_pressed()

    Apples.draw(screen)

    for i in range(2):
        #draws the snake on screen and updates the list of segments
        Player.snake_draw(screen)

        #moves the snake
        Player.snake_move(dt, screen_width, screen_height, display_size)

        #checks for collisions and restes the game if there is one
        if Player.segments[0].collidelist(Player.segments[ignored_segments:]) >= 0:
            Player = Snake(initial_player_pos.x, initial_player_pos.y, base_snake_speed, base_snake_size, square_size)
            Apples = AppleGroup(square_size)
            difficulty = base_difficulty

        #checks for collision with appleswa
        Player.apple_consume(Apples.apple_list, difficulty)

    # change direction
    Player.snake_change_direction(keys)

    if pygame.time.get_ticks() - difficulty_timer > raise_difficult_time:
        difficulty += 0.02
        difficulty_timer = pygame.time.get_ticks()

    #spawn apples
    Apples.spawn(Player.segments, screen_width, screen_height, display_size)

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
