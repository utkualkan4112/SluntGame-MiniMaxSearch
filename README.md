# SluntGame-MiniMaxSearch

Modeling the Loopless Slant game using a Mini Max search tree.

## Overview

This project models the Loopless Slant game as a Game Tree Search problem. It uses a Mini Max search tree to navigate and predict potential moves, optimizing the gameplay for each player.

## Game Rules

### Players
- **Player 1**: Assigned the symbol ‘/’ and aims to maximize the score.
- **Player 2**: Assigned the symbol ‘\\’ and aims to minimize the resulting score.

### States
- **State**: Represents the current configuration of the `m x m` grid, which includes diagonal lines' locations and empty cells.
- **Initial State**: An empty `m x m` grid with specific intersections containing circles numbered 1-3. This can change depending on the player starting first.
- **Terminal States**: Reached when all `m x m` grid cells are filled.

### Transitions & Scoring
- **State Transition Function**: Considers a state and a player's move to determine the resulting state. Moves involve placing a diagonal line in an empty cell, potentially leading to scoring based on circle intersections.
- **Payoff Function**: Returns a player's score for a terminal state, considering the number of points they've gathered (points are earned when the number of intersecting lines at a circle matches the circle's number). The score is calculated as `Max player points (Player 1) - Min player points (Player 2)`.

## Gameplay Examples

For sample gameplays, refer to the `gameplays.txt` file.

## Usage

1. Specify the gameboard size in `main`.
2. Provide the size as a `Game` parameter.
3. The code will then randomly generate a game of the specified size.

## Custom Gameboards

To design a custom gameboard:

- Use the `board` variable to indicate where '/' or '\\' can be placed.
- Use the `board_points` variable to display the scoreboard.
- Both variables are essential for a functioning gameboard.

### Examples

For a 2x2 board:

board = [[None, None], [None, None]]

For board points with a row example:

(1, 0), None, (1, 0)
here 1 is points you get, 0 is current intersecting line, None is a corner that dont contains point

For a full 2x2 gameboard:

board_points = [[(1, 0), None, (1, 0)], [None, (2, 0), None], [None, None, (1, 0)]]

To implement a custom gameboard, paste your board and board points in the commented lines at `line 19` and `line 20` in the `create_board` function, respectively.
