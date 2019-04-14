print("I am a %s" % "programmer")
print("%d + %d = %d" % (2, 3, 2+3))
list = [1, 2]
print(list[1])
adct = {}
adct.setdefault('name', 'tomy')
print(adct.items())
x = 2
x = int(x)
if x < 0:
    x = -x
else:
    x = -x
print(x)

x = x+1 if x < 0 else 0
print(x)

#=============
list = [{'name': 'tomy', 'age': 20}, {'name': 'tomy2', 'age': 21}, {'name': 'tomy3', 'age': 22}]
for person in list:
    if person["age"] <= 20:
        print(person['name'])
    else:
        break
    print(person['name'])
list2 = list.copy()
for person in list2:
    print(person['name'])
list8 = {'name': 'tomy', 'age': 20, 'sex': 'man'}
list9 = { key2:value for key2,value in list8.items() if key2 != "name"}
print(list9)
