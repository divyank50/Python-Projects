import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n "))


#User picking his choice
if user_pick == 0:
  print(rock + "You choose Rock")
elif user_pick== 1 :
  print(paper + "You choose Paper")
elif user_pick == 2:
  print(scissors + "You choose Scissors")

#Computer picking his choice
random_pick = random.randint(0,2)
if random_pick == 0:
  print(rock + "The computer choose Rock\n")
elif random_pick == 1:
  print(paper + "The computer choose Paper\n")
elif random_pick == 2:
  print(scissors + "The computer choose Scissors \n")
  
# This part of the code tells whether the User won or the Computer won!
if random_pick == 0 and user_pick == 0:
  print("It is a Draw")
elif random_pick == 1 and user_pick == 1:
  print("It is a Draw")
elif random_pick == 2 and user_pick == 2:
  print("It is a Draw")
  
elif random_pick == 0 and user_pick == 2:
    print("Computer Won")
elif random_pick == 2 and user_pick == 1:
    print("Computer Won")
elif random_pick == 1 and user_pick == 0:
    print("Computer Won")
else:
    print("You Won!")

    