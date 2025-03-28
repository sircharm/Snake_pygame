import pygame


#Simple code for creating a pygame Snake
# I'm taking example code from the pygame documentation to start

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
running = True

while running:

  #checks if the X button was pressed and quits the main loop if so
  for event in pygame.event.get():
    if event.type == pygame.quit():
      running = False

  screen.fill("white")
  
  #game goes here
  
  pygame.display.flip()
  
  clock.tick(60) #60 FPS

pygame.quit()
