#! /usr/bin/python3.8

"""
W02 Assignment - Tic Tac Toe
CSE210
Rob Cox
"""

def display_board(board):
   print()
   for i in range(9):
      print(board[i] + ("|" if (i + 1) % 3 else ""), end="")
      if i == 2 or i == 5:
         print("\n-+-+-")
   print()
   print()

def game_over(board):
   result = False
   
   # Across for x
   if board[0] == "x" and board[1] == "x" and board[2] == "x":
      result = True
   elif board[3] == "x" and board[4] == "x" and board[5] == "x":
      result = True
   elif board[6] == "x" and board[7] == "x" and board[8] == "x":
      result = True

   # Down for x
   if board[0] == "x" and board[3] == "x" and board[6] == "x":
      result = True
   elif board[1] == "x" and board[4] == "x" and board[7] == "x":
      result = True
   elif board[2] == "x" and board[5] == "x" and board[8] == "x":
      result = True

   # Diagonal for x
   if board[0] == "x" and board[4] == "x" and board[8] == "x":
      result = True
   elif board[2] == "x" and board[4] == "x" and board[6] == "x":
      result = True

 # Across for o
   if board[0] == "o" and board[1] == "o" and board[2] == "o":
      result = True
   elif board[3] == "o" and board[4] == "o" and board[5] == "o":
      result = True
   elif board[6] == "o" and board[7] == "o" and board[8] == "o":
      result = True

   # Down for o
   if board[0] == "o" and board[3] == "o" and board[6] == "o":
      result = True
   elif board[1] == "o" and board[4] == "o" and board[7] == "o":
      result = True
   elif board[2] == "o" and board[5] == "o" and board[8] == "o":
      result = True

   # Diagonal for o
   if board[0] == "o" and board[4] == "o" and board[8] == "o":
      result = True
   elif board[2] == "o" and board[4] == "o" and board[6] == "o":
      result = True

   # Draw
   if board[0] != "1" and \
      board[1] != "2" and \
      board[2] != "3" and \
      board[3] != "4" and \
      board[4] != "5" and \
      board[5] != "6" and \
      board[6] != "7" and \
      board[7] != "8" and \
      board[8] != "9":
      result = True 
      
   return result

def main():
   user = 'x'
   board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
   
   # Display initial board
   display_board(board)
   
   # Loop until game is over
   while True:

      move = int(input(user + "'s turn to choose a square(1-9): "))
      board[move - 1] = user
      display_board(board)

      if game_over(board):
         print("Good game. Thanks for playing!")
         break
      if user == "x":
         user = "o"
      elif user == "o":
         user = "x"

if __name__ == "__main__":
   main()

