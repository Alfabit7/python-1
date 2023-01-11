# list = [2, 5, 4, 7, 11, 11, 12, 67, 44, 99]

# new_list = [(i, i**3) for i in list if not i % 2]
# print(new_list)

# MAP()
# li = [x for x in range(1, 20)]

# li = list(map(lambda x: x + 10, li))
# print(li)

# data = list(map(int, input().split()))
# print(data)

# FILTER()

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x % 2, data))
# print(res)

# ZIP()

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [1, 2, 3, 4, 5]

# data = list(zip(users, ids))
# print(data)

# ENUMERATE()

users = ['user1', 'user2', 'user3', 'user4', 'user5']
users = list(enumerate(users))
print(users)