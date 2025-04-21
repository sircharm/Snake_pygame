import pygame
import random

#currently the player class
class Snake:
    def __init__(self, position_x, position_y, speed, size, square_size):
        self.square_size = square_size
        self.position_x = position_x
        self.position_y = position_y
        self.score = 0

        self.speed = speed
        self.size = size
        self.color = pygame.Color(0, 0, 0)
        self.segments = []

        # logic for the snake picking a side and starting to move
        self.speed_update()
        self.radial_velocity = self.radial_choice[random.randint(0, 3)]
        self.last_direction_change = pygame.time.get_ticks()

    def snake_change_direction(self, keys):
        x = 0
        y = 1
        # changes direction if the player pressed the movement keys
        # this algo checks if the snake didn't just change direction
        # if it's able to change direction multiple times really fast,
        # it looks really weird
        if pygame.time.get_ticks() - self.last_direction_change > self.change_direction_delay:
            # first bool checks if the key is pressed
            # second checks if not currently going the opposite direction
            # the snake should only be able to steer left and right
            self.last_direction_change = pygame.time.get_ticks()
            if keys[pygame.K_w] and abs(self.radial_choice[1][y]) != abs(self.radial_velocity[y]):
                self.radial_velocity = self.radial_choice[1]
                return
            if keys[pygame.K_s] and abs(self.radial_choice[3][y]) != abs(self.radial_velocity[y]):
                self.radial_velocity = self.radial_choice[3]
                return
            if keys[pygame.K_a] and abs(self.radial_choice[0][x]) != abs(self.radial_velocity[x]):
                self.radial_velocity = self.radial_choice[0]
                return
            if keys[pygame.K_d] and abs(self.radial_choice[2][x]) != abs(self.radial_velocity[x]):
                self.radial_velocity = self.radial_choice[2]
                return

    def snake_draw(self, screen):
        # variables for height and width if I decide to change it individually later
        rect_height = self.square_size
        rect_width = self.square_size

        # puts a rect representing the head in the start of the list
        self.segments.insert(0, pygame.Rect((self.position_x, self.position_y, rect_width, rect_height)))

        #in the beginning, the snake's body grows out of its head
        #later, we check if the snake was already complete when the head was added
        #if it was, we need to remove the extra tail
        #sometimes the snake will grow, so this step will not be necessary
        if len(self.segments) > self.size:
            self.segments.pop()

        for rect in self.segments:
            pygame.draw.rect(screen, self.color, rect)

    def snake_move(self, dt, screen_width, screen_height, display_size):
        x = 0
        y = 1

        # moves the snake according to the velocity and direction
        # it checks for both axis, but in reality one of them is 0
        posx = self.radial_velocity[x] * dt + self.position_x
        posy = self.radial_velocity[y] * dt + self.position_y

        # this block makes sure the snake wraps around the screen if appropriate
        if posx > screen_width:
            posx = posx - screen_width
        elif posx < 0:
            posx = screen_width + posx
        if posy > screen_height + display_size:
            posy = posy - screen_height
        elif posy < 0 + display_size:
            posy = screen_height + posy

        self.position_x = posx
        self.position_y = posy

    def apple_consume(self, apple_list, difficulty):
        for index, apple in enumerate(apple_list):
            if self.segments[0].colliderect(apple):

                self.score += round(10 * difficulty)
                self.speed += 1 * difficulty
                self.speed_update()
                self.size += round(2 * difficulty)

                apple_list.pop(index)
                break

    def speed_update(self):
        self.radial_choice = (
            # 0 == left
            (-abs(self.speed), 0),
            # 1 == up
            (0, -abs(self.speed)),
            # 2 == right
            (self.speed, 0),
            # 3 == down
            (0, self.speed)
        )

        self.change_direction_delay = 100 - 26 - round((self.speed * 0.3))
        if self.change_direction_delay < 10:
            self.change_direction_delay = 10