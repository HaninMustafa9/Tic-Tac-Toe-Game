# Tic-Tac-Toe Game

## Project Overview

This project implements a simple Tic-Tac-Toe game using Python. The game allows two players to take turns placing their symbols ("X" or "O") on a 3x3 board. The game checks for a win condition after every move and displays the board state.

## Classes

### `Player`

Represents a player in the game.

- **Methods:**
  - `__init__(self, name, symbol)`: Initializes the player's name and symbol.
  - `chooseName(self, index)`: Prompts the player to enter their name.
  - `chooseSymbol(self, index)`: Prompts the player to enter their symbol.

### `Board`

Represents the Tic-Tac-Toe board.

- **Methods:**
  - `__init__(self)`: Initializes the board as a 3x3 grid with all cells set to 0.
  - `displayBoard(self)`: Prints the current state of the board.
  - `resetBoard(self)`: Resets the board to its initial state and displays it.
  - `updateBoard(self, player)`: Updates the board based on the player's move and displays the updated board.

### `Game`

Manages the game flow, including player turns and win checks.

- **Methods:**
  - `__init__(self)`: Initializes the game with a board and two players.
  - `startGame(self)`: Resets the board and prompts players to choose their names and symbols.
  - `checkRow(self, player)`: Checks if the player has won by filling a row.
  - `checkCol(self, player)`: Checks if the player has won by filling a column.
  - `checkdiagonal(self, player)`: Checks if the player has won by filling a diagonal.
  - `checkWin(self, player)`: Checks if the player has won the game.
  - `playTurn(self)`: Manages the game loop, alternating turns between players and checking for a win.

## Usage

1. **Initialize and Start the Game:**

   ```python
   game = Game()
   game.startGame()
   ```

2. **Play Turns:**

   ```python
   game.playTurn()
   ```

## Example

Here’s an example of how the game classes might be used:

```python
Hanin = Player("Hanin", "X")
Hlaa = Player("Hlaa", "O")
board = Board()
board.displayBoard()
board.updateBoard(Hanin)
board.updateBoard(Hlaa)
```

## Notes

- The game checks for win conditions after each move.
- The board is displayed after each move to show the current state.
