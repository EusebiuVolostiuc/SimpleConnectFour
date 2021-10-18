import random
from copy import deepcopy


class AI:
    def __init__(self,engine, difficulty):
        self.__engine = engine
        if difficulty == 1:
            self.__difficulty = 1
        if difficulty == 2:
            self.__difficulty = 2
        if difficulty == 3:
            self.__difficulty = 4
    def move(self, board, position=0):
        """the move of the ai consists of determining the best position and putting a O on that position"""
        # position = self.__best_move(board)
        score,position = self.__minimax(board,self.__difficulty,-10000,10000,True)
        board.put_val(position, "O")

    def __score_position(self, board):
        """function that calculates and returns the score of the board (the higher the score, the higher the chance of the AI to win)"""
        score = 0
        center_array = board.get_column(3)
        score += center_array.count("O")*6
        score += self.__score_rows(board)
        score += self.__score_columns(board)
        score += self.__score_diags(board)
        return score

    def __score_rows(self,board):
        """calculates score based on how the values on the board could form horizontal formations"""
        score = 0
        for r in range(board.rows - 1, -1, -1):
            row_arr = board.get_row(r)
            for c in range(board.columns - 3):
                window = row_arr[c:c + 4]
                score += self.__eval_window(window)
        return score

    def __score_columns(self,board):
        """calculates score based on how the values on the board could form vertical formations"""
        score = 0
        for c in range(board.columns):
            col_arr = board.get_column(c)
            for r in range(board.rows - 3):
                window = col_arr[r:r + 4]
                score += self.__eval_window(window)
        return score

    def __score_diags(self,board):
        """calculates score based on how the values on the board could form diagonal formations"""
        score = 0
        matrix =board.get_matrix()
        for r in range(board.rows-3):
            for c in range(board.columns-3):
                window = [matrix[r+i][c+i] for i in range(4)]
                score += self.__eval_window(window)
        for r in range(3,board.rows):
            for c in range(board.columns-3):
                window = [matrix[r-i][c+i] for i in range(4)]
                score += self.__eval_window(window)
        return score

    def __eval_window(self,window):
        """the most important part of the AI algorithm
        here we assign the score of a particular window depending on how many Os, Xs and blank spaces it contains
        the more Os that could form a winning formation, the higher the score
        the more Xs that could form a winning formation, the lower the score"""
        score = 0
        if window.count("O") == 4:
            score += 50
        elif window.count("O") == 3 and window.count(" ") == 1:
            score += 5
        elif window.count("O") == 2 and window.count(" ") == 2:
            score += 2
        elif window.count("O") == 1 and window.count(" ") == 3:
            score += 0
        elif window.count("X") == 3 and window.count(" ") == 1 and self.__difficulty==4:
            score -= 75
        elif window.count("X") == 2 and window.count(" ") == 2:
            score -= 3
        return score

    def __get_valid_locations(self,board):
        """function that returns a list of all possible columns on which a move is possible"""
        valid_locations = []
        for i in range(board.columns):
            if board.is_valid(i):
                valid_locations.append(i)
        return valid_locations

    def __minimax(self,board,depth,alpha, beta,maximizingPlayer):
        """the minimax algorithm driver
        returns a pair consisting of the best score achievable and the position an which the move should be played
        the "best score" value is also used internally for decision making"""
        valid_locations = self.__get_valid_locations(board)
        if depth == 0 or self.__engine.is_won()!=0 or len(valid_locations)==0:
            if self.__engine.is_won() == "Player 2":
                return 100, random.choice(valid_locations)
            elif self.__engine.is_won() == "Player 1":
                return -200, random.choice(valid_locations)
            elif self.__engine.is_won() == "Draw":
                return 0, 7
            elif len(valid_locations)==0:
                return  0, 7
            else:
                return self.__score_position(board), random.choice(valid_locations)
        if maximizingPlayer:
            value = -10000
            best_col = random.choice(valid_locations)
            for col in valid_locations:
                temp_board = deepcopy(board)
                temp_board.put_val(col,"O")
                new_score, pos = self.__minimax(temp_board,depth-1,alpha,beta,False)

                if new_score > value:
                    value = new_score
                    best_col = col
                alpha = max(alpha,value)
                if alpha>=beta:
                    break
            return value, best_col
        else:
            value = 10000
            best_col = random.choice(valid_locations)
            for col in valid_locations:
                temp_board = deepcopy(board)
                temp_board.put_val(col, "X")
                new_score, pos = self.__minimax(temp_board, depth - 1,alpha,beta, True)
                if new_score < value:
                    value = new_score
                    best_col = col
                beta = min(beta,value)
                if alpha>=beta:
                    break
            return value, best_col

    # def __best_move(self,board):
    # """function that determines the best move that can be played by the AI
    # --has been made obsolete after implementation of the minimax algorithm--"""
    #     valid_locations = self.__get_valid_locations(board)
    #     best_score = 0
    #     best_position = random.choice(valid_locations)
    #     for pos in valid_locations:
    #         temp_board = deepcopy(board)
    #         temp_board.put_val(pos,"O")
    #         score = self.__score_position(temp_board)
    #         if score > best_score:
    #             best_score = score
    #             best_position = pos
    #     return best_position