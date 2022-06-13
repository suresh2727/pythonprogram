command = " "
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        print("Car started...  ")
    elif command == "stop":
        print("Car Stoped")
    elif command == "help":
        print("""
        START -- To start a car
        STOP -- To stop a car 
        QUIT -- To quit the gamee
        """)
    elif command == "quit":
        break
    else:
     print("Try other command")


