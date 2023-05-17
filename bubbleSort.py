nums = [5, 8, 7, 66, 41, 25]


def bubble_sort(list1):
    # Outer loop for traverse the entire list
    for i in range(len(list1) - 1):
        for j in range(len(list1) - 1):
            if list1[j] > list1[j + 1]:
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp
    return list1


print(bubble_sort(nums))

print(list(range(0, 5)))
