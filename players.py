# 切片，可指定要使用的第一个元素和最后一个元素的索引。 第一个元素缺省，默认从第一个元素开始；最后一个元素缺省，默认到最后一个元素结束
# 注意列表下标从0开始
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
# print(players[0:3])
# print(players[1:4])
# print(players[:4])
# print(players[2:])
#
# # 负数索引返回离列表末尾相应距离的元素
# print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())



