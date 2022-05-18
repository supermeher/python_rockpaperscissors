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

#Write your code below this line 👇
import random


your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

pc_choice = random.randint(0,2)
hand_sign = [rock, paper, scissors]

if your_choice == 0:
  if pc_choice==0:
    print(hand_sign[your_choice]+ hand_sign[pc_choice]+ "tied")
  if pc_choice == 1:
    print(hand_sign[your_choice]+ hand_sign[pc_choice] + "PC won")
  if pc_choice == 2:
    print(hand_sign[your_choice]+ hand_sign[pc_choice] + "You Won")  

if your_choice == 1:
  if pc_choice==0:
    print(hand_sign[your_choice]+ hand_sign[pc_choice] + "You Won")
  if pc_choice == 1:
    print(hand_sign[your_choice]+ hand_sign[pc_choice] + "tied")
  if pc_choice == 2:
    print(hand_sign[your_choice]+hand_sign[pc_choice] + "PC Won")  

if your_choice == 2:
  if pc_choice==0:
    print(hand_sign[your_choice]+ hand_sign[pc_choice] + "PC won")
  if pc_choice == 1:
    print(hand_sign[your_choice]+hand_sign[pc_choice] + "You Won")
  if pc_choice == 2:
    print(hand_sign[your_choice]+hand_sign[pc_choice] + "tied")  
