# 🎮 Tic Tac Toe - Python Console Game

This is a simple implementation of the classic **Tic Tac Toe** game using Python. It is played between a human player (`X`) and the computer (`O`) on the terminal/command line.

---

## 📋 Features

* Turn-based play between user (`X`) and computer (`O`)
* Board display after each move
* Detects win conditions (rows, columns, diagonals)
* Detects ties when the board is full
* Random computer moves using Python's `random` module

---

## 🛠 Requirements

* Python 3.x

---

## 🚀 How to Run

1. **Clone this repository** or copy the code into a `.py` file, for example:

   ```
   git clone https://github.com/your-username/Tic-Tac-Toe-using-python.git
   ```

2. **Navigate to the folder** and run the game:

   ```
   cd tic-tac-toe-python
   python tictactoe.py
   ```

3. **Play the game** by entering a number (1–9) when prompted:

   ```
    1 | 2 | 3
   -----------
    4 | 5 | 6
   -----------
    7 | 8 | 9
   ```

   Choose your move by typing the position number.

---

## 🧠 How It Works

* The game board is a list of 9 elements representing each cell.
* Players take turns: the human enters a position, the computer chooses a random empty spot.
* After every move:

  * It checks if a player has won.
  * It checks if the board is full (tie).
  * If no win or tie, it switches the turn.

---

## 💡 Sample Gameplay

```
- | - | -
------------
- | - | -
------------
- | - | -

Enter a num 1-9: 5

- | - | -
------------
- | X | -
------------
- | - | O

...
The winner is X
```

---

## 🔍 To-Do (Optional Enhancements)

* Improve computer logic with minimax algorithm (AI)
* Add GUI using Tkinter or Pygame
* Input validation enhancements
* Play against another human

---

## 📄 License

This project is free to use and modify for learning and personal use.

---

## 🙌 Author

Developed with ❤️ by SAGAR DEY

---


