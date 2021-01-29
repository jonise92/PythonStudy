# 方法一：
# squares = []
# for value in range(1, 11):
#     # square = value**2
#     # squares.append(square)
#
#     squares.append(value**2)
# print(squares)

# 方法二
# 列表解析
# 首先指定一个描述性的列表名，如squares；指定一个左方括号， 并定义一个表达式，用于生成你要存储到列表中的值。
# 接下来，编写一个for循环，用于给表达式提供值，再加上右方括号。
# 注意，这里的for 语句末尾没有冒号。
# squares = [value**2 for value in range(1, 11)]
# print(squares)

# 4-3
# for number in range(1, 21):
#     print(number)

# 4-4
# for number in range(1, 1000001):
#     print(number)

# 4-5
# num_list = [value for value in range(1, 1000001)]
# print(max(num_list))
# print(min(num_list))
# print(sum(num_list))

# 4-6
# for odd in range(1, 21, 2):
#     print(odd)

# 4-7 列表解析 非常灵活
# 表达式：[expression for iter_val in iterable if cond_expr]
# [expression]：最后执行的结果
# [for iter_val in iterable]：这个可以是一个多层循环
# [if cond_expr]：两个for间是不能有判断语句的，判断语句只能在最后；顺序不定，默认是左到右。
# https://www.runoob.com/note/42490

# triples = [value for value in range(3, 31) if value % 3 == 0]
# for triple in triples:
#     print(triple)

# 4-8  4-9
# cubes = [number**3 for number in range(1, 11)]
# for cube in cubes:
#     print(cube)



