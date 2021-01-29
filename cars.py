# cars = ['bmw', 'audi', 'toyota', 'subaru']

# # 按照ASCII排序
# cars.sort()
# print(cars)
#
# # 在参数内添加反转参数True,排序反转，修改是永久性的
# cars.sort(reverse=True)
# print(cars)

# print("Here is the original list:")
# print(cars)
#
# # sorted()让你能够按特定顺序显示列表元素，同时不影响它们在列表中的原始排列顺序, 向函数sorted()传递参数reverse=True。
# print("\nHere is the original list:")
# print(sorted(cars))
#
# print(sorted(cars, reverse=True))
#
# print("\nHere is the original list again:")
# print(cars)

# reverse()不是指按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排 列顺序
# cars.reverse()
# print(cars)

# len()  快速获悉列表的长度
# 注意 Python计算列表元素数时从1开始， 因此确定列表长度时，你应该不会遇到差一错误。
# print(len(cars))

# 3-8
# country = ['Japan', 'Germany', 'Iceland', 'France', 'Belarus']
# print(country)
# print(sorted(country))
# print(country)
# print(sorted(country, reverse=True))
# print(country)
# country.reverse()
# country.reverse()
# print(country)
# country.sort()
# print(country)
# country.sort(reverse=True)
# print(country)

# 3-9
# print(len(country))

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bwm':
        print(car.upper())
    else:
        print(car.title())






