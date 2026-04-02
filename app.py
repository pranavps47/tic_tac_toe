import os
import random
import math
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def check_winner(board):
    win_coords = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for a, b, c in win_coords:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board: return "Tie"
    return None


def minimax(board, depth, is_maximizing):
    res = check_winner(board)
    if res == "O": return 10 - depth
    if res == "X": return depth - 10
    if res == "Tie": return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == "":
                board[i] = "O";
                score = minimax(board, depth + 1, False)
                board[i] = "";
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == "":
                board[i] = "X";
                score = minimax(board, depth + 1, True)
                board[i] = "";
                best_score = min(score, best_score)
        return best_score


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/move', methods=['POST'])
def move():
    data = request.json
    board = data['board']
    mode = data['mode']
    available = [i for i, s in enumerate(board) if s == ""]

    if not available: return jsonify({"move": None})

    if mode == "easy":
        chosen = random.choice(available)
    else:
        best_score = -math.inf
        chosen = None
        for i in available:
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                chosen = i
    return jsonify({"move": chosen})


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)