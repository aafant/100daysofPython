print("Welcome to Treasure Island.\n Your mission is to find the treasure\n")
c1 = input("You're at a crossroad, left or right?")
if c1.lower() == "left":
    #continue
    c2 = input("Theres a lake in the way, swim or wait?\n")
    if c2.lower() == "wait":
        c3 = input("There are three doors at the end, which door do you take? Red, Yellow, or Blue?\n")
        if c3.lower() == "yellow":
            print("Congratulations you found the treasure and avoided all the island's traps")
            exit()
    print("Game over! You fell into one of the Island's traps")