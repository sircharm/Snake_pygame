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
## Starting to study (march 29 - )

Before I dive into coding, I decided to search a little bit more about pygame. Right away, I found a Youtube video with some interesting information:

[5 Things I Wish I Knew Before Making a Game with Pygame | DevLog](https://www.youtube.com/watch?v=6iUYLqIrV7s)
  - Apparently, GUI with pygame is a pain to code.
  - The author of the video makes a point that **pygame is NOT a game engine**, but a collection of libraries
  - Graphics in pygame require specific coordinates to be created, which makes it harder to make sprites, etc.
    - This shouldn't be a problem in my project, as all the graphics should be really simple.
  - I should keep my game as modular as possible, making individuals functions for scenes and mechanics
  - It was also recommended to use either VS Code or Pycharm to code. I'll look into Pycharm.
