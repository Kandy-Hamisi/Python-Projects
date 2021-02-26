'''Iterates the start number to the end number and 
    prints the sum of the current number
'''

#Initializing the variable that will store the index and number
output = ""
#initializing the sum
sum = 0
#Initializing the previous number of the range

previous = 0
for number in range(10):

    output = int(number)
    previous = number
    sum = previous + number
    print("current number is "+str(output)+ " previous number is "+ str(previous)+ " Sum: ", +sum )
    