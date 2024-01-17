import turtle
import keyboard
import shapes
import time
import random

# Tomasz Edison w domu

LENG = 32
TIME = 0.5
SCORE = 0


def kwadrat(col):
    turtle.pendown()
    turtle.fillcolor(col)
    turtle.begin_fill()
    for _ in range(4):
        turtle.fd(LENG)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()


def grid(plansza):
    turtle.clear()
    turtle.penup()
    turtle.hideturtle()
    turtle.setpos(-150, 300)
    for y in plansza:
        for x in y:
            if x == '#':
                kwadrat(shapes.colors[-1])
            else:
                kwadrat(shapes.colors[int(x)])
            turtle.fd(LENG)
        turtle.bk(LENG * len(y))
        turtle.right(90)
        turtle.fd(LENG)
        turtle.left(90)


def update_grid(plansza):
    nksztalt = random.choice(shapes.shapes)
    nksztalt = nksztalt.split()

    for y in range(4):
        for x in range(4):
            if plansza[y + 1][x + 4] == '8':
                print('Konice gry!\nWyczyszczone linie: {}'.format(SCORE))
                exit()
            plansza[y + 1][x + 4] = nksztalt[y][x]

    return plansza


def czyszczenie(plansza):
    global SCORE
    zm = 0
    usun = []
    for y in range(len(plansza)):
        if ''.join(plansza[y]) == '#8888888888#':
            usun.append(y)
            zm += 1
            SCORE += 1
    while list('#8888888888#') in plansza:
        plansza.remove(list('#8888888888#'))
    for i in range(zm):
        plansza.insert(1, list('#0000000000#'))
    return plansza


def szare(plansza):
    for y in range(len(plansza)):
        for x in range(len(plansza[y])):
            if plansza[y][x] != '0' and plansza[y][x] != '#':
                plansza[y][x] = '8'

    return update_grid(plansza)


def wszystko_sie_rusza(plansza):
    war = True
    for y in range(len(plansza) - 1, 0, -1):
        for x in range(1, len(plansza[y]) - 1):
            if plansza[y][x] != '0' and plansza[y][x] != '#' and plansza[y][x] != '8':
                if plansza[y + 1][x] == '#' or plansza[y + 1][x] == '8':
                    war = False
    if war:
        for y in range(len(plansza) - 1, 0, -1):
            for x in range(1, len(plansza[y]) - 1):
                if plansza[y][x] != '0' and plansza[y][x] != '#' and plansza[y][x] != '8':
                    plansza[y + 1][x], plansza[y][x] = plansza[y][x], '0'
    else:
        return szare(plansza)
    return plansza


def mleft(plansza):
    war = 1
    for y in range(len(plansza) - 1, 0, -1):
        for x in range(1, len(plansza[y]) - 1):
            if plansza[y][x] != '#' and plansza[y][x] != '0' and plansza[y][x] != '8':
                if plansza[y][x - 1] == '#' or plansza[y][x - 1] == '8':
                    war = 0
    if war:
        for y in range(len(plansza) - 1, 0, -1):
            for x in range(1, len(plansza[y]) - 1):
                if plansza[y][x] != '#' and plansza[y][x] != '0' and plansza[y][x] != '8':
                    if plansza[y][x - 1] != '#' and plansza[y][x - 1] != '8':
                        plansza[y][x - 1], plansza[y][x] = plansza[y][x], plansza[y][x - 1]
    return plansza


def mright(plansza):
    war = 1
    for y in range(len(plansza) - 1, 0, -1):
        for x in range(1, len(plansza[y]) - 1):
            if plansza[y][x] != '#' and plansza[y][x] != '0' and plansza[y][x] != '8':
                if plansza[y][x + 1] == '#' or plansza[y][x + 1] == '8':
                    war = 0
    if war:
        for y in range(len(plansza) - 1, 0, -1):
            for x in range(len(plansza[y]) - 1, 0, -1):
                if plansza[y][x] != '#' and plansza[y][x] != '0' and plansza[y][x] != '8':
                    if plansza[y][x + 1] != '#' and plansza[y][x + 1] != '8':
                        plansza[y][x + 1], plansza[y][x] = plansza[y][x], plansza[y][x + 1]
    return plansza


