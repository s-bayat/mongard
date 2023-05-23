# numbers = [1,2,3,4,5,6,7,8,9,10]
squares = []


def square():
    for i in range(1, 11):
        if i % 2 == 0:
            s = i * i
            squares.append(s)
    return squares


print(square())
