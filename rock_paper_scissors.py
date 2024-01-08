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

options = ["rock", "paper", "scissors"]
      
human_choice = input("What do you choose? Type \"Rock\", \"Paper or \"Scissors.\"\n").lower()
pc = str(random.randint(0, 2))
human = str(options.index(human_choice))
#print(human)
#print(pc)

if human == "0" and pc == "0":
  print(rock)
  print("Computer chose:")
  print(rock)
  print("It's a draw")
elif human == "0" and pc == "1":
  print(rock)
  print("Computer chose:")
  print(paper)
  print("You lost :(")
elif human == "0" and pc == "2":
  print(rock)
  print("Computer chose:")
  print(scissors)
  print("You win! Yay!")
  
elif human == "1" and pc == "0":
  print(paper)
  print("Computer chose:")
  print(rock)
  print("You win! Yay!")
elif human == "1" and pc == "1":
  print(paper)
  print("Computer chose:")
  print(paper)
  print("It's a draw")
elif human == "1" and pc == "2":
  print(paper)
  print("Computer chose:")
  print(scissors)
  print("You lost :(")
  
elif human == "2" and pc == "0":
  print(scissors)
  print("Computer chose:")
  print(rock)
  print("You lost :(")
elif human == "2" and pc == "1":
  print(scissors)
  print("Computer chose:")
  print(paper)
  print("You win! Yay!")
elif human == "2" and pc == "2":
  print(scissors)
  print("Computer chose:")
  print(scissors)
  print("It's a draw")

else:
  print("Wrong signal, mate")
  exit()
exit()