def czyszczenie2(plansza):
    for y in range(len(plansza)):
        for x in range(len(plansza[y])):
            if plansza[y][x] != '#' and plansza[y][x] != '0' and plansza[y][x] != '8':
                plansza[y][x] = '0'
    return plansza


def obroc(pl4x4):
    pl4x4[3][0], pl4x4[2][0], pl4x4[1][0], pl4x4[0][0], pl4x4[3][1], pl4x4[2][1], pl4x4[1][1], pl4x4[0][1], pl4x4[3][2], pl4x4[2][2], pl4x4[1][2], pl4x4[0][2], pl4x4[3][3], pl4x4[2][3], pl4x4[1][3], pl4x4[0][3] = pl4x4[0][0], pl4x4[0][1], pl4x4[0][2], pl4x4[0][3], pl4x4[1][0], pl4x4[1][1], pl4x4[1][2], pl4x4[1][3], pl4x4[2][0], pl4x4[2][1], pl4x4[2][2], pl4x4[2][3], pl4x4[3][0], pl4x4[3][1], pl4x4[3][2], pl4x4[3][3]
    return pl4x4


def locate(plansza):
    lista = [[] for _ in range(4)]
    i = 0
    for y in range(len(plansza)):
        for x in range(len(plansza[y])):
            if plansza[y][x] != '#' and plansza[y][x] != '0' and plansza[y][x] != '8':
                lista[i] = plansza[y]
                i += 1
                break

    for i in range(len(lista)):
        if len(lista[i]) == 0:
            lista[i] = list('#0000000000#')

    zostaw = []
    lista2 = [[] for _ in range(4)]

    for j in range(len(lista[0])):
        war = 0
        for k in range(4):
            if lista[k][j] != '0' and lista[k][j] != '8' and lista[k][j] != '#':
                war = 1
        if war:
            zostaw.append(j)

    for i in range(4):
        for j in zostaw:
            lista2[i].append(lista[i][j])
        while len(lista2[i]) != 4:
            lista2[i].append('0')

    lista2 = obroc(lista2)
    war = 1
    for y in range(len(plansza)):
        for x in range(len(plansza[y])):
            if plansza[y][x] != '#' and plansza[y][x] != '0' and plansza[y][x] != '8':
                try:
                    for y2 in range(len(lista2)):
                        for x2 in range(len(lista2[y2])):
                            if plansza[y + y2 - 1][x + x2] == '8' or plansza[y + y2 - 1][x + x2] == '#':
                                raise IndexError
                except IndexError:
                    war = 0
                if war:
                    plansza = czyszczenie2(plansza)
                    for y2 in range(len(lista2)):
                        for x2 in range(len(lista2[y2])):
                            plansza[y + y2 - 1][x + x2] = lista2[y2][x2]
                return plansza


if __name__ == '__main__':
    screen = turtle.Screen()
    turtle.tracer(0, 1)
    turtle.speed(0)
    MAIN_GRID = update_grid(shapes.main_grid)
    start = time.time()
    while True:
        if keyboard.is_pressed('a'):
            MAIN_GRID = mleft(MAIN_GRID)
            grid(MAIN_GRID)
            screen.update()
            time.sleep(0.05)

        if keyboard.is_pressed('d'):
            MAIN_GRID = mright(MAIN_GRID)
            grid(MAIN_GRID)
            screen.update()
            time.sleep(0.05)

        if keyboard.is_pressed('s'):
            MAIN_GRID = wszystko_sie_rusza(MAIN_GRID)
            grid(MAIN_GRID)
            screen.update()
            time.sleep(0.05)

        if keyboard.is_pressed('w'):
            MAIN_GRID = locate(MAIN_GRID)
            grid(MAIN_GRID)
            screen.update()
            time.sleep(0.05)

        stop = time.time()
        if stop - start > TIME:
            MAIN_GRID = czyszczenie(MAIN_GRID.copy())
            MAIN_GRID = wszystko_sie_rusza(MAIN_GRID.copy())
            grid(MAIN_GRID)
            screen.update()
            start = time.time()
