from enum import Enum
import argparse
import re

class COLUMNS(Enum): #change to Columns
    a=0
    b=1
    c=2
    d=3
    e=4
    f=5
    g=6
    h=7

class PIECES(Enum):
    K=1
    Q=2
    R=3
    B=4
    N=5
    P=6


CHESSBOARD = [['a8','b8','c8','d8','e8','f8','g8','h8'],#0
              ['a7','b7','c7','d7','e7','f7','g7','h7'],#1
              ['a6','b6','c6','d6','e6','f6','g6','h6'],#2
              ['a5','b5','c5','d5','e5','f5','g5','h5'],#3`
              ['a4','b4','c4','d4','e4','f4','g4','h4'],#4
              ['a3','b3','c3','d3','e3','f3','g3','h3'],#5
              ['a2','b2','c2','d2','e2','f2','g2','h2'],#6
              ['a1','b1','c1','d1','e1','f1','g1','h1']]#7
                #0   1    2     3    4    5    6    7
def InRange(cord):
    if cord >= 0 and cord <= 7 :
        return True
    return False
def InPieceList(side, unit):
    if side is 1:
        if unit in WhitePieces:
            return True
        return False
    else:
        if unit in BlackPieces:
            return True
        return False

def GiveColumnNumber(letter):
    if(COLUMNS.a.name is letter):
        return COLUMNS.a.value
    elif(COLUMNS.b.name is letter):
        return COLUMNS.b.value
    elif(COLUMNS.c.name is letter):
        return COLUMNS.c.value
    elif(COLUMNS.d.name is letter):
        return COLUMNS.d.value
    elif(COLUMNS.e.name is letter):
        return COLUMNS.e.value
    elif(COLUMNS.f.name is letter):
        return COLUMNS.f.value
    elif(COLUMNS.g.name is letter):
        return COLUMNS.g.value
    elif(COLUMNS.h.name is letter):
        return COLUMNS.h.value

def validate(string,option =1):
    if option is 1:
        regex = r"^([KQRBNP][a-h][1-8],?\s?)+$"
    else:
        regex = r"^([KQRBNP])([a-h])([1-8])$"
    return re.match(regex,string)

def RookMovement(x,y,plane,increment,yourteam,enemyteam):
    if plane is 'x':
        if InRange(x+increment):
            if InPieceList(yourteam,CHESSBOARD[y][x+increment]):
                return ''
            elif InPieceList(enemyteam,CHESSBOARD[y][x+increment]):
                return CHESSBOARD[y][x+increment]
            else:
                return CHESSBOARD[y][x+increment]+" "+RookMovement(x+increment,y,plane,increment,yourteam,enemyteam)
        else:
            return ''
    elif plane is 'y':
        if InRange(y+increment):
            if InPieceList(yourteam,CHESSBOARD[y+increment][x]):
                return ''
            elif InPieceList(enemyteam,CHESSBOARD[y+increment][x]):
                return CHESSBOARD[y+increment][x]
            else:
                return CHESSBOARD[y+increment][x]+" "+RookMovement(x,y+increment,plane,increment,yourteam,enemyteam)
        else:
            return ''
    return ''

def BishopMovement(x,y,xincrement,yincrement,yourteam,enemyteam):
    if InRange(x+xincrement) and InRange(y+yincrement):
        if InPieceList(yourteam,CHESSBOARD[y+yincrement][x+xincrement]):
            return ''
        elif InPieceList(enemyteam,CHESSBOARD[y+yincrement][x+xincrement]):
            return CHESSBOARD[y+yincrement][x+xincrement]
        else:
            h = CHESSBOARD[y][x]
            d = CHESSBOARD[(y+yincrement)][x+xincrement]
            return CHESSBOARD[y+yincrement][x+xincrement]+' '+BishopMovement(x+xincrement,y+yincrement,xincrement,yincrement,yourteam,enemyteam)
    else:
        return ''
