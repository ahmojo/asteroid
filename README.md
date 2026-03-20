# Asteroids

A clone of the classic **Asteroids** arcade game built with **Python** and **Pygame**.

This project was created as part of the Boot.dev Python course for learning object-oriented programming.

Because of Boot.dev's automated checks, the project includes some built-in code for saving a `game_state` file used for assignment validation.

## Features

- Control a spaceship and navigate through an asteroid field
- Shoot asteroids to destroy them
- Large asteroids split into smaller, faster-moving asteroids when hit
- The game ends when the player collides with an asteroid

## Controls

- **A / D** — Rotate
- **W** — Thrust forward
- **S** — Move backward
- **Space** — Shoot

## Requirements

- **Python 3.13 recommended**
- **Pygame**

If your system uses Python 3.14, create a virtual environment with **Python 3.13** and install `pygame` there.

## Installation

### If you have Python 3.14 or newer installed as default

First, change into the project directory:

```bash
cd asteroid
```

Then create and activate a virtual environment with Python 3.13.

#### Linux / macOS

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pygame
python main.py
```

#### Windows

```bash
py -3.13 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install pygame
python main.py
```

### If you are already using Python 3.13

Change into the project directory:

```bash
cd asteroid
```

Then install pygame and run the game:

```bash
python -m pip install --upgrade pip
python -m pip install pygame
python main.py
```
