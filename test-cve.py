import os
from cve import *
with open('useCases.txt', 'r') as file:
    read_data = file.readlines()
failures = 0
for line in range(1, len(read_data)):
    reset_chessboard()
    params = read_data[line].replace('\n', '').split('\t')
    whites = params[0].split(',')
    WHITE_PIECES = params[0].split(',')
    blacks = params[1].split(',')
    #globals( BLACK_PIECES = params[1].split(','))
    piece = list(params[2])
    answers =  params[3].split(' ')
    print('==========================================================')
    print ("moving: {0}".format(''.join(piece)))
    return_results =  main(whites, blacks, piece,False).split(': ')[1].split(' ')
    print("white  :",whites)
    print("black  :",blacks)
    print("results:",sorted(return_results), flush=False)
    print("answers:",sorted(answers))
    for i in range(len(return_results)):
        if return_results[i] != '':
            if return_results[i] not in answers:
                print("Failed...")
                failures = failures + 1
                break
    print('==========================================================')
print("number of test: {0}\r\nnumber of failures: {1}\r\n".format(len(read_data),failures))
