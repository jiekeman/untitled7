# -*- coding: utf-8 -*-
# @Time    : 2019-9-18 14:22
# @Author  : Jie ke man
# @FileName: 购物车程序.py
# @Software: PyCharm
'''
    购物车程序
        salary = 用户输入的金额
        商品列表
            1 iphone11 9000
            2.mac book  11000
            3.coffee   32
            4.python book 80
            5 bicycle  1500
        当选购商品金额不足时 输出余额不足,并输出缺多少钱
        当选购商品够的时候,输出某某商品已加入购物车,并输出余额
        输入quit 退出程序 并且打印出已经购买的商品
'''

goods = [('phone', 9000),
         ('mac book', 11000),
         ('coffee', 32),
         ('python book', 80),
         ('bicycle', 1500)]
shoppingCar = []
saving = input('your money:')
if saving.isdigit():
    saving = int(saving)
    while 1:
        print('商品列表:')
        for i, v in enumerate(goods, 1):
            print(i, v)
        choice = input('your product choice:')  # 商品选择输入

        if choice.isdigit():
            choice = int(choice)
            if 0 < choice <= len(goods):
                print('已经购买了:', end='')
                P_items = goods[choice-1]
                # print(P_items)
                if P_items[1] < saving:
                    shoppingCar.append(P_items)
                    saving -= P_items[1]
                    # print('you had buy %s,已经花费了%s' % shoppingCar, P_items[1])
                else:
                    print('Sorry, your credit is running low')
                print(P_items)
            else:
                print('Num is not exist')
        elif choice == 'q':
            print('------已经购买的商品-----')
            for j, o in enumerate(shoppingCar, 1):
                print(j, '.', o)
            print('余额为%s元钱' % saving)

        else:
            print('unable character')
else:
    print('unable character')
