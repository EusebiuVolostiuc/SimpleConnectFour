
class Human:
    def __init__(self,value):
        """value is used for storing the color/sign of the player"""
        self.__value = value

    def move(self,board,position):
        """the move of the player consists solely of putting a x/o
        on the specified position"""
        board.put_val(position, self.__value)