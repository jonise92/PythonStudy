# my_foods = ['pizza', 'falafel', 'carrot cake']
# 复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:]）切片复制是直接在内存中开辟一个新的内存
# 变量赋值只是变量名发生变化，内存指向不发生变化

# friend_foods = my_foods[:]
#
# # 这行不通
# # friend_foods = my_foods
#
# my_foods.append('cannoli')
# friend_foods.append('ice cream')
#
# print("My favorite foods are:")
# print(my_foods)
#
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# 4-10
# my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
# print('The first three items in the list are:')
# for food in my_foods[:3]:
#     print(food)
#
# print('Three items from the middle of the list are:')
# for food in my_foods[1:4]:
#     print(food)
#
# print('The last three items in the list are:')
# for food in my_foods[-3:]:
#     print(food)

# 4-11 4-12
# pizzas = ['China pizza', 'Japan pizza', 'America pizza']
# friend_pizzas = pizzas[:]
# pizzas.append('Iceland pizza')
# friend_pizzas.append('Germany pizza')
#
# print("My favorite pizzas are:")
# for pizza in pizzas:
#     print(pizza)
#
# print("\nMy friend’s favorite pizzas are:")
# for friend_pizza in friend_pizzas:
#     print(friend_pizza)

