'''Enum is needed to conver the chess 'Columns' into numbers
alsp use to validate chess pieces.
'''
from enum import Enum
import argparse
import re


class COLUMNS(Enum):
    '''changes the letter value into a number so it can be used by script
     to Manipulate the variable Chessboard'''
    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    f = 5
    g = 6
    h = 7


class PIECES(Enum):
    '''Enumerator used to validate the chosen chess piece'''
    K = 1
    Q = 2
    R = 3
    B = 4
    N = 5
    P = 6


CHESSBOARD = [['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],  # 0
              ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],  # 1
              ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],  # 2
              ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],  # 3`
              ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],  # 4
              ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],  # 5
              ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],  # 6
              ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']]  # 7


# 0    1     2     3      4     5     6     7

def in_range(cord):
    '''determines if the given value is between or equal to 0 and 7'''
    if 0 <= cord <= 7:
        return True
    return False


def in_piece_list(side, unit):
    '''Returns true id the piece in question is in the piece list'''
    if side is 1:
        if unit in WhitePieces:
            return True
        return False
    if unit in BlackPieces:
        return True
    return False


def give_column_number(letter):
    '''determines the letter in question numeric value is'''
    value = None
    if COLUMNS.a.name is letter:
        value = COLUMNS.a.value
    elif COLUMNS.b.name is letter:
        value = COLUMNS.b.value
    elif COLUMNS.c.name is letter:
        value = COLUMNS.c.value
    elif COLUMNS.d.name is letter:
        value = COLUMNS.d.value
    elif COLUMNS.e.name is letter:
        value = COLUMNS.e.value
    elif COLUMNS.f.name is letter:
        value = COLUMNS.f.value
    elif COLUMNS.g.name is letter:
        value = COLUMNS.g.value
    elif COLUMNS.h.name is letter:
        value = COLUMNS.h.value
    return value


def validate(string, option=1):
    '''Validates that the parameter given is syntax correct'''
    if option is 1:
        regex = r"^([KQRBNP][a-h][1-8],?\s?)+$"
    else:
        regex = r"^([KQRBNP])([a-h])([1-8])$"
    return re.match(regex, string)


def rook_movement(x_axis, y_axis, plane, increment, yourteam, enemyteam):
    '''Determines how many moves the rook can make given one direction '''
    if plane == 'x':
        if in_range(x_axis + increment):
            if in_piece_list(yourteam, CHESSBOARD[y_axis][x_axis + increment]):
                return ''
            if in_piece_list(enemyteam, CHESSBOARD[y_axis][x_axis + increment]):
                return CHESSBOARD[y_axis][x_axis + increment]
            return CHESSBOARD[y_axis][x_axis + increment] + " " + \
                   rook_movement(x_axis + increment, y_axis, plane, increment,
                                 yourteam, enemyteam)
        return ''
    if plane == 'y':
        if in_range(y_axis + increment):
            if in_piece_list(yourteam, CHESSBOARD[y_axis + increment][x_axis]):
                return ''
            if in_piece_list(enemyteam, CHESSBOARD[y_axis + increment][x_axis]):
                return CHESSBOARD[y_axis + increment][x_axis]
            return CHESSBOARD[y_axis + increment][x_axis] + " " + \
                   rook_movement(x_axis, y_axis + increment, plane, increment,
                                 yourteam, enemyteam)
        return ''
    return ''


def bishop_movement(x_axis, y_axis, xincrement, yincrement, yourteam, enemyteam):
    '''function to show the valid moves of a bishop.'''
    if in_range(x_axis + xincrement) and in_range(y_axis + yincrement):
        if in_piece_list(yourteam, CHESSBOARD[y_axis + yincrement][x_axis + xincrement]):
            return ''
        if in_piece_list(enemyteam, CHESSBOARD[y_axis + yincrement][x_axis + xincrement]):
            return CHESSBOARD[y_axis + yincrement][x_axis + xincrement]
        return CHESSBOARD[y_axis + yincrement][x_axis + xincrement] + ' ' + \
               bishop_movement(x_axis + xincrement, y_axis + yincrement, \
                               xincrement, yincrement, yourteam, enemyteam)
    return ''


def king_movement(x_axis, y_axis, yourteam, enemyteam, point=0):
    '''function to show the valid moves of a king'''
    increment = [[0, 1], [0, -1], [1, 0], [1, 1], [1, -1],
                 [-1, 0], [-1, 1], [-1, -1]]
    if point < len(increment):
        if in_range(x_axis + increment[point][0]) and in_range(y_axis + increment[point][1]):
            if in_piece_list(yourteam,
                             CHESSBOARD[y_axis + increment[point][1]][x_axis + increment[point][0]]):
                return king_movement(x_axis, y_axis, yourteam, enemyteam, point + 1)
            return CHESSBOARD[y_axis + increment[point][1]][x_axis + increment[point][0]] + ' ' + \
                   king_movement(x_axis, y_axis, yourteam, enemyteam, point + 1)
        return king_movement(x_axis, y_axis, yourteam, enemyteam, point + 1)
    return ''


