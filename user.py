import collections

# 注意，即便遍历字典时，键—值对的返回顺序也与存储顺序不同。Python不关心键—值对的存储顺序，而只跟踪键和值之间的关联关系。
# python的字典内部实现是散列表，所以字典的键值必须是可hash的，遍历顺序跟hash值的值有关

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

# 让字典按顺序输出
user_0 = collections.OrderedDict(user_0)

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

