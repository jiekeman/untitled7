# -*- coding: utf-8 -*-
# @Time    : 2019-9-19 10:28
# @Author  : Jie Ke Man
# @FileName: 省市县三级菜单.py
# @Software: PyCharm
menu = {
    '北京': {
        '海定区': {'中关村'},
        '朝阳区': {'望京': {'Sou hou', '三元桥'}},
        '通州区': {'中国人民大学', '森林公园'}},
    '安徽': {'合肥市': {'瑶海区', '蜀山区', '包河区'}, '滁州市': {'南谯区', '琅琊区'}
           }
        }
C_player = menu
fatherPlayer = []
while True:
    for key in C_player:
        print(key)
    choice = input('>>>:').strip()
    if len(choice) == 0:
        continue
    if choice in C_player:
        fatherPlayer.append(C_player)
        C_player = C_player[choice]

    elif choice == 'b':
        if fatherPlayer:
            C_player = fatherPlayer.pop()
    else:
        print('indent character')
