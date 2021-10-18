class engine:
    def __init__(self, board, players):
        self.__players = players
        self.__player1 = 0
        self.__player2 = 0
        self.__board = board

    def set_players(self, player1Type,player2Type):
        """function that sets the two types of players competing
        allows for game mode (pvp/pvai) to be decided and changed mid-game"""
        self.__player1 = self.__players[player1Type]
        self.__player2 = self.__players[player2Type]

    def is_won(self):
        """function that checks if the current board is the result of a winning move.
        If that's the case, returns the winning player. Else 0"""
        X = self.__board.get_val("X")
        O = self.__board.get_val("O")
        if (self.__line(X) or self.__diag(X)):
            return "Player 1"
        elif (self.__line(O) or self.__diag(O)):
            return "Player 2"
        elif len(X)+len(O) == self.__board.rows*self.__board.columns:
            return "Draw"
        else:
            return 0

    def __line(self, valuesList):
        """function that checks if there exists a 4-formation either vertically or horizontally"""
        for i in valuesList:
            if i + 1 in valuesList and i + 2 in valuesList and i + 3 in valuesList:
                return 1
            if i + 10 in valuesList and i + 20 in valuesList and i + 30 in valuesList:
                return 1
        return 0

    def __diag(self, valuesList):
        """function that checks if there exists a 4-formation diagonally"""
        for i in valuesList:
            if i + 11 in valuesList and i + 22 in valuesList and i + 33 in valuesList:
                return 1
            if i + 9 in valuesList and i + 18 in valuesList and i + 27 in valuesList:
                return 1
        return 0

    def move(self, player, position=0):
        """function that...makes the players move"""
        if player == 1:
            self.__player1.move(self.__board, position)
        else:
            self.__player2.move(self.__board, position)

