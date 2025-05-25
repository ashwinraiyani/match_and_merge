# Match & Merge - Number Puzzle Game

A Python implementation of a tile-matching puzzle game similar to 2048, built with Pygame.

## Description

Match & Merge is an addictive puzzle game where you combine matching number tiles to create tiles with higher values. The goal is to reach the 2048 tile, but you can continue playing to achieve even higher scores!

## Features

- Smooth tile animations
- Score tracking with high score
- Game state management (start screen, playing, paused, won, game over)
- Attractive color scheme that changes based on tile values
- Responsive controls

## Requirements

- Python 3.x
- Pygame 2.x

## Installation

1. Make sure you have Python installed on your system
2. Install Pygame using pip:
   ```
   pip install pygame
   ```
3. Clone or download this repository

## How to Play

1. Run the game:
   ```
   python3 main.py
   ```
2. Click "Start Game" on the start screen
3. Use the arrow keys (↑, ↓, ←, →) to move all tiles in that direction
4. When two tiles with the same number touch, they merge into one tile with double the value
5. After each move, a new tile (either 2 or 4) appears in a random empty cell
6. The goal is to create a tile with the value 2048
7. The game ends when there are no more possible moves

## Controls

- **Arrow Keys**: Move tiles
- **R Key**: Restart the game
- **C Key**: Continue playing after winning
- **ESC Key**: Pause/resume the game

## Project Structure

- **main.py**: Entry point with the main game loop
- **constants.py**: Game constants, colors, and configuration
- **game.py**: Game class with core game logic
- **renderer.py**: Drawing functions for the game UI

## License

This project is open source and available under the MIT License.
