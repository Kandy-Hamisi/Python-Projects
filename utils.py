def find_max():
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum
