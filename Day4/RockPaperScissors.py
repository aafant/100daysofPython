import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (_____)
---.__(_____)
"""

# ASCII Art for Paper
paper = """
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# ASCII Art for Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


keep_play = True

while keep_play == True:
    print(f"{rock}\n{paper}\n{scissors}\n Lets play rock paper scissors!\n")
    cc = random.randint(1,3) ## Computers choice
    uc = input("rock paper or scissors?\n") ## user choice
    if uc.lower() == "rock":
        print(f"You chose rock!{rock}")
        if cc == 1:
            print(f"Computer chose {rock}It's a tie!\n")
        if cc == 2:
            print(f"Computer chose {paper} You lose!\n")
        if cc == 3:
            print(f"Computer chose {scissors} You win!\n")
    if uc.lower() == "paper":
        if cc == 1:
            print(f"Computer chose {rock} You win!!\n")
        if cc == 2:
            print(f"Computer chose {paper} It's a tie!!\n")
        if cc == 3:
            print(f"Computer chose {scissors} You lose!\n")
    if uc.lower() == "scissors" or uc.lower() == "scissor":
        if cc == 1:
            print(f"Computer chose {rock} You lose!\n")
        if cc == 2:
            print(f"Computer chose {paper} You win!\n")
        if cc == 3:
            print(f"Computer chose {scissors} It's a tie!\n")
    Type = input("Type quit to quit or press enter to continue playing\n")
    if Type == "quit":
        keep_play = False
       