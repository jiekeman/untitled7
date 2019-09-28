#
# 2.增删改查
# dic[key] = value  当这个键没有存在字典中就是添加
# dic.setdefault(key,value) 如果这个键存在字典中 就不进行添加 否则就添加
#
# 删除
# pop(key)              有返回值返回的是被删除的value
# del dic[key]
# popitem()             随机删除
# clear()               清空字典
#
# 修改
# dic[key]=value  当这个键存在字典中时,强行修改value
# dic.update(字典)
#
#
# 查
# get(key)
# dic[key]
# for 循环    拿到所有的key
# setdefault(key)
# print(dic[key])
# 3.字典的其他操作
#  keys   获取到所有键存在一个高仿列表
# values  获取到所有的值存在一个高仿列表
# items   获取到所有的键值对 以元祖的形式存在一个高仿列表中
# 解构(解包) 将后面结构打开按位置复制给变量 支持str list tuple
# a, b = (1, 2)
# a, b = 1,2
# a,b = [1,2]
# print(a)
# print(b)

# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# dic = {'k1': [], 'k2': []}
# for i in li:
#     if i == 66:
#         continue
#     elif i > 66:
#         dic['k1'].append(i)
#     else:
#         dic['k2'].append(i)
# print(dic)

# 要求:
#    1. 页面显示序号+商品名称+商品价格,如:
# #       1 电脑 1999
# #       2 鼠标 10
# # ......
# # 2 用户输入选择的商品序号 然后打印商品名称及商品价格
# # 3 如果用户输入的商品序号有误 提示输入错误 重新输入
# # 4 用户输入Q或者q  退出程序
# goods = [{'name': 'computer', 'price': '1900'},
#          {'name': 'mouse', 'price': '10'},
#          {'name': 'beautiful girl', 'price': '20000'},
#          {'name': 'yacht', 'price': '30000'}, ]
# while 1:
#     for i in goods:
#         print(goods.index(i)+1, i['name'], i['price'])
#
#     str_input = input('请输入您要选择的商品,输入Q退出:')
#
#     if str_input.isdigit() and 0 < int(str_input) < len(goods):
#         # i_index = int(str_input) - 1
#         print(goods[int(str_input)-1]['name'], goods[int(str_input)-1]['price'])
#     elif str_input.upper() == 'Q':
#         pass
#     else:
#         print('输入错误,重新输入!')

