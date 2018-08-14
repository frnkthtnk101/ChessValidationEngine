from enum import Enum

class PIECES(Enum):
    K=1
    Q=2
    R=3
    B=4
    N=5
    P=6

class SIDES(Enum):
    BLACK = 1
    WHITE = 2


    
class ChessPiece():
    def __INIT__(self,piece,side):
        self._Self = self
        self._Piece= piece
        self._Side = side
        
        