def main():
    '''the main function of the script'''
    for w_piece in WhitePieces:
        plsplit = list(w_piece)
        CHESSBOARD[8 - int(plsplit[2])][give_column_number(plsplit[1])] = w_piece
    for b_piece in BlackPieces:
        plsplit = list(b_piece)
        CHESSBOARD[8 - int(plsplit[2])][give_column_number(plsplit[1])] = b_piece
    for i in range(0, len(CHESSBOARD)):
        for j in range(0, len(CHESSBOARD[i])):
            print(f"{CHESSBOARD[i][j]}", end=' ', flush=True)
        print()
    # decide if the piece moving is black or white
    if args.piece in WhitePieces:
        piece_movement_team = 1
    elif args.piece in BlackPieces:
        piece_movement_team = -1
    else:
        raise ValueError("Piece you are trying to move is not white set or black set.")
    enemy_team = piece_movement_team * -1
    # decide its move
    piece_x_axis = give_column_number(PieceToMove[1])
    piece_y_axis = int(PieceToMove[2])
    print("Moves: ", end="", flush=True)
    # pawn
    if PieceToMove[0] is PIECES.P.name:
        if piece_movement_team is 1:
            if 8 - piece_y_axis is 6:
                print(CHESSBOARD[8 - (piece_y_axis + piece_movement_team + piece_movement_team)]
                      [piece_x_axis], end=" ", flush=True)
            if CHESSBOARD[7 - piece_y_axis][piece_x_axis + 1] in BlackPieces:
                print(CHESSBOARD[7 - piece_y_axis][piece_x_axis + 1], end=" ", flush=True)
            if CHESSBOARD[7 - piece_y_axis][piece_x_axis - 1] in BlackPieces:
                print(CHESSBOARD[7 - piece_y_axis][piece_x_axis - 1], end=" ", flush=True)
        else:
            if 8 - piece_y_axis is 1:
                print(CHESSBOARD[8 - (piece_y_axis + piece_movement_team + piece_movement_team)]
                      [piece_x_axis], end=" ", flush=True)
            if CHESSBOARD[9 - piece_y_axis][piece_x_axis + 1] in WhitePieces:
                print(CHESSBOARD[9 - piece_y_axis][piece_x_axis + 1], end=" ", flush=True)
            if CHESSBOARD[9 - piece_y_axis][piece_x_axis - 1] in WhitePieces:
                print(CHESSBOARD[9 - piece_y_axis][piece_x_axis - 1], end=" ", flush=True)
        if in_range(8 - (piece_y_axis + piece_movement_team)):
            if CHESSBOARD[8 - (piece_y_axis + piece_movement_team)][piece_x_axis] not in WhitePieces \
                    and CHESSBOARD[8 - (piece_y_axis + piece_movement_team)][piece_x_axis] \
                    not in BlackPieces:
                print(CHESSBOARD[8 - (piece_y_axis + piece_movement_team)][piece_x_axis],
                      end=" ", flush=True)
    # knight
    elif PieceToMove[0] is PIECES.N.name:
        if in_range(8 - (piece_y_axis + (piece_movement_team * 2))):
            if in_range(piece_x_axis + 1):
                if in_piece_list(enemy_team,
                                 CHESSBOARD[8 - (piece_y_axis + (piece_movement_team * 2))]
                                 [piece_x_axis + 1]) is False:
                    print(CHESSBOARD[8 - (piece_y_axis + (piece_movement_team * 2))]
                          [piece_x_axis + 1], end=" ", flush=True)
            if in_range(piece_x_axis - 1):
                if in_piece_list(enemy_team,
                                 CHESSBOARD[8 - (piece_y_axis + (piece_movement_team * 2))] is False):
                    print(CHESSBOARD[8 - (piece_y_axis + (piece_movement_team * 2))][piece_x_axis - 1],
                          end=" ", flush=True)
        if in_range(8 - (piece_y_axis + (piece_movement_team * -2))):
            if in_range(piece_x_axis + 1):
                if in_piece_list(enemy_team,
                                 CHESSBOARD[8 - (piece_y_axis + (piece_movement_team * -2))]
                                 [piece_x_axis + 1]) is False:
                    print(CHESSBOARD[8 - (piece_y_axis + (piece_movement_team * -2))][piece_x_axis + 1],
                          end=" ", flush=True)
            if in_range(piece_x_axis - 1):
                if in_piece_list(enemy_team,
                                 CHESSBOARD[8 - (piece_y_axis + (piece_movement_team * -2))]
                                 [piece_x_axis - 1]) is False:
                    print(CHESSBOARD[8 - (piece_y_axis + (piece_movement_team * -2))]
                          [piece_x_axis - 1],
                          end=" ", flush=True)
        if in_range(8 - (piece_y_axis + (piece_movement_team * 1))):
            if in_range(piece_x_axis - 2):
                if in_piece_list(enemy_team,
                                 CHESSBOARD[8 - (piece_y_axis + (piece_movement_team * 1))]
                                 [piece_x_axis - 2]) is False:
                    print(CHESSBOARD[8 - (piece_y_axis + (piece_movement_team * 1))]
                          [piece_x_axis - 2],
                          end=" ", flush=True)
            if in_range(piece_x_axis + 2):
                if in_piece_list(enemy_team,
                                 CHESSBOARD[8 - (piece_y_axis + (piece_movement_team * 1))]
                                 [piece_x_axis + 2]) is False:
                    print(CHESSBOARD[8 - (piece_y_axis + (piece_movement_team * 1))][piece_x_axis + 2],
                          end=" ", flush=True)
        if in_range(8 - (piece_y_axis + (piece_movement_team * -1))):
            if in_range(piece_x_axis + 2):
                if in_piece_list(enemy_team,
                                 CHESSBOARD[8 - (piece_y_axis + (piece_movement_team * -1))]
                                 [piece_x_axis + 2]) is False:
                    print(CHESSBOARD[8 - (piece_y_axis + (piece_movement_team * -1))][piece_x_axis + 2],
                          end=" ", flush=True)
            if in_range(piece_x_axis - 2):
                if in_piece_list(enemy_team,
                                 CHESSBOARD[8 - (piece_y_axis + (piece_movement_team * -1))]
                                 [piece_x_axis - 2]) is False:
                    print(CHESSBOARD[8 - (piece_y_axis + (piece_movement_team * -1))][piece_x_axis - 2],
                          end=" ", flush=True)
    # Rook
    elif PieceToMove[0] is PIECES.R.name:
        print(rook_movement(piece_x_axis, piece_y_axis, 'x', 1, piece_movement_team, enemy_team),
              end=' ', flush=True)
        print(rook_movement(piece_x_axis, piece_y_axis, 'x', -1, piece_movement_team, enemy_team),
              end=' ', flush=True)
        print(rook_movement(piece_x_axis, piece_y_axis, 'y', 1, piece_movement_team, enemy_team),
              end=' ', flush=True)
        print(rook_movement(piece_x_axis, piece_y_axis, 'y', -1, piece_movement_team, enemy_team),
              end=' ', flush=True)
    # Bishop
    elif PieceToMove[0] is PIECES.B.name:
        print(bishop_movement(piece_x_axis, piece_y_axis, 1, 1, piece_movement_team, enemy_team),
              end=' ', flush=True)
        print(bishop_movement(piece_x_axis, piece_y_axis, 1, -1, piece_movement_team, enemy_team),
              end=' ', flush=True)
        print(bishop_movement(piece_x_axis, piece_y_axis, -1, 1, piece_movement_team, enemy_team),
              end=' ', flush=True)
        print(bishop_movement(piece_x_axis, piece_y_axis, -1, -1, piece_movement_team, enemy_team),
              end=' ', flush=True)
    elif PieceToMove[0] is PIECES.Q.name:
        print(rook_movement(piece_x_axis, piece_y_axis, 'x', 1, piece_movement_team, enemy_team),
              end=' ', flush=True)
        print(rook_movement(piece_x_axis, piece_y_axis, 'x', -1, piece_movement_team, enemy_team),
              end=' ', flush=True)
        print(rook_movement(piece_x_axis, piece_y_axis, 'y', 1, piece_movement_team, enemy_team),
              end=' ', flush=True)
        print(rook_movement(piece_x_axis, piece_y_axis, 'y', -1, piece_movement_team, enemy_team),
              end=' ', flush=True)
        print(bishop_movement(piece_x_axis, piece_y_axis, 1, 1, piece_movement_team, enemy_team),
              end=' ', flush=True)
        print(bishop_movement(piece_x_axis, piece_y_axis, 1, -1, piece_movement_team, enemy_team),
              end=' ', flush=True)
        print(bishop_movement(piece_x_axis, piece_y_axis, -1, 1, piece_movement_team, enemy_team),
              end=' ', flush=True)
        print(bishop_movement(piece_x_axis, piece_y_axis, -1, -1, piece_movement_team, enemy_team),
              end=' ', flush=True)
    elif PieceToMove[0] is PIECES.K.name:
        print(king_movement(piece_x_axis, piece_y_axis, piece_movement_team, enemy_team))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('white', help="white pieces [KQRBNP][a-h][1-8],...", type=str)
    parser.add_argument('black', help='Black pieces [KQRBNP][a-h][1-8],...', type=str)
    parser.add_argument('piece', help='the moving piece [KQRBNP][a-h][1-8]', type=str)

    args = parser.parse_args()

    piece = args.piece

    WhiteSet = validate(args.white)
    BlackSet = validate(args.black)
    MovingPiece = validate(args.piece, 1)

    if WhiteSet is not None and BlackSet is not None and MovingPiece is not None:
        WhitePieces = args.white.split(',')
        BlackPieces = args.black.split(',')
        PieceToMove = list(args.piece)
        main()
    else:
        raise ValueError("One of the paramaters was out of format")
