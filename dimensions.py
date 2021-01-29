dimensions = (200, 5)
# print(dimensions[0])
# print(dimensions[1])

# 元组不能直接赋值 可理解为静态数组
# dimensions[0] = 250

# 相比于列表，元组是更简单的数据结构。如果需要存储的一组值在程序的整个生命周期内都不变，可使用元组

# print("Original dimensions:")
# for dimension in dimensions:
#     print(dimension)
#
# dimensions = (400, 100)
# print("\nModified dimensions:")
# for dimension in dimensions:
#     print(dimension)

# 4-13
buffet = ('面包', '饺子', '米饭', '面条', '酸辣粉')
# buffet[0] = '螺蛳粉'

buffet = ('面包', '饺子', '米饭', '牛排', '酸菜鱼')
print(buffet)
for food in buffet:
    print(food)


