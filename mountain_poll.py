# responses = {}
# # 设置一个标志，指出调查是否继续
# polling_active = True
# while polling_active:
#     # 提示输入被调查者的名字和回答
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday?")
#
#     # 将答卷存储在字典中
#     responses[name] = response
#
#     # 看看是否还有人要参与调查
#     repeat = input("Would you like to let another person respond? (yes/ no) ")
#     if repeat == 'no':
#         polling_active = False
#
# # 调查结束，显示结果
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(name + " would like to climb " + response + ".")


# 7-8
sandwich_orders = ['牛肉三明治', '五香烟熏牛肉', '鸡肉三明治', '五香烟熏牛肉', '花生酱三明治', '五香烟熏牛肉']
# finished_sandwiches = []

# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     print("I made your " + sandwich + "sandwich")
#     finished_sandwiches.append(sandwich)

# # 显示所有已验证的用户
# print("三明治已经制作完成：")
# for info in finished_sandwiches:
#     print(info)

# 7-9
# print("非常抱歉，五香烟熏牛肉卖完了")
# while '五香烟熏牛肉' in sandwich_orders:
#     sandwich_orders.remove('五香烟熏牛肉')
# print(sandwich_orders)

# 7-10
places = {}
active = True
while active:
    # 输入调查者姓名和期望地点
    name = input("\nWhat is your name? ")
    place = input("If you could visit one place in the world, where would you go?")

    # 将地点存储在字典中
    places[name] = place
    # 看看是否还有人要参与调查
    answer = input("Would you like to let another person respond? (yes/ no) ")
    if answer == 'no':
        active = False

# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, place in places.items():
    print(name + " would like to visit" + place + ".")






