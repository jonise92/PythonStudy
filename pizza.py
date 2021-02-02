# # 存储所点比萨的信息
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }
#
# # 概述所点的比萨
# print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
# for topping in pizza['toppings']:
#     print("\t" + topping)


# 形参名*toppings中的星号让Python创建一个名为toppings的空元组,并将收到的所有值都封装到这个元组中
# def make_pizza(*toppings):
#     """打印顾客点的所有配料"""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print('- ' + topping)
#
#
# make_pizza('pepperoni')
# make_pizza('pepperoni', 'green peppers', 'extra cheese')


# 如果前面的函数还需要一个实参，必须将该形参放在可变形参的前面：
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


