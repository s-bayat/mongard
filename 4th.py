nums = [2, 8, 7, 66, 41, 25]


def show(batch, element):
    for i in batch:
        if i == element:
            return batch.index(i)


print(show(nums, 66))
