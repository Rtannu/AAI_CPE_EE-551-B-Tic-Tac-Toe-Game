import random

"""
Roushan Kumar | ID: 20009314
Spring 2023 – Final-project
Tic-Tac-Toe game
"""


class TicTacToeGame:
    def __init__(self, row, col, firstPlayer, secondPlayer,emptySymbol):
        # row of board
        self.ROW = row

        # column of board
        self.COL = col

        # empty symbol of board
        self.EMPTY_SYMBOL=emptySymbol

        # initialization of board with empty string
        self.board = [[self.EMPTY_SYMBOL for j in range(col)] for i in range(row)]

        # initialization of player
        self.players = [firstPlayer, secondPlayer]

        # random choice of player
        self.currentPlayer = random.choice(self.players)

    # check whether board is filled or not
    def isBoardFilled(self):

        # iterate the board
        for row in self.board:

            # check the empty string in row
            if self.EMPTY_SYMBOL in row:
                return False
        return True

    # check the winner
    def checkWinner(self, player):

        # check row
        for row in range(self.ROW):
            if self.board[row] == [player] * self.COL:
                return True

        # check column
        for i in range(self.COL):
            if [self.board[j][i] for j in range(self.ROW)] == [player] * self.ROW:
                return True

        # check the backward diagonal
        diagonalEleList = []
        for row in range(self.ROW):
            diagonalEleList.append(self.board[row][row])
        if ([player] * self.ROW == diagonalEleList):
            return True

        # check the forward diagonal
        diagonalEleList = []
        for row in range(self.ROW):
            diagonalEleList.append(self.board[row][self.COL - 1 - row])
        if ([player] * self.ROW == diagonalEleList):
            return True

        # no winner
        return False

    # show board
    def showBoard(self):
        for row in self.board:
            # print row
            print(row)

    # start the game
    def startGame(self):

        # run infinite loop
        while True:

            # print current player
            print(f"\nCurrent player : {self.currentPlayer}")

            # show the board
            self.showBoard()

            # take row from user
            while True:
                try:
                    row = int(input(f"Enter row number between 1 and {self.ROW} [1-{self.ROW}]: "))
                    if (row < 1 or row > self.ROW):
                        print("Invalid row, please try again..........")
                    else:
                        break
                except:
                    print("Invalid row, please try again..........")



            # take col from user
            while True:
                try:
                    col = int(input(f"Enter column number between 1 and {self.ROW} [1-{self.COL}]: "))
                    if (col < 1 or col > self.COL):
                        print("Invalid col, please try again..........")
                    else:
                        break
                except:
                    print("Invalid col, please try again..........")

            row = row - 1
            col = col - 1

            # check illegal move
            if self.board[row][col] != self.EMPTY_SYMBOL:
                print("This space is already occupied. Please choose another empty space!!")
                continue

            # store the move of current player in board
            self.board[row][col] = self.currentPlayer

            # check the winner
            if self.checkWinner(self.currentPlayer):
                print(f"\nCongrats {self.currentPlayer}, you won the tic-tac-toe game!!!!!")
                break

            # check the board whether it's filled or not
            if self.isBoardFilled():
                print("\nNo player has won and the game is a draw!!!!!")
                break

            # choose next player
            for player in self.players:
                if player!=self.currentPlayer:
                    self.currentPlayer=player
                    break

        # show the user the final view of the board
        self.showBoard()


# start game
def playTicToeGame():
    # no of row
    ROW = 5

    # no of column
    COL = 5

    # first player
    FIRST_PLAYER = 'A'

    # second player
    SECOND_PLAYER = 'B'

    # empty symbol
    EMPTY_SYMBOL = '_'

    # instance creating
    game = TicTacToeGame(ROW, COL, FIRST_PLAYER, SECOND_PLAYER, EMPTY_SYMBOL)

    # start game
    game.startGame()


while True:
    # start game
    playTicToeGame()

    # take input from user
    i=input("Do you want to play again?\nEnter YES to play again, otherwise enter any to exit from game\n")
    if i.lower()=="yes":
        continue
    else:
        print("\n................Thank you for playing!.........")
        print("..................Exiting from game..............")
        break

