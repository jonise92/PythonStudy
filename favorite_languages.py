# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

# 6-1
# person = {
#     'first_name': 'jack',
#     'last_name': 'black',
#     'age': 22,
#     'city': 'Beijing',
# }
# print(person)

# # 6-2
# person = {
#     'a': 1,
#     'b': 9,
#     'c': 22,
#     'd': 27,
#     'e': 18
# }

# # 6-3
# glossary = {
#     'for': '为了',
#     'in': '里面',
#     'list': '列表',
#     'print': '打印',
#     'max': '最大值'
# }

# print('for:' + glossary['for'])
# print('in:' + glossary['in'])
# print('list:' + glossary['list'])
# print('print:' + glossary['print'])
# print('max:' + glossary['max'])


# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " + language.title() + ".")

# # 遍历字典时， 会默认遍历所有的键
# for name in favorite_languages:
#     print(name.title())
#
# # 显示遍历key()方法使代码更易读
# for name in favorite_languages.keys():
#     print(name.title())

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#
#     if name in friends:
#         print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# 字典外面像顺序遍历只需要加函数sorted()
# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作，单是会开辟一块新的内存空间

# 遍历所有数据的键
# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", thank you for taking the poll.")

# 遍历所有数据的值
# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())

# 列表调用set()可以去除重复
# for language in set(favorite_languages.values()):
#     print(language.title())

# 6-4
# glossary['False'] = '假'
# glossary['True'] = '真'
# glossary['break'] = '停止'
#
# for key, value in glossary.items():
#     print(key + ':' + value)

# 6-5
# Rivers = {
#     'Yangtze': 'china',
#     'nile': 'egypt',
#     'Danube': 'germany',
# }
#
# for river, country in Rivers.items():
#     print("The " + river + "runs through " + country)
#     print(river)
#     print(country+"\n")

# 6-6
# accepted_list = {
#     '1': 'name1',
#     '2': 'name2',
#     '3': 'name3',
#     '4': 'name4',
#     '5': 'name5',
# }
# in_list = {
#     '1': 'name1',
#     '2': 'name3',
#     '3': 'name5',
# }
#
# for name in accepted_list.values():
#     if name in [names for names in in_list.values()]:
#         print(name + ',非常感谢您的参与')
#     else:
#         print(name + ',期待您的参与')

# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell'],
# }
#
# for name, languages in favorite_languages.items():
#     if len(languages) == 1:
#         print("\n" + name + "'s favorite language is " + languages[0] + "。")
#     else:
#         print("\n" + name.title() + "'s favorite languages are:")
#         for language in languages:
#             print("\t" + language.title())






