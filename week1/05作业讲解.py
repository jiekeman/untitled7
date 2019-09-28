# 1.老男孩好声音选秀大赛评委打分的时候,可以进行输入,
# 有10个评委,让10个评委依次打分,分数必须大于5分小于10分
# count = 1
# while count <= 10:
#     fen = int(input('请第%s号评委评分:' % count))
#     if fen < 5 or fen > 10:
#         print("超出范围,请重新输入")
#         continue
#     else:
#         print('第%s号评委打%s分' % (count, fen))
#     count += 1
# 2.车牌区域划分
# cars = ['鲁A3244', '鲁B2133', '京A8989M', '皖M5897']
# local = {'鲁': '山东', '京': '北京', '皖': '安徽'}
# result = {}
# for i in cars:
#     name = i[0]
#     location = local[name]
#     if result.get(location) == None:
#         result[location] = 1
#     else:
#         result[location] += 1
# print(result)
# index = 1
# while index < 11:
#     index = index + 1
#     if index == 8:
#         # break
#         pass
#         # continue
#     else:
#         print(index)
# else:
#     print('你好')
# 1*1=1
# 1*2=2 2*2=4
# 1*3=3 2*3=6 3*3=9
# num1 = 0
# num2 = 0
# while num2 < 9:
#     while num1 < 9:
#         num1 += 1
#         print(num1, end='')
#     num2 += 1
# print()




# num1 = 4
# while num1 > 0:
#     num = 4
#     while num > 0:
#         print('#', end='')
#         num -= 1
#     print()
#     num1 -= 1
# print('#', end='')

# line = 5
# while line > 0:
#     # print('*')
#     temp = line
#     while temp > 0:
#         temp -= 1
#         print('*', end='')
#     print()
#     line -= 1

# first = 1
# while first < 10:
#     sec = 1
#     while sec <= first:
#         print(str(sec) + '*' + str(first) + '=', sec*first, end='\t')
#         sec += 1
#     print()
#     first += 1
