I'll be journaling my learning experience on this file for future reference. 

At first, I dealt with a lot of problems during the setup. Even installing the dependencies wasn't as straight forward as I thought it would be. But I did learn a lot of valuable things doing it.
In the beginning, I chose a template Python workflow on github and learned it would already do a lot for me. I just needed to create a requirements file for the dependencies I'd use.
After a few attempts, I managed to get it right, but my workflow was still raising errors because pytest wasn't finding any tests to run. After a few tries, I solved that as well.
Now, with a workflow setup for tests, I don't really have tests I want to run with it yet, so I modified the workflow to only be triggered manually and not after each push.

But to test my code for now, I'll be testing mostly visual things, which isn't possible with pytest. Since at first I was also having problems with the dependecies on codespaces, I decided to run the tests on my computer from IDLE.
Problem was, I had another python version on my computer that I forgot I had installed. That made it so that every time I pip installed pygame, it was only installed in the other version of python I was not using.
I decided to uninstall that version, reinstall pip on the correct version and put pip back on PATH. From that point, I was finally able to see the result of the simple code I copied from the pygame documentation that draws a circle
and makes it move with WASD.

**I lost A LOT of time over this, so I finally understood why you shouldn't install multiple versions of python in your PC. Next time, I'll be sure to create a virtual environment to run a different vesion of python**

Now I just need to configure the codespaces environment and I'll be all set to start actually working on the coding part of the project.