def Main():

        for piece in WhitePieces:
            plsplit = list(piece)
            CHESSBOARD[8-int(plsplit[2])][GiveColumnNumber(plsplit[1])]=piece
        for piece in BlackPieces:
            plsplit = list(piece)
            CHESSBOARD[8-int(plsplit[2])][GiveColumnNumber(plsplit[1])]=piece
        for i in range(0,len(CHESSBOARD)):
            for j in range(0,len(CHESSBOARD[i])):
                 print(CHESSBOARD[i][j],end=' ',flush=True)
            print()
        #decide if the piece moving is black or white
        if(args.piece in WhitePieces):
            movement =  1
        elif(args.piece in BlackPieces):
            movement = -1
        else:
            raise ValueError("Piece you are trying to move is not white set or black set.")
        team = movement * -1
        #decide its move
        x = GiveColumnNumber(PieceToMove[1])
        y = int(PieceToMove[2])
        print("Moves: ",end="",flush=True)
        #pawn
        if(PieceToMove[0] is PIECES.P.name):
            if movement is 1:
                if 8-y is 6:
                    print(CHESSBOARD[8 - (y + movement + movement)][x],end=" ",flush=True)
                if CHESSBOARD[7-y][x+1] in BlackPieces:
                    print(CHESSBOARD[7-y][x+1],end=" ",flush=True)
                if CHESSBOARD[7-y][x-1] in BlackPieces:
                    print(CHESSBOARD[7-y][x-1],end=" ",flush=True)
            else:
                if 8-y is 1:
                    print(CHESSBOARD[8 - (y + movement + movement)][x], end=" ", flush=True)
                if CHESSBOARD[9-y][x+1] in WhitePieces:
                    print(CHESSBOARD[9-y][x+1],end=" ",flush=True)
                if CHESSBOARD[9-y][x-1] in WhitePieces:
                    print(CHESSBOARD[9-y][x-1],end=" ",flush=True)
            if InRange(8-(y+movement)):
                if CHESSBOARD[8-(y+movement)][x] not in WhitePieces and CHESSBOARD[8-(y+movement)][x] not in BlackPieces:
                    print(CHESSBOARD[8-(y+movement)][x],end=" ",flush=True)
        #knight
        elif PieceToMove[0] is PIECES.N.name:
            if InRange(8 - (y + (movement * 2))):
                if InRange(x+1):
                    if InPieceList(team,CHESSBOARD[8 - (y + (movement * 2))] [x + 1]) is False:
                        print(CHESSBOARD[8 - (y + (movement * 2))] [x + 1],end=" ",flush=True)
                if InRange(x-1):
                    if InPieceList(team,CHESSBOARD[8 - (y + (movement * 2))] is False):
                        print(CHESSBOARD[8 - (y + (movement * 2))] [x - 1],end=" ",flush=True)
            if InRange(8 - (y + (movement * -2))):
                if InRange(x + 1):
                    if InPieceList(team,CHESSBOARD[8 - (y + (movement * -2))][x + 1]) is False:
                        print(CHESSBOARD[8 - (y + (movement * -2))][x + 1],end=" ",flush=True)
                if InRange(x - 1):
                    if InPieceList(team, CHESSBOARD[8 - (y + (movement * -2))][x - 1]) is False:
                        print(CHESSBOARD[8 - (y + (movement * -2))][x - 1],end=" ",flush=True)
            if InRange(8 - (y + (movement * 1))) :
                if InRange(x - 2):
                    if InPieceList(team,CHESSBOARD[8 - (y + (movement * 1))] [x - 2]) is False:
                        print(CHESSBOARD[8 - (y + (movement * 1))] [x - 2],end=" ",flush=True)
                if InRange(x +2):
                    if InPieceList(team, CHESSBOARD[8 - (y + (movement * 1))][x + 2]) is False:
                        print(CHESSBOARD[8 - (y + (movement * 1))] [x + 2],end=" ",flush=True)
            if InRange(8 - (y + (movement * -1))):
                if InRange(x + 2):
                    if InPieceList(team,CHESSBOARD[8 - (y + (movement * -1))][x + 2]) is False:
                        print(CHESSBOARD[8 - (y + (movement * -1))][x + 2],end=" ",flush=True)
                if InRange(x - 2):
                    if InPieceList(team, CHESSBOARD[8 - (y + (movement * -1))][x - 2]) is False:
                        print(CHESSBOARD[8 - (y + (movement * -1))][x - 2],end=" ",flush=True)
        #Rook
        elif PieceToMove[0] is PIECES.R.name:
            print(RookMovement(x,y,'x',1,movement,team),end=' ',flush=True)
            print(RookMovement(x, y, 'x', -1, movement, team), end=' ', flush=True)
            print(RookMovement(x, y, 'y', 1, movement, team), end=' ', flush=True)
            print(RookMovement(x, y, 'y', -1, movement, team), end=' ', flush=True)
        #Bishop
        elif PieceToMove[0] is PIECES.B.name:
            print(BishopMovement(x,y,1,1,movement,team),end=' ',flush=True)
            print(BishopMovement(x,y,1,-1, movement, team), end=' ', flush=True)
            print(BishopMovement(x, y, -1, 1, movement, team), end=' ', flush=True)
            print(BishopMovement(x, y, -1, -1, movement, team), end=' ', flush=True)
        elif PieceToMove[0] is PIECES.Q.name:
            print(RookMovement(x,y,'x',1,movement,team),end=' ',flush=True)
            print(RookMovement(x, y, 'x', -1, movement, team), end=' ', flush=True)
            print(RookMovement(x, y, 'y', 1, movement, team), end=' ', flush=True)
            print(RookMovement(x, y, 'y', -1, movement, team), end=' ', flush=True)
            print(BishopMovement(x,y,1,1,movement,team),end=' ',flush=True)
            print(BishopMovement(x,y,1,-1, movement, team), end=' ', flush=True)
            print(BishopMovement(x, y, -1, 1, movement, team), end=' ', flush=True)
            print(BishopMovement(x, y, -1, -1, movement, team), end=' ', flush=True)
        elif PieceToMove[0] is PIECES.K.name:
            




        
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('white', help = "white pieces [KQRBNP][a-h][1-8],...", type = str)
    parser.add_argument('black', help = 'Black pieces [KQRBNP][a-h][1-8],...', type = str)
    parser.add_argument('piece', help = 'the moving piece [KQRBNP][a-h][1-8]', type = str)

    args = parser.parse_args()


    piece = args.piece

    WhiteSet=validate(args.white)
    BlackSet=validate(args.black)
    MovingPiece=validate(args.piece,1)

    if WhiteSet is not None and BlackSet is not None and MovingPiece is not None:
        WhitePieces =args.white.split(',')
        BlackPieces = args.black.split(',')
        PieceToMove = list(args.piece)
        Main()
    else:
        raise ValueError("One of the paramaters was out of format")



        
