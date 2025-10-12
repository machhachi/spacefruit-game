# spacefruit-game
Explore space and collect fruit in this little 2D gravity simulator for a CMU 15-112 term project.
Watch my trailer here, at https://drive.google.com/file/d/1eN9BEnRg4FzKXTg-9le0OG85pc71hbK0/view?usp=sharing

ACCREDITATION
Background music of the Spacefruit trailer is entirely 'Selfless' by Eleven Tales. I take no credit for the music.
I borrowed a piece of programming for line segment intersection from this URL: https://www.geeksforgeeks.org/dsa/check-if-two-given-line-segments-intersect/
Thank you to professor Michael Taylor for the time in his course! I couldn't have done it without his lectures or our wonderful conversations.

NOTES FOR RUNNING PROJECT
All files required to run the project are stored in spacefruit-game/MAIN GAME. 
- Open main.py in VSCode (Or another editor, though I've only tested on this one)
- Run file
That should be it!

NOTES FOR SUPPLEMENTAL MATERIALS
I have several supplemental programs, utilies I used during project development, that I want to preserve alongside the full game.
They are stored in spacefruit-game/SUPPLEMENTAL MATERIAL, which itself contains a .txt file describing the individual programs.
Critical note: They all require the CMU Grahpics package to run, which is accomplished by having the cmu_graphics folder stored in the same folder as the programs.
I have elected to not store a second copy of cmu_graphics, so to operate these programs, either move cmu_graphics into Programs + Documentation or the programs into MAIN GAME.

NOTES FOR PLAYING THE GAME
- Please take note of all the instructions on the start screen! Your controls will be locked until you read them. (Spoiler alert, it will tell you to press enter)
- Purple arrows indicate the strength of distant gravitational influences; more relevantly, they point towards other interesting planets.
- Bear in mind that this is a physics simulation game with very little drag! If you are moving at crazy speeds, you will have to slow yourself down.
- If you unreachably far from the main area of the game, hit [r] to respawn back at home.
- Please pardon the lag! There are a few particularly large sources, and some ways to mitigate them:
- 1. CMU Graphics takes a moment to load a new image for the first time. When you are thrusting, each thrust plume will have 4 unique sprites, so the first time each movement key is held will skip a few times before smoothing out.
  2. CMU Graphics seems to, in general, dislike loading images up close. Use the zoom keys (up and down arrow) to zoom out for a smoother experience.
 
Thank you so much for reading or playing!
Alex Werth, 10/11/2025
