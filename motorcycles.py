motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

# print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

# append将元素追加到列表的末尾
# motorcycles.append('ducati')
# print(motorcycles)

# insert 根据索引插入元素
# motorcycles.insert(0, 'ducati')
# print(motorcycles)

# del根据索引删除元素
# del motorcycles[1]
# print(motorcycles)

# pop删除列表末尾的元素相当于弹出栈顶元素
# 执行pop操作后返回弹出元素
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# first_owned = motorcycles.pop(0)
# print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# 使用del语句还是pop()方法，下面是一个简单的判断标准：
# 如果你要从列表 中删除一个元素，且不再以任何方式使用它，就使用del语句；
# 如果你要在删除元素后还能继续 使用它，就使用方法pop()。

# remove根据值删除元素,同时返回删除元素值
# 方法 remove() 只删除第一个指定的值。
# 如果要删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值。
# motorcycles.remove('ducati')
# print(motorcycles)

# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print("\nA " + too_expensive.title() + " is too expensive for me")

# 3-4
guest = ['小明', '小红', '小黑']
event = ',请和我共进晚餐'
# print(guest[0] + event)
# print(guest[1] + event)
# print(guest[2] + event)

# 3-5
# lost = "小白"
# print(guest[0] + event + '。' + lost + '，有事来不了')
# lost = "小紫"
# print(guest[0] + event + '。' + lost + '，有事来不了')
# print(guest[1] + event + '。' + lost + '，有事来不了')
# print(guest[2] + event + '。' + lost + '，有事来不了')

# # 3-6
# guest.insert(0, 'tom')
# print(guest)
# guest.append('jack')
# print(guest)
#
# # 3-7
# guest.pop()
# print(guest)
# guest.pop()
# print(guest)
# guest.pop()
# print(guest)
#
# print(guest[0]+'，您依然受到邀请')
# print(guest[1]+'，您依然受到邀请')
#
# del guest[0]
# del guest[0]
# print(guest)

# 如果列表为空则报错
# motorcycles = []
print(len(motorcycles))
print(motorcycles[-1])
