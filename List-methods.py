numbers = [5, 2, 3, 1, 7, 4]
numbers2 = numbers.copy()
# numbers.insert(0,10)
# numbers.remove(3)
# # numbers.pop()
# # numbers.clear()
# numbers.append(20)
# # print(numbers.count(5))
# # numbers.sort()
# # numbers.reverse()
# print(numbers2)


numbers3 = [5, 2, 3, 1, 7, 4, 5, 5, 3, 1]
duplicates = ''
uniques = []

for number in numbers3:
    if number not in uniques:
        uniques.append(number)
print(uniques)