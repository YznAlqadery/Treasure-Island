
print("Welcome to Treasure Island. Your mission is to find the treasure.")

left_right = input("Where do you want to go? left or right? ")

if(left_right.lower() == "right"):
    print("You fell into a hole, better luck next time!")
elif(left_right.lower() == "left"):
    swim_wait = input("Do you want to swim or wait? ")
    if(swim_wait.lower() == "swim"):
        print("Attacked by trout, better luck next time!")
    elif(swim_wait.lower() == "wait"):
        door = input("Which door do you want to go through? Red, Blue, Yellow? ")
        if(door.lower() == "red" or door.lower() == "blue"):
            print("Eaten by a beast, better luck next time!")
        else:
            print("You win, Congrats!")
else:
    print("Please enter a valid option!")
