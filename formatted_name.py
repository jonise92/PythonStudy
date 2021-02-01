# 简单返回值
# def get_formatted_name(first_name, last_name):
#     """"返回整洁的姓名"""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)


# 可选实参
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
