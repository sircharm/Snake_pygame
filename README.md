I'm starting a very simple project in order to learn the ropes of github. 
I never used pygame either, but I think it'll be a simple task given my current level of knowledge.
I'll not ctrl+c, ctrl+v any code that wasn't written by myself for this project.
If at some point I need to copy code from somewhere, I'll at least type all the code myself.
This way, I'll have the opportunity to get used to the synthax and the logic of the copied code.
I'll leave comments on the parts of the code I didn't write it myself, so it'll be very clear.
I won't leave a comment if I'm simply consulting the parameters/synthax of a function I'm already familiar with.

This is what the project absolutely requires:
  *Visuals for the snake and the apples
    >Apples give points and make the snake grow
  *Persistent score implement through the sqlite3 module
    >I want to use this module to learn more about it and sql in general
  *Collision detection
  *Game Over screen where you can type your name to register
    >The score should be compared with the previous ones and a highscore list should be displayed
    >The score should be shown in it's correct place on the list so the player can decide if it's even worth saving
    >The overall position of the score between all registered scores should be displayed, even if outside the highscores table. (e.g. 1023th place)
  *Difficulty setting.
    >The player selects the initial difficult and it gets harder as time goes on
    >A higher difficulty makes the snake go faster and apples give more points
    >Option to have a barrier surrounding the map or not
    >If there's no barrier, the player should be able to go through one side and come out the opposite side

What I *might* implement further:
  *Random obstacles.
  *Other snakes controlled by the CPU that compete with you
    >The player needs to make it collide his/hers own snake you to kill it
    >The other snakes act as normal obstacles if you collide head-first into them
    >They can steal your apples
  *A very simple bare-bones story and a way to beat the game
  *Achievements
  *If I think of anything else, I'll add it here along with the date I thought of it

_Time Frame_
This is a simple project, but it is not my priority right now. I'm starting on the 28th of march 2025.
I intend to finish all the essential parts by the end of next month.
I might work on it further to implement optional stuff.
    
