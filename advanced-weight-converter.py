weight = input("Enter your weight: ")
quiz = input("(L)bs or (Kg)s: ")
new_weight= ""

if quiz.upper() == "L":
    print("Converting to Kgs:::::::::::")
    new_weight = float(weight) * 0.45
    print("You are "+str(new_weight)+" kilos")
elif quiz.upper() == "K":
    print("Converting to Pounds:::::::::")
    new_weight = float(weight) / 0.45
    print("You are "+str(new_weight)+ "pounds")
else:
    print("Invalid Entry, Try again")
    
    

