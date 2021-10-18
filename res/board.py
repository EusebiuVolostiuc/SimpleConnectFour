class board:
    def __init__(self):
        self.__rows = 6
        self.__col = 7
        self.__board = [[" " for i in range(self.__col)] for j in range(self.__rows)]
        self.__xList = []
        self.__oList = []

    def reset(self):
        """function that resets the board to the initial state"""
        for i in self.__board:
            for j in range(self.__col):
                i[j] = " "
        while len(self.__xList) != 0:
            del self.__xList[0]
        while len(self.__oList) != 0:
            del self.__oList[0]
        # self.__xList = []
        # self.__oList = []

    def get_val(self,val):
        """returns the list of positions where <val> is in the matrix in the form of integers
        eg. there is an X on column 4 line 3. In self.__xList there will be a 43"""
        if val == 'X':
            return self.__xList
        elif val == 'O':
            return self.__oList
        else:
            return -1

    def put_val(self, pos, val):
        """ads <vaL> at <pos> just like in the irl game. If the column indicated by <pos> is full, returns -1"""
        if self.__board[0][pos] != " ":
            return -1
        i = 0
        while (i+1 < self.__rows and self.__board[i+1][pos] == " "):
            i += 1
        self.__board[i][pos] = val
        if val == "X":
            self.__xList.append(int(str(i)+str(pos)))
        elif val == "O":
            self.__oList.append(int(str(i) + str(pos)))
        else: raise ValueError(f"<val> argument different from X/O")
        return 0

    @property
    def columns(self):
        return self.__col

    @property
    def rows(self):
        return self.__rows

    def get_row(self,row):
        """returns a list corresponding to the selected row"""
        return self.__board[row]

    def get_column(self,column):
        """returns a list corresponding to the selected column"""
        col = []
        for i in range(self.__rows):
            col.append(self.__board[i][column])
        return col

    def get_matrix(self):
        return self.__board

    def is_valid(self,position):
        """checks if the column indicated by <position> has any slots left. returns 1 if it has, else 0"""
        if self.__board[0][position]== ' ':
            return 1
        else:
            return 0