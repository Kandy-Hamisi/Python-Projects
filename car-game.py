
command = ""

while True:
    command = input("> ")
    if command == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to quit the car")
    elif command == "start":
        print("Car already started...ready to go")
    elif command == "stop":
        print("Car stopped..")
    elif command == "quit":
        break
    else:
        print("Hey I cant understand that")
    

