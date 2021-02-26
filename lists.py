# name = ['John', 'Kandy', 'Bless', 'Eric', 'Marry']
# print(name[2:-1])

#checking the largest number in a list
numbers = [1, 2, 3, 4]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)