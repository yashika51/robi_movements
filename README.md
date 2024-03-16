# Robi Movements


This is a Python based project that addresses the robi movements task. I am primarily using FastAPI, Pydantic as well as Typer.


## How to run the command

- Clone the repo
- Create a virutal env `python3 -m venv name_of_venv`
- `source name_of_venv/bin/activate`
- `pip install -r requirements.txt`
- `python app.py move_robot "movement_str"`


## Future improvements

I added models.py as a placeholder to show how pydantic types can be enforced, its specifically
useful with the API implementation. On the same note, I added api.py file to also have the similar
API implementation.

## Additional Info

- There is also the test.py file added just to have some initial tests
- The bonus_x position(bonus_x,bonus_y) can either be provided to be constant
   or let to be set randomly between -100 to 100

## Overview

Below is the high level description of what the task asks:

Keed Digital has a small robot (Robi), which moves around in a 2-dimensional grid. Robi can
only turn left or right and walk straight. The robot also knows its current position (X, Y) as well
as its direction: Top (T), Bottom (B), Left (L) or Right (R).
In order to get the Robi to move, we need to input a move command. The move command can
be represented with a string consisting of three alphabets L, R and F. F string will be followed by
a positive integer X to indicate the distance of how many steps it has to move, which can be
explained as follows:
- L: Turn to the left from Robi current position (counterclockwise)
- R: Turn to the right from Robi current position (clockwise)
- FX: Move Forward for X step(s) where X can be any positive integers. For example, F12
means moving forward for 12 steps.

Initial conditions
- Robi starts at the position (X,Y) of (0,0)
- Robi is facing Top (T), we state Direction (D) to D:T
 We add one Bonus item in a random (X,Y) location in the range of -100 to 100


The example
Given the move command of LLF9RF4RRF12 means
Robi starts at the position X:0; Y:0; D:T
1. Robi turns left - facing Left (X:0; Y:0; D:L)
2. Robi turns left - facing Bottom (X:0; Y:0; D:B)
3. Robi moves forward 9 steps (X:0; Y:-9; D:B)
4. Robi turns right - facing Left (X:0; Y:-9; D:L)
5. Robi moves forward 4 steps (X:-4; Y:-9; D:L)
6. Robi turns right - facing Top (X:-4; Y:-9; D:T)
7. Robi turns right - facing Right (X:-4; Y:-9; D:R)
8. Robi moves forward 12 steps (X:8; Y:-9; D:R)
9. Print out the last position, direction and if passed the bonus location &gt; X:8; Y:-9; D:R;
B:0

The task is to create an elegant command-line script that accepts a command-line argument as an input string of the move command and print
out the result of the last position (X, Y), direction (T, B, L or R) and if Robi passed the Bonus (B) location.