a = int(input("Разница: "))
d = int(input("Длинна: "))
c = int(input("Первое значение: "))
list_1 = []
for i in range(d):
    c = c+a
    list_1.append(c)
print(list_1)