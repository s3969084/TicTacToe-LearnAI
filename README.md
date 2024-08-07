# Tic Tac Toe Game

This is a simple Tic Tac Toe game implemented using Python and Pygame. The game features a basic AI opponent that makes random moves. The game includes sound effects and background music to enhance the user experience.

## Features

- **Single-player mode**: Play against a basic AI opponent.
- **Random AI**: The AI makes random moves.
- **Sound effects**: Sound effects play when a piece is placed.
- **Background music**: Background music plays during the game.
- **Graphical interface**: The game uses Pygame to provide a graphical interface with images for the board and pieces.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/s3969084/TicTacToe-LearnAI.git
    cd tic-tac-toe-random-ai
    ```

2. **Install the required dependencies**:
    Make sure you have Python and Pygame installed. You can install Pygame using pip:
    ```sh
    pip3 install pygame
    ```

## How to Play

1. **Run the game**:
    ```sh
    python TicTacToe.py
    ```

2. **Gameplay**:
    - The player ('X') will make the first move by clicking on an empty cell on the board.
    - The AI ('O') will then make a random move.
    - The game continues until there is a winner or the board is full (resulting in a draw).

## Files

- `TicTacToe.py`: The main game script.
- `ai.py. : Implement the AI logic here,
- `images/`: Directory containing the images for the board, X, and O pieces.
  - `Board.png`: Image for the Tic Tac Toe board.
  - `X.png`: Image for the X piece.
  - `O.png`: Image for the O piece.
  - `Background.png`: Image for the game background.
- `sounds/`: Directory containing the sound effects and background music.
  - `place.wav`: Sound effect for placing a piece.
  - `background.mp3`: Background music for the game.

## License

This project is licensed under the MIT License. 

## Acknowledgments

- The Pygame community for providing an excellent library for game development.
