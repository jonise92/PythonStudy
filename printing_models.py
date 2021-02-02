import printing_functions

# 首先创建一个列表，其中包含一些要打印的设计
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []


# # 模拟打印每个设计，直到没有未打印的设计为止
# # 打印每个设计后，都将其移到列表completed_models中
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#
#     # 模拟根据设计制作3D打印模型的过程
#     print("Printing model: " + current_design)
#     completed_models.append(current_design)
#
# # 显示打印好的所有模型
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

# def print_models(unprinted_designs, completed_models):
#     """
#     模拟打印每个设计，直到没有未打印的设计为止
#     打印每个设计后，都将其移到列表completed_models中
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#
#         # 模拟根据设计制作3D打印模型的过程
#         print("Printing model:" + current_design)
#         completed_models.append(current_design)
#
#
# def show_completed_models(completed_models):
#     """显示打印好的所有模型"""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
#
# unprinted_designs_info = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models_info = []


# print_models(unprinted_designs_info, completed_models_info)
# show_completed_models(completed_models_info)
# print(unprinted_designs_info)

# 向函数传递列表的副本而不是原件;这样函数所做的任何修改都只影响副本，而丝毫不影响原件。
# print_models(unprinted_designs_info[:], completed_models_info)
# print(unprinted_designs_info)

# 8-9
# magicians = ['小明', '阿紫', '木木']
#
#
# def show_magicians(names):
#     for name in names:
#         print(name)


# show_magicians(magicians)


# 8-10
# def make_great():
#     great_magicians = []
#     while magicians:
#         magician = magicians.pop()
#         great_magician = magician + ' the Great.'
#         great_magicians.append(great_magician)
#
#     for magician in great_magicians:
#         magicians.append(magician)
#
#
# show_magicians(magicians)
# print("\n")
# make_great()


# 8-11

# magicians_back = magicians[:]
#
#
# def make_great(magicians_info):
#     great_magicians = []
#     while magicians_info:
#         magician = magicians_info.pop()
#         great_magician = magician + ' the Great.'
#         great_magicians.append(great_magician)
#
#     for magician in great_magicians:
#         magicians_info.append(magician)
#
#
# show_magicians(magicians)
# make_great(magicians_back)
#
# print('\n')
#
# show_magicians(magicians_back)


