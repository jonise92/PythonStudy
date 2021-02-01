# def build_person(first_name, last_name):
#     """返回一个字典，其中包含有一个人的信息"""
#     person = {'first': first_name, 'last': last_name}
#     return person
#
#
# musician = build_person('jimi', 'hendrix')
# print(musician)
#

# 书中p127 这里age最好不要直接用''赋值，因为其定义为str类型，与输出预期不符
def build_person(first_name, last_name, age=0):
    """返回一个字典, 其中包含一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)

