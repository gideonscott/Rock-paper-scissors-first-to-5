import random


Options=["rock","paper","scissors"]
wins=0
losses=0
while wins < 5 and losses < 5:
    guess= input("ENTER ROCK,PAPER, OR SCISSORS. FIRST TO FIVE!!!: ")
    computeranswer=random.choice(Options) 
    print("you chose " + guess + " computer chose " + computeranswer )
    if guess==computeranswer:
        print("We tied!")
    elif guess=="paper":
        if computeranswer=="scissors":
            print("Lost round!")
            losses=losses+1
        else: 
            print("Won round!")
            wins=wins+1 
    elif guess =="rock":
        if computeranswer=="scissors":
            print("Won round!")
            wins=wins+1
        else: 
            print("Lost round!")
            losses=losses+1
    elif guess =="scissors":
        if computeranswer =="rock":
            print("Won round!")
            wins=wins+1
        else:
            print("Lost round!")
            losses=losses+1
if wins==5:
    print("Well played")
if losses==5:
    print("You lost, so close!")
