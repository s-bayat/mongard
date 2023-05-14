nums = [5, 8, 7, 66, 41, 25]


def show(batch, element):
    for i in batch:
        if i == element:
            return batch.index(i)


print(show(nums, 66))


def show1():
    if nums[0] % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(show1())
