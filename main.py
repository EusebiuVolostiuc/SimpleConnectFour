"""Here lies the initialisation of the program"""
if __name__ == "__main__":
    from res.board import board
    board = board()
    from res.human import Human
    from res.ai import AI
    players = {"hX": Human("X"),"hO":Human("O")}
    from res.engine import engine
    engine = engine(board,players)
    players["AIeasy"]=AI(engine,1)
    players["AImedium"] = AI(engine, 2)
    players["AIhard"] = AI(engine, 3)
    from res.console import console
    console = console(engine,board)



