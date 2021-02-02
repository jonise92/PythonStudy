# 导入整个模块
# import pizza
#
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 导入模块中的特定函数
# from pizza import make_pizza
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：
# from module_name import function_0, function_1, function_2

# 使用as作为别名
# from pizza import make_pizza as mp

# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用星号（*）运算符可让Python导入模块中的所有函数
# from pizza import *
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 给形参指定默认值时，等号两边不要有空格：
# def function_name(parameter_0, parameter_1='default value')

# 对于函数调用中的关键字实参，也应遵循这种约定
# function_name(value_0, parameter_1='value')