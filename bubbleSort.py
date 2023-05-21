# nums = [5, 3, 7, 66, 41, 25]
#
#
# def bubble_sort(list1):
#     # Outer loop for traverse the entire list
#     for i in range(len(list1) - 1):
#         for j in range(len(list1) - 1):
#             if list1[j] > list1[j + 1]:
#                 temp = list1[j]
#                 list1[j] = list1[j + 1]
#                 list1[j + 1] = temp
#     return list1
#
#
# print(bubble_sort(nums))

# print(list(range(0, 5)))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# list1 = []

def multi(i):
    return i * i


print(list(map(lambda i: i * i, numbers)))


def even(i):
    if i % 2 == 0:
        return True
    return False


print(list(filter(lambda i: i % 2 == 0, numbers)))

# def even(listofnumbers):
#     for i in listofnumbers:
#         if i % 2 == 0:
#             list1.append(i)
#     return list1
#
#
#     # print(list(map(even, numbers)))
#
#
# print(even(numbers))

list2 = [(5, "e"), (2, "y"), (4, "a"), (9, "g"), (1, "k")]

print(sorted(list2, key=lambda i: i[1]))
