import random
import math

BOARD_SIZE = 5  # ボードの初期サイズ

# print(random.randrange(0, 5))

# def calc_distance(x1, y1, x2, y2):
#     diff_x = x1 - x2
#     diff_y = y1 - y2

#     return math.sqrt(diff_x**2 + diff_y**2)

def calc_distance(pos1, pos2):
    diff_x = pos1[0] - pos2[0]
    diff_y = pos1[1] - pos2[1]

    return math.sqrt(diff_x**2 + diff_y**2)

# スイカの位置を決める
# suika_x = random.randrange(0, BOARD_SIZE)  # スイカのx座標
# suika_y = random.randrange(0, BOARD_SIZE)  # スイカのy座標

suika_pos = (random.randrange(0, BOARD_SIZE), random.randrange(0, BOARD_SIZE))

# プレイヤーの位置を決める
# player_x = random.randrange(0, BOARD_SIZE)  # プレイヤーのx座標
# player_y = random.randrange(0, BOARD_SIZE)  # プレイヤーのy座標

player_pos = (random.randrange(0, BOARD_SIZE), random.randrange(0, BOARD_SIZE)) 

# while (suika_x != player_x) or (suika_y != player_y):
while suika_pos != player_pos:

    distance = calc_distance(suika_pos, player_pos)
    print('スイカへの距離:', distance)

    c = input("n:北に移動 s:南に移動 e:東に移動 w:西に移動")
    player_x, player_y = player_pos
    if c == "n":
        player_y = player_y - 1
    elif c == "s":
        player_y = player_y + 1
    elif c == "w":
        player_x = player_x - 1
    elif c == "e":
        player_x = player_x + 1
    
    player_pos = (player_x, player_y)

print('スイカが割れました')    

