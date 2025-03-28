import pygame


#Simple code for creating a pygame Snake
# I'm taking example code from the pygame documentation to start

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:

  #checks if the X button was pressed and quits the main loop if so
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

  screen.fill("white")
  
  #game goes here
  pygame.draw.circle(screen, "black", player_pos, 40)

  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
      player_pos.y -= 300 * dt
  if keys[pygame.K_s]:
      player_pos.y += 300 * dt
  if keys[pygame.K_a]:
      player_pos.x -= 300 * dt
  if keys[pygame.K_d]:
      player_pos.x += 300 * dt
  
  pygame.display.flip()
  
  dt = clock.tick(60) / 1000 #60 FPS

pygame.quit()
