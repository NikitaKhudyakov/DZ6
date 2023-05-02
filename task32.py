a = int(input("min: "))
d = int(input("max: "))
list_1 = [-5,9,0,3,-1,-2,1,4,-2,10,2,0,-9,9,10,-9,0,-5,-5,7]
list_2 =[]
for i in range(len(list_1 )):
    if a < list_1[i] and d > list_1[i]:
        list_2.append(i)
print(list_2)