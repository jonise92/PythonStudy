# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#     },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#     },
# }
#
# for username, user_info in users.items():
#     print("\nUsername:" + username)
#     full_name = user_info['first'] + " " + user_info['last']
#     location = user_info['location']
#
#     print("\tFull name:" + full_name.title())
#     print("\tLocation:" + location.title())

# 6-7
# people = {
#     'one': {
#         'first_name': 'ming',
#         'last_name': 'zhang',
#         'age': 18,
#         'city': 'Beijing',
#         },
#     'two': {
#             'first_name': 'bai',
#             'last_name': 'li',
#             'age': 22,
#             'city': 'Xian',
#         },
#     'three': {
#             'first_name': 'fu',
#             'last_name': 'du',
#             'age': 29,
#             'city': 'Baoji',
#         },
# }
#
#
# for person in people.values():
#     print(person)

# 6-8
# Bella = {
#     'name': 'Bella',
#     'type': 'dog',
#     'master': 'Xiao ming',
# }
#
# Buddy = {
#     'name': 'Buddy',
#     'type': 'cat',
#     'master': 'Xiao li',
# }
#
# Lucy = {
#     'name': 'Lucy',
#     'type': 'rabbit',
#     'master': 'Xiao hei',
# }
#
# pests = [Bella, Bella, Lucy]
#
# for name in pests:
#     print(name)

# 6-9
# favorite_places = {
#     'xiao_hei': ['北京', '上海', '南京'],
#     'xiao_lan': ['保定', '广东', '西安'],
#     'xiao_zi': ['南京', '菏泽', '青岛'],
# }
#
# for name, place in favorite_places.items():
#     print(name + "喜欢的地方有：")
#     for address in place:
#         print("\t" + address)

# 6-10
# person = {
#     '小黑': [1, 2, 15],
#     '小红': [3, 5, 8],
#     '小蓝': [4, 23],
#     '小紫': [11, 63],
#     '小白': [18, 42],
# }
#
# for name, numbers in person.items():
#     print(name + '喜欢的数字有:')
#     for number in numbers:
#         print("\t" + str(number))

# 6-11
# cities = {
#     '宝鸡': {
#         'country': '中国',
#         'population': '300万',
#         'fact': '青铜器之乡',
#     },
#     '北京': {
#             'country': '中国',
#             'population': '1200万',
#             'fact': '中国首都',
#         },
#     '上海': {
#             'country': '中国',
#             'population': '1500万',
#             'fact': '中国经济中心',
#         },
# }
#
# for city, infos in cities.items():
#     print(city + ":隶属" + infos['country'] + "，人口有" + infos['population'] + "，是" + infos['fact'])

