# Russian Roullete Simulator 0.1
# Created by luvdead999
# Owner The ICA Agency

from random import *
from time import *
end = False
winner = None
turn = randint(1, 2)
round = 1
def gameplay(end, turn, round):
  while end == False:
    print(f"Round {round} is starting.")
    sleep(1)
    if turn == 1:
      print("It's your turn.")
      input("Press [Enter] to spin the revolver drum. ")
      sleep(1)
      print()
      print("You scrolled the drum and put a revolver to your head.")
      sleep(1)
      bullet = randint(1, 6)
      input("Press [Enter] to to pull the trigger. ")
      print()
      sleep(1)
      trigger = randint(1, 6)
      if trigger == bullet:
        print("You pulled the trigger...")
        sleep(1)
        print("Boom!")
        sleep(1)
        print("You shot yourself in the head.")
        sleep(1)
        print("You fell dead from the chair on the ground.")
        sleep(1)
        print()
        winner = "your opponent"
        end = True
      else:
        print("You pulled the trigger...")
        sleep(1)
        print("Nothing happened.")
        sleep(1)
        print("With sigh, you gave the revolver to your opponent.")
        sleep(1)
        input("Press [Enter] to continue")
        sleep(1)
        print()
        round += 1
        turn = 2
        
    else:
      print("It's your opponent's turn.")
      sleep(1)
      print("He scrolled the drum and put a revolver to his head.")
      print()
      bullet = randint(1, 6)
      input("Press [Enter] to continue. ")
      print()
      sleep(1)
      trigger = randint(1, 6)
      if trigger == bullet:
        print("He pulled the trigger...")
        sleep(1)
        print("Boom!")
        sleep(1)
        print("He shot himself in the head.")
        sleep(1)
        print("He fell dead from the chair on the ground.")
        sleep(1)
        winner = "you"
        end = True
        print()
      else:
        print("He pulled the trigger...")
        sleep(1)
        print("Nothing happened.")
        sleep(1)
        print("With sigh, he gave the revolver to you")
        sleep(1)
        input("Press [Enter] to continue. ")
        print()
        sleep(1)
        round += 1
        turn = 1
  print("Game Over.")
  sleep(1)
  print(f"The winner is {winner}!")
  sleep(1)
  print(f"The game ended in {round} rounds.")
  sleep(1)
  input("Press [Enter] to return to Main Menu. ")
  sleep(1)
  print()
  main_menu()
          
          
def main_menu():
  sleep(1)
  print("Welcome to Russian Roulett Simulator!")
  sleep(1)
  print("Please, take your seat.")
  sleep(1)
  input("Press [Enter] to sit down.")
  sleep(1)
  print()
  print("- MAIN MENU -")
  print("Play")
  sleep(1)
  print("Quit")
  sleep(1)
  choice = input("(Write the whole choice, the whole choice wihout capital letters, or the first 3 letters of the choice.) ")
  if choice == "Play" or choice == "play" or choice == "pla":
    print()
    sleep(1)
    gameplay(end, turn, round)
  elif choice == "Quit" or choice == "quit" or choice == "qui":
    print()
    sleep(1)
    print("Goodbye! We hope you will visit us once more!")
    sleep(1)
    input("Press [Enter] to quit.")
  else:
    print()
    sleep(1)
    print("Invalid input.")
    sleep(1)
    input("Press [Enter] to return to Main Menu")
    print()
main_menu()
    
      
