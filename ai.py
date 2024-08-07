# ai.py

import random

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    # No winner
    return None

def ai_move(board):
    # Simple AI move logic: pick a random empty spot
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    if empty_cells:
        return random.choice(empty_cells)
    return None

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)
