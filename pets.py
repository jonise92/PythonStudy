# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
#
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

# 位置实参
# def describe_pet(animal_type, pet_name):
#     """"显示宠物信息"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
#
# # describe_pet('hamster', 'harry')
# # describe_pet('dog', 'willie')
# # # 位置实参的顺序很重要,如果实参的顺序不正确，结果可能出乎意料
# # describe_pet('harry', 'hamster')
#
# # 关键字实参的顺序无关紧要,下面两个函数等效
# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='harry', animal_type='hamster')

# 添加默认值后,在这个函数的定义中，修改了形参的排列顺序。
# Python依然将这个默认值视为位置实参，因此如果函数调用中只包含宠物的名字，这个实参将关联到函数定义中的第一个形参。
# 使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。 这让Python依然能够正确地解读位置实参。
# def describe_pet(pet_name, animal_type='dog'):
#     """"显示宠物信息"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# # 效果相同
# describe_pet(pet_name='willie')
# describe_pet('willie')
# describe_pet(pet_name='harry', animal_type='hamster')


# 等效的函数调用

# 一条名为Willie的小狗
# describe_pet('willie')
# describe_pet(pet_name='willie')

# 一只名为Harry的仓鼠
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')


# traceback指出了问题出在什么地方
# describe_pet()


# 8-3
# def make_shirt(size, word):
#     print('T恤尺码是' + size + ',字样为' + word)
#
#
# # make_shirt('x', 'Hello')
#
# # 8-4
# def make_shirt(size, word='I love Python'):
#     print('T恤尺码是' + size + ',字样为' + word)
#
#
# make_shirt('x')

# 8-5
def describe_city(name, county='China'):
    print(name + " is in " + county)


describe_city('Beijing')
describe_city('Shanghai')
describe_city('Tokyo', 'Japan')


