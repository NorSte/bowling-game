# 🎳 Bowling Game (Cyber-Dojo Challenge) - Test-Driven Development Task (TDD)

This is a Python implementation of the classic **Bowling Score Calculator**, developed as part of the Cyber-Dojo kata. 

## Project Structure

cyber-dojo-bowling-game/
├── files/                 # Main source code files
├── test_bowling.py        # Unit tests for the game
├── bowling.py             # Core logic for score calculation
├── README.md              # This file
├── manifest.json, etc.    # Cyber-Dojo configuration files

## Features

- Calculates bowling scores frame-by-frame
- Supports all rules:
  - Strikes (`X`)
  - Spares (`/`)
  - Misses (`-`)
  - Tenth frame bonus logic
- Includes unit tests using `pytest`

## How to Run

Make sure you have Python and pytest installed:

pip install pytest

Then run tests with:

pytest

## Example

For input:  
X|7/|9-|X|-8|8/|-6|X|X|X||81

The output score will be:
167

## Based On

This project is inspired by the Cyber-Dojo Bowling Game Kata (https://cyber-dojo.org/).
