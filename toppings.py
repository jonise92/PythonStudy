# requested_topping = 'mushrooms'
#
# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")

# requested_toppings = ['mushrooms', 'extra cheese']
# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")
#
# print("\nFinished making your pizza!")

# 5-3
# alien_color = ('green', 'yellow', 'red')
# if 'green' in alien_color:
#     print("玩家获得了5分")
#
# if 'black' in alien_color:
#     print("玩家获得了10分")

# 5-4
# if 'green' in alien_color:
#     print("玩家获得了5分")
# else:
#     print("玩家获得了10分")
#
# if 'black' in alien_color:
#     print("玩家获得了5分")
# else:
#     print("玩家获得了10分")

# 5-5
# color = 'green'
# color = 'yellow'
# color = 'red'

# if color == 'green':
#     print("玩家获得了5分")
# elif color == 'yellow':
#     print("玩家获得了10分")
# elif color in 'red':
#     print("玩家获得了15分")

# 5-6
# age = 12
# if age < 2:
#     print('他是婴儿')
# elif age < 4:
#     print('他正蹒跚学步')
# elif age < 13:
#     print('他是儿童')
# elif age < 20:
#     print('他是青少年')
# elif age < 65:
#     print('他是成年人')
# else:
#     print('他是老年人')

# 5-7
# fruits = ['apple', 'pear', 'watermelon', 'bananas']
# if 'apple' in fruits:
#     print('You really like apple!')
# if 'pear' in fruits:
#     print('You really like pear!')
# if 'watermelon' in fruits:
#     print('You really like watermelon!')

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
#
# for requested_topping in requested_toppings:
#
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print("Adding " + requested_topping + ".")
#
# print("\nFinished making your pizza!")

# requested_toppings = []
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print("Adding " + requested_topping + ".")
#     print("\nFinished making your pizza!")
# else:
#     print('Are you sure you want a plain pizza?')

# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
#                       'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
#
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print("Adding " + requested_topping + ".")
#     else:
#         print("Sorry, we don't have " + requested_topping + ".")
# print("\nFinished making your pizza!")

# 5-8 5-9
# users = ['admin', 'user1', 'user2', 'user3', 'user4']
# # 删除所有元素
# del users[-len(users):]
# # users = []
# if users:
#     for user in users:
#         if user == 'admin':
#             print('Hello admin, would you like to see a status report?')
#         else:
#             print('Hello Eric, thank you for logging in again')
# else:
#     print('We need to find some users!')

# 5-10
# current_users = ['user1', 'user2', 'user3', 'user4', 'user5', 'John']
# new_users = ['user4', 'user5', 'user6', 'user7', 'user8', 'JOHN']
# for new_user in new_users:
#     if new_user.lower() in [current_user.lower() for current_user in current_users]:
#         print('用户名重复')
#     else:
#         print('用户名可用')

# 5-11  列表生成两种方法

# 直接使用list函数效率最高
number1 = list(range(10))
# 列表解析稍慢
# number = [num for num in range(10)]
# print(number)

# 注意python打印时候int型变量需要用str()函数转化使用
# for number in number1:
#     if number == 1:
#         print(str(number) + 'st')
#     elif number == 2:
#         print(str(number) + 'st')
#     elif number == 3:
#         print(str(number) + 'st')
#     elif number == 4:
#         print(str(number) + 'st')
#     elif number == 5:
#         print(str(number) + 'st')
#     elif number == 6:
#         print(str(number) + 'st')
#     elif number == 7:
#         print(str(number) + 'st')
#     elif number == 8:
#         print(str(number) + 'st')
#     elif number == 9:
#         print(str(number) + 'st')
#     else:
#         print(str(number) + 'st')

# if in 区分大小写
# test1 = ['a', 'b', 'c', 'John']
# test2 = ['A', 'B', 'C', 'JOHN']
#
# if test1[3] in test2:
#     print('不区分大小写')
# else:
#     print('区分大小写')

