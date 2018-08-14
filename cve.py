import argparse
import re

def validate(string,option =1):
    if option is 1:
        regex = r"^([KQRBNP][a-h][1-8],?\s?)+$"
    else:
        regex = r"^([KQRBNP])([a-h])([1-8])$"
    return re.match(regex,string)

def Main():
        WhitePieces =args.white.split(',')
        BlackPieces = args.black.split(',')
        PieceToMove = args.piece

        


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('white', help = "white pieces [KQRBNP][a-h][1-8],...", type = str)
    parser.add_argument('black', help = 'Black pieces [KQRBNP][a-h][1-8],...', type = str)
    parser.add_argument('piece', help = 'the moving piece [KQRBNP][a-h][1-8]', type = str)

    args = parser.parse_args()

 
    piece       = args.piece

    WhiteSet=validate(args.white)
    BlackSet=validate(args.black)
    MovingPiece=validate(args.piece,1)

    if WhiteSet is not None and BlackSet is not None and MovingPiece is not None:
        Main()
    else:
        raise ValueError("One of the paramaters was out of format")



        
