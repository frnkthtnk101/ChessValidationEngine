import os
from cve import *
with open('useCases.txt', 'r') as file:
    read_data = file.readlines()
for line in range(1, len(read_data)):
    params = read_data[line].replace('\n', '').split('\t')
    whites = params[0].split(',')
    WHITE_PIECES = params[0].split(',')
    blacks = params[1].split(',')
    #globals( BLACK_PIECES = params[1].split(','))
    piece = list(params[2])
    answers =  params[3].split(' ')
    print('==========================================================')
    print ("{0}".format(''.join(piece)))
    s =  main(whites, blacks, piece, False)
    print(s, flush=False)
    print(answers)
    print('==========================================================')

