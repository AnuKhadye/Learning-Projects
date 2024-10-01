# Classic Pong Game

This is a classic Pong game implemented using Python's `turtle` module. The game is a two-player game where each player controls a paddle to prevent the ball from getting past them. The first player to lose the ball to the other side loses the round.

## Features
- Simple 2-player Pong game.
- Controls:
  - **Left Paddle (Player 1):**
    - Move up: `W`
    - Move down: `S`
  - **Right Paddle (Player 2):**
    - Move up: `Up Arrow`
    - Move down: `Down Arrow`
- Scoreboard to track points.
- Realistic ball movement with bouncing off walls and paddles.
  
## Prerequisites

Before you begin, ensure you have Python installed on your machine. You also need the following modules, which are part of the `turtle` library:

- `turtle` (comes with Python)
- `time` (standard Python library)

## How to Run the Game

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/pong-game.git
    ```

2. Navigate into the directory:

    ```bash
    cd pong-game
    ```

3. Run the Python file:

    ```bash
    python pong.py
    ```

The game will open in a new window, where you can use the controls listed above to play.

## Files

- `pong.py`: Main game file that sets up the screen and runs the game.
- `paddle.py`: Class definition for the paddles.
- `ball.py`: Class definition for the ball.
- `scoreboard.py`: Class definition for the scoreboard.

## How to Play

- The goal of the game is to prevent the ball from passing your paddle.
- Each time a player misses the ball, the other player scores a point.
- The game continues indefinitely, so you can decide the winning score!

## License

This project is open-source and free to use under the [MIT License](../LICENSE).
