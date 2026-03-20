Boot.dev Python Project for learning Object oriented programming
Because of checks from Boot.dev there are some built in code for saving a game_state file for correcting the assignment on boot.dev

## Asteroids
A clone of the classic Asteroids arcade game built with Python and Pygame.

### Features

Control a spaceship and navigate through an asteroid field
Shoot asteroids to destroy them
Large asteroids split into smaller, faster-moving asteroids when hit
Game ends when the player collides with an asteroid

### How to Play

Rotate: A / D 

Thrust: W 

Backwards: S

Shoot: Space

### Requirements

Python version must be under version 3.14 because pygame doesn't support 3.14. Create a venv with python 3.13 and pygame if you want to run it.

Pygame

### Installation and running it

if python Version is above 3.13:

CD into the project directory

python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pygame
python main.py

Else:

CD into the project directory

pip install pygame

python main.py
