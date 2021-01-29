# current_number = 1
#
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# x = 1
# while x <= 5:
#     print(x)
#     x += 1

# 缺少退出循环条件，变成死循环
# x = 1
# while x <= 5:
#     print(x)

# 7-4
# massage = ''
# while massage != 'quit':
#     massage = input()
#     if massage != 'quit':
#         print("我们会在比萨中添加这种配料：" + massage)

# 7-5
# age = 0
# while True:
#     age = input()
#     if age == 'quit':
#         break
#     else:
#         age = int(age)
#         if age < 3:
#             print("票价免费")
#         elif age <= 12:
#             print("票价10美元")
#         elif age > 12:
#             print("票价15美元")

# 7-6
# active = True
# while active:
#     age = input()
#     if age == 'quit':
#         # active = False
#         break
#     else:
#         age = int(age)
#         if age < 3:
#             print("票价免费")
#         elif age <= 12:
#             print("票价10美元")
#         elif age > 12:
#             print("票价15美元")

# 7-7
# while True:
#     info = input()
#     print(info)


# for循环是一种遍历列表的有效方式，但在for循环中不应修改列表，否则将导致Python难以跟踪其中的元素。
# 要在遍历列表的同时对其进行修改，可使用while循环。
