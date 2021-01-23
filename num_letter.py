import random, string

print(string.ascii_lowercase)   # 输出所有小写字母
print(string.ascii_uppercase)   # 输出所有大写字母
print(string.ascii_letters)     # 输出所有大小写字母
print(string.digits)            # 输出数字0-9

str = string.ascii_letters + string.digits
print(str)
# 随机生成一个10位的密码，由大小写字母和数字组成
print("".join(random.sample(str, 10)))