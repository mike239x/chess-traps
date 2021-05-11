import chess
import chess.pgn
import chess.polyglot
from tqdm import tqdm
import numpy as np

# https://python-chess.readthedocs.io/en/latest/pgn.html


black = chess.BLACK
white = chess.WHITE

#  games_num = 121332
games_num = 1213

zhash = chess.polyglot.zobrist_hash

pgn = open('lichess_db_standard_rated_2013-01.pgn')

def result_(game):
    result = game.headers['Result']
    possible_results = np.array([
        '0-1',
        '1/2-1/2',
        '1-0',
    ])
    return possible_results == result

moves_db = {}

#  max_depth = 1
#  max_width = 10

for n in tqdm(range(games_num)):
    game = chess.pgn.read_game(pgn)
    game_result = result_(game)
    board = game.board()
    for move in game.mainline_moves():
        h = zhash(board)
        if h not in moves_db:
            moves_db[h] = {}
        if move not in moves_db[h]:
            moves_db[h][move] = np.zeros(3)
        moves_db[h][move] += game_result
        board.push(move)

print(moves_db[zhash(chess.Board())])
#  print(moves_db)
