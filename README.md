# AAI_CPE_EE-551-B-Tic-Tac-Toe-Game
## CS546-C | Engineering Programming: Python | Tic Tac Toe Game | Members: Kumar Roushan ##

### ***Goal: Directly apply the Python programming concepts  to develop a Tic-Tac-Toe game.*** ###

1. Create a 3x3 board using a 2-dimensional array and initialize each element as empty.
   -  You can represent empty using any symbol you like.
2. Write a Function to check whether the board is filled or not.
   - Iterate over the board and return false if the board contains an empty sign or else return true.
3. Write a Function to check whether a player has won or not.
   - You have to check the possibilities mentioned item 2.
   - Check for all the rows, columns, and two diagonals.
4. Write Function to show the board. (You will show the board multiple times to the users while they are playing).
5. Write a Function to start the game.
   - Select the first turn of the player randomly.
   - Write an infinite loop that breaks when the game is over (either win or draw).
     - Show the board to the user to select the spot for the next move.
     - Ask the user to enter the row and column number.
     - Update the spot with the respective player sign.
     - Check whether the current player won the game or not.
     - If the current player won the game, then print a winning message and break the infinite loop.
     - Next, check whether the board is filled or not.
     - If the board is filled, then print the draw message and break the infinite loop.
   - Finally, show the user the final view of the board.

### ***Required conditions:*** ###
   
- Win: If a player gets three of their symbols in a row (horizontally, vertically, or diagonally), they win the game.
- Draw: If all the spaces on the grid are filled and no player has won, the game is a draw.
- Illegal move: If a player tries to make a move on a space that is already occupied, it is considered an illegal
move. The player should make a move on an empty space.

### ***Requirements*** ###
- Develop an OOP-based Python program or a functional-based Python program to implement a Tic-Tac-Toc game
in python.
- Add comments to your program describing how you have done each part of your program.

## GitHub Link
- https://github.com/Rtannu/AAI_CPE_EE-551-B-Tic-Tac-Toe-Game

