# Snake Game

A simple Snake game built using Python's Turtle graphics library. The player controls a snake to eat food, grow longer, and avoid collisions with the walls and itself.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Directory Structure](#directory-structure)
- [License](#license)

## Features

- Control the snake using keyboard arrow keys.
- The snake grows longer each time it eats food.
- The game ends when the snake collides with the wall or itself.
- Scoreboard to track the player's score.

## Requirements

To run this application, you'll need the following:

- Python 3.x
- Turtle graphics library (included with standard Python installations)

## Installation

1. Clone this repository or download the source code.
2. Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
3. Navigate to the project directory in your terminal.

   ```bash
   cd path/to/your/snake-game
4. Run the main game script:
    ```bash
   python main.py
## How to Play
- Use the arrow keys (Up, Down, Left, Right) to control the snake.
- Try to eat the food to grow longer and increase your score.
- Avoid hitting the walls or running into your own tail.
- The game will end when you collide with a wall or your own body.

## Directory Structure

    ```bash
    snake-game/
    │
    ├── main.py                # The main script to run the game
    ├── snake.py               # The Snake class managing the snake's behavior
    ├── food.py                # The Food class for generating food
    ├── scoreboard.py          # The Scoreboard class for tracking the score
    └── README.md              # This README file

## License
This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
