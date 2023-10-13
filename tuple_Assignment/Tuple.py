def reverse_tuple(numbers):
    length = len(numbers)
    reverse = (numbers[length - 1],)
    for num in range(length - 1):
        reverse += (numbers[length - 2],)
        length -= 1
    return reverse


def unpack(numbers):
    length = len(numbers)
    x = numbers[0]
    y = numbers[length - 1]

    return y, x


def secondTerm(numbers):
    length = len(numbers) - 1
    count = 1
    tuple = ()
    for count in range(1, length, 2):
        tuple += numbers[count]
    return tuple






def duplicate(numbers):
    length = len(numbers)
    total = (0,)
    for count in range(length):
        for index in range(1, length):
            if numbers[count] == numbers[index]:
                total += (numbers[index],)
                return total
