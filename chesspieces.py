from enum import Enum
CHESSBOARD = [['A8','B8','C8','D8','E8','F8','G8','H8'],
              ['A7','B7','C7','D7','E7','F7','G7','H7'],
              ['A6','B6','C6','D6','E6','F6','G6','H6'],
              ['A5','B5','C5','D5','E5','F5','G5','H5'],
              ['A4','B4','C4','D4','E4','F4','G4','H4'],
              ['A3','B3','C3','D3','E3','F3','G3','H3'],
              ['A2','B2','C2','D2','E2','F2','G2','H2'],
              ['A1','B1','C1','D1','E1','F1','G1','H1']]
CONST_CHESSBOARDLENGTH = 8
class PIECES(Enum):
    K=1
    Q=2
    R=3
    B=4
    N=5
    P=6

class ROWS(Enum): #change to Columns
    a=0
    b=1
    c=2
    d=3
    e=4
    f=5
    g=6
    h=7

class SIDES(Enum):
    BLACK = 1
    WHITE = 2

class ChessPiece():
    def __init__(self, PieceLocation, side):
        plsplit = list(PieceLocation)
        self.y = int(plsplit[2])
        self.side = side.value
        if(ROWS.a.name is plsplit[1]):
            self.x = ROWS.a.value
        elif(ROWS.b.name is plsplit[1]):
            self.x = ROWS.b.value
        elif(ROWS.c.name is plsplit[1]):
            self.x = ROWS.c.value
        elif(ROWS.d.name is plsplit[1]):
            self.x = ROWS.d.value
        elif(ROWS.e.name is plsplit[1]):
            self.x = ROWS.e.value
        elif(ROWS.f.name is plsplit[1]):
            self.x = ROWS.f.value
        elif(ROWS.g.name is plsplit[1]):
            self.x = ROWS.g.value
        elif(ROWS.h.name is plsplit[1]):
            self.x = ROWS.h.value
        if(PIECES.K.name is plsplit[0]):
            self.PieceType = PIECES.K.value
        elif(PIECES.Q.name is plsplit[0]):
            self.PieceType = PIECES.Q.value
        elif(PIECES.R.name is plsplit[0]):
            self.PieceType = PIECES.R.value
        elif(PIECES.N.name is plsplit[0]):
            self.PieceType = PIECES.N.value
        elif(PIECES.B.name is plsplit[0]):
            self.PieceType = PIECES.B.value
        elif(PIECES.P.name is plsplit[0]):
            self.PieceType = PIECES.P.value
        
class Pawn(ChessPiece):
    def __init__(self,PieceLocation, side):
        ChessPiece.__init__(self,PieceLocation, side)
        if(side.name is SIDES.BLACK.name):
            self.movement = -1
            self.JumpLine = 1
        else:
            self.movement = 1
            self.JumpLine = 6
    def RegularMove(self):
        if(self.JumpLine is 8-self.y):
            return CHESSBOARD[8-(self.y+self.movement)][self.x] , CHESSBOARD[8-(self.y+(self.movement*2))][self.x]
        return CHESSBOARD[8-(self.y+self.movement)][self.x]
    def CurrentLocation(self):
        return 8-self.y,self.x
    
class Rook
