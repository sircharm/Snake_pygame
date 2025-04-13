import pygame
import random

def snake_change_direction():
    #first bool checks if the key is pressed
    #second checks if not currently going the opposite direction
    #the snake should only be able to steer left and right
    if keys[pygame.K_w] and abs(radial_choice[1][y]) != abs(radial_velocity[y]):
        return radial_choice[1]
    if keys[pygame.K_s] and abs(radial_choice[3][y]) != abs(radial_velocity[y]):
        return radial_choice[3]
    if keys[pygame.K_a] and abs(radial_choice[0][x]) != abs(radial_velocity[x]):
        return radial_choice[0]
    if keys[pygame.K_d] and abs(radial_choice[2][x]) != abs(radial_velocity[x]):
        return radial_choice[2]
    #no key press just returns the same direction it was already going
    return radial_velocity

def snake_draw(rect_list):
    # variables for height and width if I decide to change it individually later
    rect_height = square_size
    rect_width = square_size

    #puts a rect representing the head in the start of the list
    rect_list.insert(0, pygame.Rect((player_pos.x, player_pos.y, rect_width, rect_height)))

    #in the beginning, the snake's body grows out of its head
    #later, we check if the snake was already complete when the head was added
    #if it was, we need to remove the extra tail
    #sometimes the snake will grow, so this step will not be necessary
    if len(rect_list) > snake_size:
        rect_list.pop()

    for rect in rect_list:
        pygame.draw.rect(screen, snake_color, rect)

def snake_move():
    #moves the snake according to the velocity and direction
    #it checks for both axis, but in reality one of them is 0
    posx = radial_velocity[x] * dt + player_pos.x
    posy = radial_velocity[y] * dt + player_pos.y

    #this block makes sure the snake wraps around the screen if appropriate
    if posx > screen_width:
        posx = posx - screen_width
    elif posx < 0:
        posx = screen_width + posx
    if posy > screen_height:
        posy = posy - screen_height
    elif posy < 0:
        posy = screen_height + posy

    return posx, posy

#pygame setup
screen_height = 400
screen_width = 400
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
last_direction_change = pygame.time.get_ticks()
clock = pygame.time.Clock()
running = True
dt = 0

#making the snake a bunch of squares for now
square_size = 8

#base snake values
base_snake_speed = 75
base_snake_size = 40
base_change_direction_delay = 10

#basic attributes
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
snake_speed = base_snake_speed
snake_size = base_snake_size
snake_segments = []
ignored_segments = 19
snake_color = [0, 0, 0]
change_direction_delay = base_change_direction_delay
score = 0

#logic for the snake picking a side and starting to move
x = 0
y = 1
radial_choice = (
    #0 == left
    (-abs(snake_speed), 0),
    #1 == up
    (0, -abs(snake_speed)),
    #2 == right
    (snake_speed, 0),
    #3 == down
    (0, snake_speed)
)
radial_velocity = radial_choice[random.randint(0, 3)]

while running:

    #checks if the X button was pressed and quits the main loop if so
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    keys = pygame.key.get_pressed()

    for i in range(2):
        #draws the snake on screen and updates the list of segments
        snake_draw(snake_segments)

        #moves the snake
        player_pos.x, player_pos.y = snake_move()

        #checks for collisions and restes the game if there is one
        if snake_segments[0].collidelist(snake_segments[ignored_segments:]) >= 0:
            snake_speed, snake_size, snake_segments = base_snake_speed, base_snake_size, []
            radial_velocity = radial_choice[random.randint(0, 3)]
            player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
            score = 0

        #changes direction if the player pressed the movement keys
        #this algo checks if the snake didn't just change direction
        #if it's able to change direction multiple times really fast,
        #it looks really weird
        if pygame.time.get_ticks() - last_direction_change > change_direction_delay:
            last_direction_change, radial_velocity = pygame.time.get_ticks(), snake_change_direction()

    #this is needed to actually load and display the graphics
    pygame.display.flip()

    #dt is needed to ensure consistency
    dt = clock.tick(60) / 1000 #60 FPS

pygame.quit()
