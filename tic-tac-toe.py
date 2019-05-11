# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 19:32:27 2019

@author: shujat
"""

#-----global variables---



#game board
board=["_","_","_",
       "_","_","_",
       "_","_","_" ]
      
game_still_going= True

#who won ?or tie?
winner=None

#who's turn is it
current_player="X"

def display_board():
  print(board[0]+ " | "+ board[1]+" | "+board[2])
  print(board[3]+ " | "+ board[4]+" | "+board[5])
  print(board[6]+ " | "+ board[7]+" | "+board[8])






#play the game of tic-tac-toe
def play_game():
 #display intial board
  display_board()
  #while the game is still going 
  while game_still_going:
    #handle of single turn of arbitary player
    handle_turn(current_player)
    #check if the game has ended
    check_if_game_over()
    # Flip to the other player
    flip_player()
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")
#handle of single turn of arbitary player
def handle_turn(player):
    print(player + "'s turn.")
    position=input("choose a position from 1 to 9: ")
    valid=False
    while not valid:

        while position not in ["1","2","3","4","5","6","7","8","9"]:
          position =input("Invalid input.chose a position from 1-9:")
        
        position=int(position)-1
        if board[position] == "_":
          valid=True
        else:
          print("you can't go there.Go again.")

    board[position]=player
    display_board()




def check_if_game_over():
  check_for_winner()
  check_if_tie()

def check_for_winner():
  #Set_up_global _variable
  #check for rows
  global winner
  row_winner=check_rows()
  #check for columns
  column_winner=check_columns()
  #check for diagonals
  diagonal_winner=check_diagonals()
  if row_winner:
    winner=row_winner
    
  elif column_winner:
    winner=column_winner
  elif diagonal_winner:
    winner=diagonal_winner
  else:
    return None
  
def check_rows():
  #setting up the global vaiable
    global game_still_going
    #check any of the row has same value(and is not empty)
    row_1 = board[0] == board[1] == board[2] !="_"
    row_2 = board[3] == board[4] == board[5] !="_"
    row_3 = board[6] == board[7] == board[8] !="_"
    # if any row has a match then flag there is a win
    if row_1 or row_2 or row_3:
      game_still_going=False
    # return the winner "X" or "O"
    if row_1:
      return board[0]
    elif row_2:
      return board[3]
    elif row_3:
      return board[6]
    return
    # else:
    #   return None
def check_columns():
  global game_still_going
  #check any of the row has same value(and is not empty)
  Columns_1=board[0]==board[3]==board[6] !="_"
  Columns_2=board[1]==board[4]==board[7] !="_"
  Columns_3=board[2]==board[5]==board[8] !="_"
  # if any row has a match then flag there is a win
  if Columns_1 or Columns_2 or Columns_3:
    game_still_going=False
  #return the winner "X" or "O"
  if Columns_1:
    return board[0]
  elif Columns_2:
    return board[1]
  elif Columns_3:
    return board[2]
  return
def check_diagonals():
        global game_still_going
        #check any of the row has same value(and is not empty)
        Diagonal_1=board[0]==board[4]==board[8] !="_"
        Diagonal_2=board[2]==board[4]==board[6] !="_"
        
        # if any row has a match then flag there is a win
        if Diagonal_1 or Diagonal_2 :
          game_still_going=False
        #return the winner "X" or "O"
        if Diagonal_1:
          return board[0]
        elif Diagonal_2:
          return board[2]
        
        return
def check_if_tie():
  global game_still_going
  if "_" not in board:
    game_still_going=False
  return

def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player =="O":
    current_player ="X"
  return
play_game()
