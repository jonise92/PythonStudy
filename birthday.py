age = 23
# TypeError: can only concatenate str (not "int") to str 这个变量表示的可能是数值23，
# 也可能是字符2和3,需要显式地指,出你希望Python将这个整数用作字符串
message = "Happy " + str(age) + "rd Birthday"
print(message)
