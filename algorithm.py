# makes an actual copy of the object not just a reference to the object. BOXES!
from copy import deepcopy
from constants import RED, WHITE
import random

# this function will be called recursively
# current_board will be a board object - based on this board
# depth - how far am i making this tree - every time we call this function the depth will decrease by one.
# max_player - boolean value - are we trying minimize or maximize?
# game - the actual game object. 
def minimax(current_board, depth, max_player):
  return 0, get_all_moves(current_board, WHITE)[0]
  # evaluate position when we reach the depth of the tree, evaluations bubble up. 
  if depth == 0 or current_board.winner(RED) != False or current_board.winner(WHITE) != False:
    pass

  elif max_player:
    pass

  else:
    pass


# This function crates a deep copy of the current board, determines all possible moves that color can make, and returns a list that contains the boards that would result from the possible moves.
def get_all_moves(board, color):
    moves = []                                # this array will contain Boards
    possible_moves = board.get_valid_moves()  # gets an array that contains the lowest open row in each column. It's main purpose is to see if a column is full so that we can skip over that row. 
    for column in range(len(possible_moves)):      # loop through each column
      if possible_moves[column] != -1:             # column is full if it has a lowest open row of -1 so we can skip it.
        temp_board = deepcopy(board)               # creates a deep copy of the board as opposed to a shallow copy.
        temp_board.add_piece(color, column)        # add a piece to the new copy of board in column
        moves.append(temp_board)                  # add the new board to the list

    if board.winner(RED) or board.winner(WHITE):
      return []

    return moves

# Functions for evaluating the board. These functions will be used by the minimax algorithm.
# this function will get the score!

def evaluate_algorothm(board):
  return total_score(WHITE, board) - total_score(RED, board)

def total_score(color, board):
  return random.randint(1,10)