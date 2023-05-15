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


def show2(nums2):
    max_num = nums[0]
    for i in nums:
        if i > max_num:
            max_num = i
    return max_num


print(show2(nums))
