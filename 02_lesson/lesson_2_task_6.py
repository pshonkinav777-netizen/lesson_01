lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]


def elements(lst):
    result = []
    for num in lst:
        if num < 30 and num % 3 == 0:
            result.append(num)
    return result


print(elements(lst))
