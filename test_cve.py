'''Tests the features of the cve script'''
from cve import main, reset_chessboard
with open('useCases.txt', 'r') as file:
    READ_DATA = file.readlines()
FAILURES = 0
for line in range(1, len(READ_DATA)):
    reset_chessboard()
    params = READ_DATA[line].replace('\n', '').split('\t')
    whites = params[0].split(',')
    WHITE_PIECES = params[0].split(',')
    blacks = params[1].split(',')
    piece = list(params[2])
    answers = params[3].split(' ')
    print('==========================================================')
    print("moving: {0}".format(''.join(piece)))
    return_results = main(whites, blacks, piece, False).split(': ')[1].split(' ')
    print("white  :", whites)
    print("black  :", blacks)
    print("results:", sorted(return_results))
    print("answers:", sorted(answers))
    for i in range(len(return_results)):
        if return_results[i] != '':
            if return_results[i] not in answers:
                print("Failed...")
                failures = FAILURES + 1
                break
    print('==========================================================')
print("number of test: {0}\r\nnumber of failures: {1}\r\n".format(len(READ_DATA), FAILURES))
