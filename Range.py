count = [x for x in range(12)]
for i in count:
    print(i)


my_list = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]

new_list = list(filter(lambda x: (x/3 == 1), my_list))

print(new_list)

triple = lambda x: x * 3

print(triple(6))

add = lambda x = 17, y = 23, z = 34: x + y + z
print(add(50))

ListyList = [2, 6, 10, 15, 19, 23, 26, 27]
print(ListyList)

double_list = list(map(lambda x : x ** 2, ListyList))
print(double_list)

triple_list = list(map(lambda x : x ** 3, ListyList))
print(triple_list)

remainder_list = list(map(lambda x : x%2, ListyList))
print(remainder_list)