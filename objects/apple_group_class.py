import pygame
import random


class AppleGroup:
    def __init__(self, square_size):
        self.apple_list = []
        self.apple_timer = pygame.time.get_ticks()
        self.apple_spawn_time = 5000
        self.square_size = square_size + 2
        self.apple_color = (255, 0, 0)

    def spawn(self, collision_list, screen_width, screen_height, display_size):
        if pygame.time.get_ticks() - self.apple_timer > self.apple_spawn_time:
            while True:
                temp_apple = pygame.Rect((random.randint(10, screen_width - 10),
                                         random.randint(10 + display_size, screen_height + display_size - 10),
                                         self.square_size, self.square_size))

                if temp_apple.collidelist(collision_list + self.apple_list) == -1:
                    break

            self.apple_list.append(temp_apple)

            self.apple_timer = pygame.time.get_ticks()

    def draw(self, screen):
        for apple in self.apple_list:
            pygame.draw.rect(screen, self.apple_color, apple)