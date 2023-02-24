
values = [10, 20, 30]
iterator = iter(values)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))

mylist = [x for x in range(25)]

for x in iter(mylist):
    print(x)
    if x % 4 == 0:
        print("--->", x)
        next(mylist)
        print("--->", x)
