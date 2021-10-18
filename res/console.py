class console:
    def __init__(self,engine,board):
        self.__engine = engine
        self.__board = board
        self.run_game()

    def __print_board(self):
        """function that prints the board"""
        board = self.__board.get_matrix()
        for i in board:
            print(*i, sep=" | ")
        l=[]
        for i in range (1,8):
            l.append(i)
        print(*l,sep=" | ")

    def run_game(self):
        print("Welcome")
        print("Enter 'exit' anytime to quit")
        playing = 1
        last = 0
        while playing:
            game_mode, game_diff = self.__gametype()
            if game_mode == 1:
                last = self.__HvH(last)
            else:
                last = self.__HvAI(game_diff,last)
            print("Play again? Y/N")
            choice = input(">").upper()
            if choice == "EXIT":
                self.__exit(0)
            while(not choice in ["Y","N"]):
                print("Type Y or N")
                choice = input(">").upper()
                if choice == "EXIT":
                    self.__exit(0)
            if choice == "N":
                self.__exit(0)
            else:
                self.__board.reset()

    def __gametype(self):
        print("Choose game mode:")
        print("1: local pvp     2: vs AI")
        print("Type 1 or 2")
        game_mode = input(">")
        if game_mode == "exit":
            self.__exit(0)
        count = 0
        while (not (game_mode in ["1", "2"])):
            print("Please enter 1 or 2!!!")
            game_mode = input(">")
            if game_mode == "exit":
                self.__exit(0)
            count += 1
            if count > 10:
                print("Please come back when you really want to play...")
                self.__exit(0)
        if game_mode == "1":
            return 1,0
        else:
            print("Choose AI difficulty:")
            print("1: easy   2: medium   3:hard")
            print("Type 1, 2 or 3")
            game_diff = input(">")
            if game_mode == "exit":
                self.__exit(0)
            count = 0
            while (not (game_diff in ["1","2","3"]) ):
                print("Please enter 1, 2 or 3!!!")
                game_mode = input(">")
                if game_mode == "exit":
                    self.__exit(0)
                count += 1
                if count > 10:
                    print("Please come back when you really want to play...")
                    self.__exit(0)
            return 2,int(game_diff)

    def __HvH(self,last):
        self.__engine.set_players("hX", "hO")
        print("initializing game...")
        self.__print_board()
        winner = 0
        p = last
        while (winner == 0):
            print(f"Player {p + 1}'s turn")
            print(f"Select a column in 1-{self.__board.columns}")
            ok = True
            while ok:
                try:
                    pos = input(">")
                    if pos == "exit":
                        ok = False
                        break
                    pos = int(pos)-1
                    assert pos in range(0,self.__board.columns)
                    if self.__board.is_valid(pos):
                        break
                    else:
                        print(f"Column {pos+1} is full. Try another one.")
                except:
                    print(f"Please select a column in 1-{self.__board.columns}")
            if ok == False:
                self.__exit(0)
            self.__engine.move(p + 1, pos)
            self.__print_board()
            p = (p + 1) % 2
            winner = self.__engine.is_won()
        if winner == "Draw":
            print("Draw!")
            return p
        else:
            print(f"{winner} won!!")
            if winner == "Player 1":
                return 1
            else: return 0

    def __HvAI(self,game_diff,last):
        diffs = ["easy", "medium", "hard"]
        print(f"AI: {diffs[game_diff - 1]}")
        self.__engine.set_players("hX", str("AI"+diffs[game_diff - 1]))
        print("initializing game...")
        self.__print_board()
        winner = 0
        p = last
        while (winner == 0):
            if p==0:
                print(f"Your turn")
                print(f"Select a column in 1-{self.__board.columns}")
                while True:
                    try:
                        pos = input(">")
                        if pos == "exit":
                            self.__exit(0)
                        pos = int(pos) - 1
                        assert pos in range(0, self.__board.columns)
                        if self.__board.is_valid(pos):
                            break
                        else:
                            print(f"Column {pos+1} is full. Try another one.")
                    except:
                        print(f"Please select a column in 1-{self.__board.columns}")
                self.__engine.move(1, pos)
                self.__print_board()
            else:
                print(f"AI's turn...")
                self.__engine.move(2)
                self.__print_board()
            p=(p+1)%2
            winner = self.__engine.is_won()
        if winner == "Player 1":
            print("You won!!")
            return 1
        elif winner == "Player 2":
            print("AI won!!")
            return 0
        else:
            print("Draw!")
            return p

    def __exit(self,value):
        print("Closing the application...")
        exit(value)
