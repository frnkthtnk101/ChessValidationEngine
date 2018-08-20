'''Enum is needed to conver the chess 'Columns' into numbers
alsp use to validate chess pieces.
'''
from enum import Enum
import argparse
import re
import sys


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


global CHESSBOARD
CHESSBOARD= [['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],  # 0
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
        if unit in WHITE_PIECES:
            return True
        return False
    if unit in BLACK_PIECES:
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

def pawn_movement(x_axis, y_axis, yourteam, enemyteam):
    '''Function to check for Pawn movement'''
    if in_range(y_axis):
        if in_range(x_axis) is True\
            and in_piece_list(yourteam, CHESSBOARD[y_axis][x_axis]) is False \
            and in_piece_list(enemyteam, CHESSBOARD[y_axis][x_axis]) is False:
            return  CHESSBOARD[y_axis][x_axis] + ' '
    return ''

def pawn_capture(x_axis, y_axis, enemyteam):
    '''Function to check if a pawn can capture'''
    if in_range(y_axis):
        if in_range(x_axis) is True\
            and in_piece_list(enemyteam, CHESSBOARD[y_axis][x_axis]):
            return CHESSBOARD[y_axis][x_axis] + ' '
    return ''

def pawn_special(x_axis, y_axis, yourteam, enemyteam):
    '''Function to check if the pawn has a special move'''
    if 8 - y_axis == 6:
        if in_piece_list(yourteam, CHESSBOARD[4][x_axis]) is False\
                and in_piece_list(enemyteam, CHESSBOARD[4][x_axis]) is False:
            return CHESSBOARD[4][x_axis] + ' '
    if 8 - y_axis == 1:
        if in_piece_list(yourteam, CHESSBOARD[3][x_axis]) is False\
                and in_piece_list(enemyteam, CHESSBOARD[3][x_axis]) is False:
            return CHESSBOARD[3][x_axis] + ' '
    return ''

def knight_movement(x_axis, y_axis, yourteam):
    '''Function to determin the moves is valid for the knight'''
    if in_range(8-y_axis):
        if in_range(x_axis):
            if in_piece_list(yourteam, CHESSBOARD[y_axis][x_axis]) is False:
                return CHESSBOARD[y_axis][x_axis] + ' '
    return ''

def rook_movement(x_axis, y_axis, plane, increment, yourteam, enemyteam):
    '''Determines how many moves the rook can make given one direction '''
    if plane == 'x':
        if in_range(x_axis + increment) \
                and in_piece_list(yourteam, CHESSBOARD[y_axis][x_axis + increment]) is False:
            if in_piece_list(enemyteam, CHESSBOARD[y_axis][x_axis + increment]):
                return CHESSBOARD[y_axis][x_axis + increment]
            return CHESSBOARD[y_axis][x_axis + increment] + " " + \
                   rook_movement(x_axis + increment, y_axis, plane, increment,
                                 yourteam, enemyteam)
    if plane == 'y':
        if in_range(y_axis + increment) \
                and in_piece_list(yourteam, CHESSBOARD[y_axis + increment][x_axis]) is False:
            if in_piece_list(enemyteam, CHESSBOARD[y_axis + increment][x_axis]):
                return CHESSBOARD[y_axis + increment][x_axis]
            return CHESSBOARD[y_axis + increment][x_axis] + " " + \
                   rook_movement(x_axis, y_axis + increment, plane, increment,
                                 yourteam, enemyteam)
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
                             CHESSBOARD[y_axis + increment[point][1]]
                             [x_axis + increment[point][0]]):
                return king_movement(x_axis, y_axis, yourteam, enemyteam, point + 1)
            return CHESSBOARD[y_axis + increment[point][1]][x_axis + increment[point][0]] + ' ' + \
                   king_movement(x_axis, y_axis, yourteam, enemyteam, point + 1)
        return king_movement(x_axis, y_axis, yourteam, enemyteam, point + 1)
    return ''

def print_chessboard(do_print):
    '''print chessboard if so bee'''
    if do_print:
        for i in range(0, len(CHESSBOARD)):
            for j in range(0, len(CHESSBOARD[i])):
                print(f"{CHESSBOARD[i][j]}", end=' ', flush=True)
            print()
def fix_chessboard(pieces):
    '''Function to put pieces on the chessboard'''
    for s_piece in pieces:
        plsplit = list(s_piece)
        CHESSBOARD[8 - int(plsplit[2])][give_column_number(plsplit[1])] = s_piece

def main(white_pieces, black_pieces, piece_to_move, Print_chessboard):
    '''the main function of the script'''
    #under normal circumstances WHITE_PIECES and BLACK_PIECES are normally GLOBAL,
    #but when they are being tested, They are not.
    global WHITE_PIECES, BLACK_PIECES
    WHITE_PIECES = white_pieces
    BLACK_PIECES = black_pieces
    fix_chessboard(white_pieces)
    fix_chessboard(black_pieces)
    print_chessboard(Print_chessboard)
    # decide if the piece moving is black or white
    if ''.join(piece_to_move) in white_pieces:
        piece_movement_team = 1
    elif ''.join(piece_to_move) in black_pieces:
        piece_movement_team = -1
    else:
        raise ValueError("Piece you are trying to move is not white set or black set.")
    enemy_team = piece_movement_team * -1
    # decide its move
    piece_x_axis = give_column_number(piece_to_move[1])
    piece_y_axis = int(piece_to_move[2])
    results = "Moves: "
    # pawn
    if piece_to_move[0] is PIECES.P.name:
        results += pawn_movement(piece_x_axis, 8 - (piece_y_axis + piece_movement_team),piece_movement_team,enemy_team)
        results +=pawn_capture(piece_x_axis + 1, 8- (piece_y_axis + piece_movement_team),enemy_team)
        results +=pawn_capture(piece_x_axis - 1, 8 - (piece_y_axis + piece_movement_team),enemy_team)
        results +=pawn_special(piece_x_axis, piece_y_axis, piece_movement_team, enemy_team)

    # knight
    elif piece_to_move[0] is PIECES.N.name:
        results +=knight_movement(piece_x_axis + 1, piece_y_axis + (piece_movement_team * 2),piece_movement_team)
        results +=knight_movement(piece_x_axis - 1, piece_y_axis + (piece_movement_team * 2),piece_movement_team)
        results +=knight_movement(piece_x_axis + 1, piece_y_axis + (piece_movement_team * -2),piece_movement_team)
        results +=knight_movement(piece_x_axis - 1, piece_y_axis + (piece_movement_team * -2),piece_movement_team)
        results +=knight_movement(piece_x_axis + 2, piece_y_axis + (piece_movement_team * 1),piece_movement_team)
        results +=knight_movement(piece_x_axis - 2, piece_y_axis + (piece_movement_team * 1),piece_movement_team)
        results +=knight_movement(piece_x_axis + 2, piece_y_axis + (piece_movement_team * -1),piece_movement_team)
        results +=knight_movement(piece_x_axis - 2, piece_y_axis + (piece_movement_team * -1),piece_movement_team)
    # Rook
    elif piece_to_move[0] is PIECES.R.name:
        results +=rook_movement(piece_x_axis, piece_y_axis, 'x', 1, piece_movement_team, enemy_team)
        results +=rook_movement(piece_x_axis, piece_y_axis, 'x', -1, piece_movement_team, enemy_team)
        results +=rook_movement(piece_x_axis, piece_y_axis, 'y', 1, piece_movement_team, enemy_team)
        results +=rook_movement(piece_x_axis, piece_y_axis, 'y', -1, piece_movement_team, enemy_team)
    # Bishop
    elif piece_to_move[0] is PIECES.B.name:
        results +=bishop_movement(piece_x_axis, piece_y_axis, 1, 1, piece_movement_team, enemy_team)
        results +=bishop_movement(piece_x_axis, piece_y_axis, 1, -1, piece_movement_team, enemy_team)
        results +=bishop_movement(piece_x_axis, piece_y_axis, -1, 1, piece_movement_team, enemy_team)
        results +=bishop_movement(piece_x_axis, piece_y_axis, -1, -1, piece_movement_team, enemy_team)
    elif piece_to_move[0] is PIECES.Q.name:
        results +=rook_movement(piece_x_axis, piece_y_axis, 'x', 1, piece_movement_team, enemy_team) + ' '
        results +=rook_movement(piece_x_axis, piece_y_axis, 'x', -1, piece_movement_team, enemy_team) + ' '
        results +=rook_movement(piece_x_axis, piece_y_axis, 'y', 1, piece_movement_team, enemy_team) + ' '
        results +=rook_movement(piece_x_axis, piece_y_axis, 'y', -1, piece_movement_team, enemy_team) + ' '
        results +=bishop_movement(piece_x_axis, piece_y_axis, 1, 1, piece_movement_team, enemy_team) + ' '
        results +=bishop_movement(piece_x_axis, piece_y_axis, 1, -1, piece_movement_team, enemy_team) + ' '
        results +=bishop_movement(piece_x_axis, piece_y_axis, -1, 1, piece_movement_team, enemy_team) + ' '
        results +=bishop_movement(piece_x_axis, piece_y_axis, -1, -1, piece_movement_team, enemy_team) + ' '
    elif piece_to_move[0] is PIECES.K.name:
        results += king_movement(piece_x_axis, piece_y_axis, piece_movement_team, enemy_team)
    print(results)
    return results

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('white', help="white pieces [KQRBNP][a-h][1-8],...", type=str)
    PARSER.add_argument('black', help='Black pieces [KQRBNP][a-h][1-8],...', type=str)
    PARSER.add_argument('piece', help='the moving piece [KQRBNP][a-h][1-8]', type=str)
    PARSER.add_argument('--chessboard', help='prints chessboard', type=bool)
    ARGS = PARSER.parse_args()
    if validate(ARGS.white) is not None \
            and validate(ARGS.black) is not None\
            and validate(ARGS.piece) is not None:
        WHITE_PIECES = ARGS.white.split(',')
        BLACK_PIECES = ARGS.black.split(',')
        PIECE_TO_MOVE = list(ARGS.piece)
        PRINTCB = ARGS.chessboard
        main(WHITE_PIECES, BLACK_PIECES, PIECE_TO_MOVE, PRINTCB)
    else:
        raise ValueError("One of the paramaters was out of format")
