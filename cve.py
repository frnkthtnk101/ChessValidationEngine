from enum import Enum
import argparse
import re

class ROWS(Enum): #change to Columns
    a=0
    b=1
    c=2
    d=3
    e=4
    f=5
    g=6
    h=7

CHESSBOARD = [['A8','B8','C8','D8','E8','F8','G8','H8'],
              ['A7','B7','C7','D7','E7','F7','G7','H7'],
              ['A6','B6','C6','D6','E6','F6','G6','H6'],
              ['A5','B5','C5','D5','E5','F5','G5','H5'],
              ['A4','B4','C4','D4','E4','F4','G4','H4'],
              ['A3','B3','C3','D3','E3','F3','G3','H3'],
              ['A2','B2','C2','D2','E2','F2','G2','H2'],
              ['A1','B1','C1','D1','E1','F1','G1','H1']]

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
        for piece in WhitePieces:
            plsplit = list(piece)
            if(ROWS.a.name is plsplit[1]):
                x = ROWS.a.value
            elif(ROWS.b.name is plsplit[1]):
                x = ROWS.b.value
            elif(ROWS.c.name is plsplit[1]):
                x = ROWS.c.value
            elif(ROWS.d.name is plsplit[1]):
                x = ROWS.d.value
            elif(ROWS.e.name is plsplit[1]):
                x = ROWS.e.value
            elif(ROWS.f.name is plsplit[1]):
                x = ROWS.f.value
            elif(ROWS.g.name is plsplit[1]):
                x = ROWS.g.value
            elif(ROWS.h.name is plsplit[1]):
                x = ROWS.h.value
            CHESSBOARD[8-int(plsplit[2])][x]=piece
        for piece in BlackPieces:
            plsplit = list(piece)
            if(ROWS.a.name is plsplit[1]):
                x = ROWS.a.value
            elif(ROWS.b.name is plsplit[1]):
                x = ROWS.b.value
            elif(ROWS.c.name is plsplit[1]):
                x = ROWS.c.value
            elif(ROWS.d.name is plsplit[1]):
                x = ROWS.d.value
            elif(ROWS.e.name is plsplit[1]):
                x = ROWS.e.value
            elif(ROWS.f.name is plsplit[1]):
                x = ROWS.f.value
            elif(ROWS.g.name is plsplit[1]):
                x = ROWS.g.value
            elif(ROWS.h.name is plsplit[1]):
                x = ROWS.h.value
            CHESSBOARD[8-int(plsplit[2])][x]=piece
        for i in range(0,len(CHESSBOARD)):
            for j in range(0,len(CHESSBOARD[i])):
                 print(CHESSBOARD[i][j],end=' ',flush=True)
            print()
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



        
