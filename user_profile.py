def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


# user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
# print(user_profile)


# 8-12
# def sandwich(**ingredients):
#     ingredient_list = {}
#     for key, value in ingredients:
#         ingredient_list[key] = value
#     return ingredients
#
#
# food = sandwich(肉类='牛肉', 原料='面粉', 调料='食盐')
# print(food)
#
# food = sandwich(肉类='牛肉', 调料='食盐')
# print(food)
#
# food = sandwich(调料='食盐')
# print(food)

# 8-13
# introduction = build_profile('jack', 'ma', 性别='男', 年龄='35', 籍贯='广东')
# print(introduction)

# 8-14
def make_car(vendor, car_type, **other):
    info = {}
    info['vendor'] = vendor
    info['car_type'] = car_type
    for key, value in other.items():
        info[key] = value
    return info


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
