# name = input("Please enter your name: ")
# print("Hello, " + name + "!")

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
#
# name = input(prompt)
# print("\nHello, " + name + "!")

# def greet_user(username):
#     # """为文档字符串
#     """显示简单的问候语"""
#     print("Hello, " + username.title() + "!")


# # 按照PEP8标准，类或方法后面要有两行空行
# greet_user('jesse')


# def display_message():
#     print("本章学习函数定及参数义")


# display_message()


# def favorite_book(title):
#     print("One of my favorite books is " + title)


# favorite_book('Alice in Wonderland')


# def ge_formatted_name(first_name, last_name):
#     """返回整洁的姓名"""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# # 这是一个无线循环
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("First name:")
#     if f_name == "q":
#         break
#     l_name = input("Last name:")
#     if l_name == 'q':
#         break
#
#     formatted_name = ge_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

# 8-6
# def city_country(city, country):
#     return print('"' + city + ',' + country + '"')
#
#
# city_country('Beijing', 'China')
# city_country('Shanghai', 'China')
# city_country('Nanjing', 'China')


# 8-7
def make_album(singer, album_name, song_number=''):
    if song_number != '':
        song = {'singer': singer, 'album_name': album_name, 'song_number': song_number}
    else:
        song = {'singer': singer, 'album_name': album_name}
    return song


# print(make_album('阿三', '明月几时有'))
# print(make_album('小妮', '把酒问青天'))
# print(make_album('小明', '瞎起个名', '10'))

# 8-8
while True:
    print("(enter 'q' at any time to quit)")
    singer = input("Please input singer name:")

    if singer == "q":
        break
    album_name = input("Please input album name:")
    if album_name == 'q':
        break

    info = make_album(singer, album_name)
    print(info)
    print('\n')

