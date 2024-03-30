#!/usr/bin/env python
# coding: utf-8

# In[4]:


print("Welcome to Rock ,Paper, Scissors!")
print("Lets Begin ...")
name1 = input("Player 1:What's your name?")
name2 = input("Player 2:What's your name?")

print("Hello " +name1 + " and " +name2)
print(name2 + ": Close your eyes!")

choice1 = input(name1 + ": enter 'r' for rock, 'p' for paper, and 's' for scissors: ")
print("Great choice! Now - cover your answer and ask " +name2 + " to choose. \n\n\n")
choice2 = input(name2 + ": enter 'r' for rock, 'p' for paper, and 's' for scissors: ")

if choice1 == choice2:
    print("Both players have chosen the same answer, it is a tie!")

if choice1 == "r":
    if choice2 == "p":
        print("You win " +name2 + " Paper beats Rock!")
else:
    if choice1 == "p":
        print("You lose " +name1 + " Paper beats Rock!")
    if choice1 == "r":
        if choice2 == "s":
            print("You win " +name1 + " Rock beats Scissors!")
    else:
        print("You lose " +name1 + " Rock beats Scissors!")
        
            

    if choice1 == "s":
        if choice2 == "p":
            print("You win " +name1 + " Scissors beats Paper!")
    else:
        if choice1 == "p":
            if choice2 == "s":
                print("You lose " +name1 + " Scissors beats Paper!")


# In[ ]:




