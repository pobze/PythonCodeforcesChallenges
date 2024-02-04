str1 = input()
str2 = str1.split("+")
str2.sort()
str3 = ""
for char in str2:
    str3 += char + "+"
print(str3[:-1])
