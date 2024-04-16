import pygame as pg
import random
import math

# color
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
light_blue = (200, 200, 255)
blue = (100, 100, 255)
white = (255, 255, 255)

# Game screen setup
window = pg.display.set_mode((1000, 700))

# Inicializando fonte
pg.font.init()
# Choosing a font and size
font = pg.font.SysFont("Courier New", 50, bold=True)

tray_data = [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']]

game_data = [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],

             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']]

hide_numbers = True
tray_filled = True
click_last_status = False
click_position_x = -1
click_position_y = -1
number = 0

def hover_board(window, mouse_position_x, mouse_position_y):
    square = 66.7
    adjustment = 50
    x = (math.ceil((mouse_position_x - adjustment) / square) - 1)
    y = (math.ceil((mouse_position_y - adjustment) / square) - 1)
    pg.draw.rect(window, white, (0, 0, 1000, 700))
    if x >= 0 and x <= 8 and y >= 0 and y <= 8:
        pg.draw.rect(window, light_blue, ((adjustment + x * square, adjustment + y * square, square, square)))

def cell_selected(window, mouse_position_x, mouse_position_y, click_last_status, click, x, y):
    square = 66.7
    adjustment = 50
    if click_last_status == True and click == True:
        x = (math.ceil((mouse_position_x - adjustment) / square) - 1)
        y = (math.ceil((mouse_position_y - adjustment) / square) - 1)
    if x >= 0 and x <= 8 and y >= 0 and y <= 8:
        pg.draw.rect(window, blue, ((adjustment + x * square, adjustment + y * square, square, square)))
    return x, y

def board(window):
    pg.draw.rect(window, black, (50, 50, 600, 600), 6)
    pg.draw.rect(window, black, (50, 250, 600, 200), 6)
    pg.draw.rect(window, black, (250, 50, 200, 600), 6)
    pg.draw.rect(window, black, (50, 117, 600, 67), 2)
    pg.draw.rect(window, black, (50, 317, 600, 67), 2)
    pg.draw.rect(window, black, (50, 517, 600, 67), 2)
    pg.draw.rect(window, black, (117, 50, 67, 600), 2)
    pg.draw.rect(window, black, (317, 50, 67, 600), 2)
    pg.draw.rect(window, black, (517, 50, 67, 600), 2)

def botton_restart(window):
    pg.draw.rect(window, green, (700, 50, 250, 100))
    palavra_f = font.render('Restart', True, black)
    window.blit(palavra_f, (725, 75))

def chosen_line(tabuleiro_data, y):
    drawn_line = tabuleiro_data[y]
    return drawn_line

def chosen_column(tabuleiro_data, x):
    coluna_sorteada = []
    for n in range(8):
        coluna_sorteada.append(tabuleiro_data[n][x])
    return coluna_sorteada

def selected_quadrant(tray_data, x, y):
    quadrant = []
    if x >= 0 and x <= 2 and y >= 0 and y <= 2:
        quadrant.extend([tray_data[0][0], tray_data[0][1], tray_data[0][2],
                         tray_data[1][0], tray_data[1][1], tray_data[1][2],
                         tray_data[2][0], tray_data[2][1], tray_data[2][2]])
    elif x >= 3 and x <= 5 and y >= 0 and y <= 2:
        quadrant.extend([tray_data[0][3], tray_data[0][4], tray_data[0][5],
                         tray_data[1][3], tray_data[1][4], tray_data[1][5],
                         tray_data[2][3], tray_data[2][4], tray_data[2][5]])
    elif x >= 6 and x <= 8 and y >= 0 and y <= 2:
        quadrant.extend([tray_data[0][6], tray_data[0][7], tray_data[0][8],
                         tray_data[1][6], tray_data[1][7], tray_data[1][8],
                         tray_data[2][6], tray_data[2][7], tray_data[2][8]])
    elif x >= 0 and x <= 2 and y >= 3 and y <= 5:
        quadrant.extend([tray_data[3][0], tray_data[3][1], tray_data[3][2],
                         tray_data[4][0], tray_data[4][1], tray_data[4][2],
                         tray_data[5][0], tray_data[5][1], tray_data[5][2]])
    elif x >= 3 and x <= 5 and y >= 3 and y <= 5:
        quadrant.extend([tray_data[3][3], tray_data[3][4], tray_data[3][5],
                         tray_data[4][3], tray_data[4][4], tray_data[4][5],
                         tray_data[5][3], tray_data[5][4], tray_data[5][5]])
    elif x >= 6 and x <= 8 and y >= 3 and y <= 5:
        quadrant.extend([tray_data[3][6], tray_data[3][7], tray_data[3][8],
                         tray_data[4][6], tray_data[4][7], tray_data[4][8],
                         tray_data[5][6], tray_data[5][7], tray_data[5][8]])
    elif x >= 0 and x <= 2 and y >= 6 and y <= 8:
        quadrant.extend([tray_data[6][0], tray_data[6][1], tray_data[6][2],
                         tray_data[7][0], tray_data[7][1], tray_data[7][2],
                         tray_data[8][0], tray_data[8][1], tray_data[8][2]])
    elif x >= 3 and x <= 5 and y >= 6 and y <= 8:
        quadrant.extend([tray_data[6][3], tray_data[6][4], tray_data[6][5],
                         tray_data[7][3], tray_data[7][4], tray_data[7][5],
                         tray_data[8][3], tray_data[8][4], tray_data[8][5]])
    elif x >= 6 and x <= 8 and y >= 6 and y <= 8:
        quadrant.extend([tray_data[6][6], tray_data[6][7], tray_data[6][8],
                         tray_data[7][6], tray_data[7][7], tray_data[7][8],
                         tray_data[8][6], tray_data[8][7], tray_data[8][8]])
    return quadrant

def filled_quadrant(tray_data, x2, y2):
    filled_quadrant = True
    loop = 0
    try_count = 0
    number = 1

    while filled_quadrant == True:
        x = random.randint(x2, x2 + 2)
        y = random.randint(y2, y2 + 2)
        drawn_line = chosen_line(tray_data, y)
        draw_collumn = chosen_column(tray_data, x)
        quadrante = selected_quadrant(tray_data, x, y)
        if tray_data[y][x] == 'n' and number not in drawn_line and number not in draw_collumn and number not in quadrante:
            tray_data[y][x] = number
            number += 1
        loop += 1
        if loop == 50:
            tray_data[y2][x2] = 'n'
            tray_data[y2][x2 + 1] = 'n'
            tray_data[y2][x2 + 2] = 'n'
            tray_data[y2 + 1][x2] = 'n'
            tray_data[y2 + 1][x2 + 1] = 'n'
            tray_data[y2 + 1][x2 + 2] = 'n'
            tray_data[y2 + 2][x2] = 'n'
            tray_data[y2 + 2][x2 + 1] = 'n'
            tray_data[y2 + 2][x2 + 2] = 'n'
            loop = 0
            number = 1
            try_count += 1
        if try_count == 10:
            break
        count = 0
        for n in range(9):
            if quadrante[n] != 'n':
                count += 1
        if count == 9:
            filled_quadrant = False
    return tray_data

def reset_data_board(tabuleiro_data):
    tabuleiro_data = [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']]
    return tabuleiro_data

def board_template(board_data, board_complet):
    while board_complet == True:
        board_data = filled_quadrant(board_data, 0, 0)
        board_data = filled_quadrant(board_data, 3, 0)
        board_data = filled_quadrant(board_data, 6, 0)
        board_data = filled_quadrant(board_data, 0, 3)
        board_data = filled_quadrant(board_data, 0, 6)
        board_data = filled_quadrant(board_data, 3, 3)
        board_data = filled_quadrant(board_data, 3, 6)
        board_data = filled_quadrant(board_data, 6, 3)
        board_data = filled_quadrant(board_data, 6, 6)
        for nn in range(9):
            for n in range(9):
                if board_data[nn][n] == 'n':
                    board_data = reset_data_board(board_data)
        count = 0
        for nn in range(9):
            for n in range(9):
                if board_data[nn][n] != 'n':
                    count += 1
        if count == 81:
            board_complet = False
    return board_data, board_complet

def hiding_numbers(board_data, game_data, hide_numbers):
    if hide_numbers == True:
        for n in range(40):
            drawing_numbers = True
            while drawing_numbers == True:
                x = random.randint(0, 8)
                y = random.randint(0, 8)
                if game_data[y][x] == 'n':
                    game_data[y][x] = board_data[y][x]
                    drawing_numbers = False
        hide_numbers = False
    return game_data, hide_numbers

def writing_numbers(window, game_data):
    square = 66.7
    adjustment = 67
    for nn in range(9):
        for n in range(9):
            if game_data[nn][n] != 'n':
                palavra = font.render(str(game_data[nn][n]), True, black)
                window.blit(palavra, (adjustment + n * square, adjustment - 5 + nn * square))
                if game_data[nn][n] == 'X':
                    palavra = font.render(str(game_data[nn][n]), True, red)
                    window.blit(palavra, (adjustment + n * square, adjustment - 5 + nn * square))

def typing_number(number):
    try:
        number = int(number[1])
    except:
        number = int(number)
    return number

def Checking_Entered_Number(window, tray_data, game_data, click_position_x, click_position_y, number):
    x = click_position_x
    y = click_position_y
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and tray_data[y][x] == number and game_data[y][x] == 'n' and number != 0:
        game_data[y][x] = number
        number = 0
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and tray_data[y][x] == number and game_data[y][x] == number and number != 0:
        pass
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and tray_data[y][x] != number and game_data[y][x] == 'n' and number != 0:
        game_data[y][x] = 'X'
        number = 0
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and tray_data[y][x] == number and game_data[y][x] == 'X' and number != 0:
        game_data[y][x] = number
        number = 0
    return game_data, number

def click_botton_restart(mouse_position_x, mouse_position_y, click_last_status, click, filled_board, hide_numbers, tray_data, game_data):
    x = mouse_position_x
    y = mouse_position_y
    if x >= 700 and x <= 950 and y >= 50 and y <= 150 and click_last_status == False and click == True:
        filled_board = True
        hide_numbers = True
        tray_data = reset_data_board(tray_data)
        game_data = reset_data_board(game_data)
    return filled_board, hide_numbers, tray_data, game_data

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            number = pg.key.name(event.key)

    mouse = pg.mouse.get_pos()
    mouse_position_x = mouse[0]
    mouse_position_y = mouse[1]

    click = pg.mouse.get_pressed()

    hover_board(window, mouse_position_x, mouse_position_y)
    click_position_x, click_position_y = cell_selected(window, mouse_position_x, mouse_position_y, click_last_status, click[0], click_position_x, click_position_y)
    board(window)
    botton_restart(window)
    tray_data, tray_filled = board_template(tray_data, tray_filled)
    game_data, hide_numbers = hiding_numbers(tray_data, game_data, hide_numbers)
    writing_numbers(window, game_data)
    number = typing_number(number)
    game_data, number = Checking_Entered_Number(window, tray_data, game_data, click_position_x, click_position_y, number)
    tray_filled, hide_numbers, tray_data, game_data= click_botton_restart(mouse_position_x, mouse_position_y, click_last_status, click[0], tray_filled, hide_numbers, tray_data, game_data)

    # Click Last Status
    if click[0] == True:
        click_last_status = True
    else:
        click_last_status = False

    pg.display.update()