# pong

Pong, in Python with pygame. Two paddles, one ball, first-to-N wins.

```bash
pip install pygame
python pong.py
```

`W` / `S` for the left paddle, `↑` / `↓` for the right.

Early-summer 2023 project — wrote this in an afternoon while learning the pygame event loop. The whole game lives in one file: globals for position/velocity, a single `while True` for the loop, axis-aligned rectangle collision against the paddles, and a serve-from-center reset after each point.

Things I'd do differently now: factor the game state into a class, move the input handling out of the render path, and pin the ball's velocity to a fixed magnitude so each rally has the same difficulty. But as a learning artifact it stays as-is.
