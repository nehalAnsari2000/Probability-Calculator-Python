# Probability Calculator

## Overview
This project is a probability calculator implemented in Python. It simulates drawing balls from a hat to estimate the probability of drawing a specific combination of balls. This project was a **mandatory** part of the *Scientific Computing with Python* certification on FreeCodeCamp, where I learned about probability, random sampling, and deep copying objects in Python.

## Features
- **Hat Class**: Represents a hat filled with balls of different colors.
- **Random Draws**: Simulates drawing a specified number of balls from the hat.
- **Experiment Function**: Runs multiple experiments to estimate the probability of drawing the expected combination of balls.
- **Uses `random.sample`**: Ensures random and non-repeating draws.
- **Deep Copying**: Prevents modifications to the original hat during experiments.

## Usage
1. Create a `Hat` object with the desired number of balls:
   ```python
   hat = Hat(black=6, red=4, green=3)
   ```
2. Run an experiment to estimate probability:
   ```python
   probability = experiment(hat=hat, expected_balls={'red':2, 'green':1}, num_balls_drawn=5, num_experiments=2000)
   print(probability)
   ```
3. The function returns an estimated probability between `0` and `1`.

## Dependencies
- Python 3.x
- Uses the built-in `random` and `copy` modules (no external dependencies required).

## Acknowledgments
This project was a **mandatory** part of the *Scientific Computing with Python* certification on FreeCodeCamp, where I learned about probability and object-oriented programming concepts in Python.

