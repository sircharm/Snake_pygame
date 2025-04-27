# Snake with pygame and sqlite3

I'm starting a very simple project in order to learn the ropes of github. I never used pygame either, but I think it'll be a simple task given my current level of knowledge.

I wrote all the code myself, except for a few lines of code I took from Grok 3. Most of the time I needed help with some code, simply consulting official documentation sufficed.

I left comments on the parts of the code I didn't write myself, so it is very clear.


### This is what the project absolutely requires:
**The parts I still need to implement are in bold**
  - Visuals for the snake and the apples
    - Apples give points and make the snake grow
    
  - Persistent score implemented through the sqlite3 module
    - I want to use this module to learn more about it and sql in general
    
  - Collision detection
  - Game Over screen where you can type your name to register
    - The score should be compared with the previous ones and a highscore list should be displayed
    - The score should be shown in its correct place on the list so the player can decide if it's even worth saving
    - The overall position of the score between all registered scores should be displayed, even if outside the highscores table. (e.g. 1023th place)
  - Difficulty setting.
    - **The player selects the initial difficult** and it gets harder as time goes on
    - A higher difficulty makes the snake go faster and apples give more points
    - **Option to have a barrier surrounding the map or not**
    - If there's no barrier, the player should be able to go through one side and come out the opposite side

## What I *might* implement further:
  - Random obstacles.
  - Other snakes controlled by the CPU that compete with you
    - The player needs to make it collide his/hers own snake you to kill it
    - The other snakes act as normal obstacles if you collide head-first into them
    - They can steal your apples
  - A very simple bare-bones story and a way to beat the game
  - Achievements

## _Time Frame_
Currently, the basics of the project are finished. I still have some stuff to finish, but I don't really have a deadline for any of it.
    
