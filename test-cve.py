import os
with open('useCases.txt', 'r') as file:
    read_data = file.readlines()
for line in read_data:
    params = line.replace('\n','').split('\t')
    whites = params[0]
    blacks = params[1]
    piece = params[2]
    os.system('python3.7 test-cve.py {0} {1} {2}'.format(whites, blacks, piece))

