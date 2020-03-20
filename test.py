class Board:
    def __init__(self):
        self.board = {(0, 0): None, (0, 1): None, (0, 2): None, (1, 0): None, (1, 1): None, (1, 2): None, (2, 0): None, (2, 1): None, (2, 2): None}

    def isMoveValid(self, x, y):
        for square in self.board:
            if square[0] == x and square[1] == y and self.board[(x, y)] is None:
                return True
        return False

    def move(self, x, y, player):
        self.board[(x, y)] = player

    def isWinner(self):
        squares = []
        # check vertical squares
        for i in range(3):
            for j in range(3):
                squares.append(self.board[(i, j)])
            if len(set(squares)) == 1:
                if squares[0] is not None:
                    return True
            squares = []
        # check horizontal squares
        for i in range(3):
            for j in range(3):
                squares.append(self.board[(j, i)])
            if len(set(squares)) == 1:
                if squares[0] is not None:
                    return True
            squares = []
        # check diagonal squares
        # top left bottom right
        for i in range(3):
            squares.append(self.board[(i, i)])
        if len(set(squares)) == 1:
            if squares[0] is not None:
                return True
        squares = []
        # bottom left top right
        j = 2
        for i in range(3):
            squares.append(self.board[(i, j)])
            j -= 1
        if len(set(squares)) == 1:
            if squares[0] is not None:
                return True


    def empty(self):
        self.board = {(0, 0): None, (0, 1): None, (0, 2): None, (1, 0): None, (1, 1): None, (1, 2): None, (2, 0): None, (2, 1): None, (2, 2): None}


board = Board()

player1 = "circle"
player2 = "cross"


player = player1

while True:
    print(player, "it's your turn to play")
    inpx = int(input("input x:  "))
    inpy = int(input("input y:  "))
    if board.isMoveValid(inpx, inpy):
        board.move(inpx, inpy, player)
        print(board.board)
        if board.isWinner():
            print(player, "is the winner")
        if player == player1:
            player = player2
        else:
            player = player1
