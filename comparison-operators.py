name = input("Enter your name: ");

if len(name) < 3:
    print("name must be more than 3 letters")
elif len(name) > 10:
    print("name must have a maximum of 10 letters")
else:
    print("name looks good")
    
    