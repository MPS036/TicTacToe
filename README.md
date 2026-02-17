🎮 Tic-Tac-Toe (Console Version)

A console-based implementation of the classic Tic-Tac-Toe game written in Python.
The human player competes against a simple rule-based AI.

The human player always starts first and plays as X.
The computer plays as O.
The game runs in the terminal.
The board positions are numbered from 1 to 9:
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9

🤖 AI Strategy

The computer uses a deterministic rule-based strategy:
(i) Win if possible;
(ii) Block opponent’s winning move;
(iii) Take a corner (1, 3, 7, 9);
(iv) Take the center (5);
(v) Take an edge (2, 4, 6, 8).
This ensures the AI plays optimally within the defined logic.

🛠 Requirements

This project uses only Python’s standard library.
Python 3.x is required.
