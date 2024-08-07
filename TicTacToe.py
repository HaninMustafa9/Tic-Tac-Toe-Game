class Player:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def chooseName(self, index):
        self.name = input(f"Player {index + 1} Name: ")

    def chooseSymbol(self, index):
        self.symbol = input(f"Player {index + 1} Symbol: ")


class Board:
    def __init__(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]

    def displayBoard(self):
        for row in self.board:
            print(" ".join(map(str,row)))

    def resetBoard(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.displayBoard()
    
    def updateBoard(self, player):
        row = int(input(f"{player.name}: Enter the row number: (1 - 3) "))
        col = int(input(f"{player.name}: Enter the col number: (1 - 3) "))
        
        while (self.board[row-1][col-1] != 0):
                    print("This cell is already filled, Enter another one: ")
                    row = int(input(f"{player.name}: Enter the row number: (1 - 3) "))
                    col = int(input(f"{player.name}: Enter the col number: (1 - 3) "))
        self.board[row - 1][col - 1] = player.symbol
        self.displayBoard()




class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("player 1", "X"), Player("player 2", "O")]

    def startGame (self):
        self.board.resetBoard()
        self.players[0].chooseName(0)
        self.players[0].chooseSymbol(0)
        self.players[1].chooseName(1)
        self.players[1].chooseSymbol(1)

    def checkRow(self, player):
        i = 0
        while (i <=  2):
                if(self.board.board[i][0] == self.board.board[i][1] == self.board.board[i][2] == player.symbol):
           
                    return True
                i += 1
        return False
    
    def checkCol(self, player):
        j = 0
        while (j <=  2):
                if(self.board.board[0][j] == self.board.board[1][j] == self.board.board[2][j] == player.symbol):
              
                    return True
                j += 1
        return False
    def checkdiagonal(self, player):

        if(self.board.board[0][0] == self.board.board[1][1] == self.board.board[2][2] == player.symbol):
                    return True

        return False
    
    def checkWin(self, player):
        if self.checkCol(player) or self.checkRow(player)  or self.checkdiagonal(player):
            print(f"{player.name} WON!")
            return True
        else:
            return False
        

        
    def playTurn(self):
        turn = 1
        while( turn <= 9):
            if(turn % 2 != 0):
                turn += 1
                self.board.updateBoard(self.players[0])
                if self.checkWin(self.players[0]):
                    break
            else:
                turn += 1
                self.board.updateBoard(self.players[1])  
                if self.checkWin(self.players[0]):
                    break       


game = Game()
game.startGame()
game.playTurn()






# Hanin = Player("Hanin", "X")
# Hlaa = Player("Hlaa", "O")
# board = Board()
# board.displayBoard()
# board.updateBoard(Hanin)
# board.updateBoard(Hlaa)