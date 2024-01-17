square = '''
0110
0110
0000
0000
'''

line = '''
0200
0200
0200
0200
'''

tblock = '''
0333
0030
0000
0000
'''

lblock = '''
4000
4000
4400
0000
'''

jblock = '''
0500
0500
5500
0000
'''

sblock = '''
0660
6600
0000
0000
'''

zblock = '''
7700
0770
0000
0000
'''

main_grid = '''
############
#0000000000#
#0000000000#
#0000000000#
#0000000000#
#0000000000#
#0000000000#
#0000000000#
#0000000000#
#0000000000#
#0000000000#
#0000000000#
#0000000000#
#0000000000#
#0000000000#
#0000000000#
#0000000000#
#0000000000#
############
'''


main_grid_copy = '''
############
#0000000000#
#0000000000#
#0000000000#
#0000000000#
#0000000000#
#0000000000#
#0000000000#
#0000000000#
#0000000000#
#0000000000#
#0000000000#
#0000000000#
#0000000888#
#8888888888#
#0880808800#
#8888888888#
#8880000880#
############
'''

main_grid = [list(x) for x in main_grid.split()]


colors = ['white', 'yellow', 'cyan', 'purple',
          'orange', 'blue', 'green', 'red', 'grey', 'black']

shapes = [square, line, tblock, lblock, jblock, sblock, zblock]

if __name__ == '__main__':
    from itertools import permutations
    lista = [x for x in range(1, 16)]
    lista = list(permutations(lista, 2))
    print(lista)
    om = 0
    w = 0
    for elem in lista:
        if elem[0] == elem[1]:
            print(f'{elem}')
            continue
        if elem[0] * elem[1] % 2 == 0:
            print(elem)
            w += 1
        om += 1
    print(w, '/', om, len(lista))