I'll be journaling my learning experience on this file for future reference. The most important points will be made into list so they're easier to localize in the text.

## Initial setup difficulties (march 28 - march 29)

At first, I dealt with a lot of problems during the setup. Even installing the dependencies wasn't as straight forward as I thought it would be. But I did learn a lot of valuable things doing it.
In the beginning, I chose a template Python workflow on github and learned it would already do a lot for me. I just needed to create a requirements file for the dependencies I'd use.
After a few attempts, I managed to get it right, but my workflow was still raising errors because pytest wasn't finding any tests to run. After a few tries, I solved that as well.
Now, with a workflow setup for tests, I don't really have tests I want to run with it yet, so I modified the workflow to only be triggered manually and not after each push.

For now, I'll be testing mostly visual things, which isn't possible with pytest. Since at first I was also having problems with the dependecies on codespaces, I decided to run the tests on my computer from IDLE.
Problem was, I had another python version on my computer that I forgot I had installed. That made it so that every time I pip installed pygame, it was only installed in the other version of python I was not using.
I decided to uninstall that version, reinstall pip on the correct version and put pip back on PATH. From that point, I was finally able to see the result of the simple code I copied from the pygame documentation that draws a circle
and makes it move with WASD.

**I lost A LOT of time over this**, so I finally understood:
  - I shouldn't install multiple versions of python on my PC.
  - If I need to use a different python version, I should use a virtual environment for that

I think I won't really be using codespaces a lot for this project, since it requires some extra steps to display graphics and I can just do it locally.
## Starting to study (march 29)

Before I dive into coding, I decided to search a little bit more about pygame. Right away, I found a Youtube video with some interesting information:

[5 Things I Wish I Knew Before Making a Game with Pygame | DevLog](https://www.youtube.com/watch?v=6iUYLqIrV7s)
  - Apparently, GUI with pygame is a pain to code.
  - The author of the video makes a point that **pygame is NOT a game engine**, but a collection of libraries
  - Graphics in pygame require specific coordinates to be created, which makes it harder to make sprites, etc.
    - This shouldn't be a problem in my project, as all the graphics should be really simple.
  - I should keep my game as modular as possible, making individuals functions for scenes and mechanics
  - It was also recommended to use either VS Code or Pycharm to code. I'll look into Pycharm.

## Initial steps (april 12 - april 13)

With a basic example code from pygame's docs to work from, I started coding. The code created a white screen, a black circle and allowed the player to move the circle with wasd. At first, I made the circle pick a random direction and start moving. The snake moves at all times and now the player can steer it left and right.

The next thing I did was changing the circle into a list of rectangles that were drawn on screen once every loop. I did this by creating a new rectangle after everytime the snake moves, which is it's head. The other rects are the body. This means the snake is constantly trying to grow over the limit, which means I also have to pop the last item in the list when appropriate. It worked well enough for now and looks good visually, but I'll probably have to change this behavior because it makes the rects intersect a lot. When dealing with collisions, I'll ignore some of the rects in the list. This shouldn't be too problematic since the snake's head can't physically collide with rects that are straight behind itself anyway. For learning about collisions, I searching for a few more Youtube videos:

[Get Started in Pygame in 10 minutes!](https://www.youtube.com/watch?v=y9VG3Pztok8)

[Pygame Event Handler Explained](https://www.youtube.com/watch?v=KR2zP6yuWAs&t=4s)
  - Two videos from the same author. He talked mostly about simple stuff I already knew from the example code, but the explanation about the event handler was very important.
  - I learned that pygame captures a bunch of useful stuff automatically that I can use, like mouse position and key presses, for example.
  - I could maybe use that to make a simple GUI with a pause button. I could I also make a main menu for selecting the difficulty, but I think I'll do that when the project is almost done.

[Collisions in Pygame - Beginner Tutorial](https://www.youtube.com/watch?v=BHr9jxKithk)
  - In this video, I learned that collision detection is built into pygame. There are functions specifically to check for the collision of rects and lists of rects, which I think I'll be using the most.
  - After watching it, I was able to introduce collision detection into the game. For now, I'm using it to reset some variables, which effectively resets the game.

This was all I got done this weekend. The obvious next steps is introducing apples for the snake to eat, which will raise it's size, speed and give points. I also needs to display the score somehow. I'll probably need to grow the scree a little to make room for it.

## Implementing random generation of apples (april 18)

I created the logic for spawning apples, checking for collisions with them for updating the score and raising the size and speeed of the snake. At first I made the score be printed to the terminal just to see if it's working. The code also checks for collision between the newly-created apple with the snake before creating it because spawning an apple inside the snake would be frustrating for the player. If I add more obstacles, I should probably include them in this check as well.

## Reorganizing the code (april 21)

The logic has been working fine so far, but I now realized the code isn't very well organized. I thought about how I planned to introduce other snakes as enemies in the game at some point and how that would be way easier if I was using OOP, since NPC snakes wouldn't be that different from the main one. The functions I wrote will work better as methods anyway since I'm dealing with return values unecessarily. I already have a vague idea of how I'm going to go about this, but I think it's best to study a little first:

[5 Tips To Organize Python Code](https://www.youtube.com/watch?v=e9yMYdnSlUA&t=1s)

[Python OOP Tutorial 1: Classes and Instances](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)

[Python OOP Tutorial 2: Class Variables](https://www.youtube.com/watch?v=BJ-VvGyQxho)

With the information of those videos in mind, I was able to create a new folder with separate python files for a Snake class and an AppleGroup class. The code is now much more organized and modular. When I have multiple snakes implemented, I plan on including all the snakes in a list so I can run a for loop for each method that needs to be executed.

  - I also made a score display for the game
