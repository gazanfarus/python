############### Blackjack House Rules #################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


from art import logo
import random
#from replit import clear


def restart():
  if input("\nDo you want to restart? \'Y\' or \'N\': ").lower() == "y":
#    clear()
    blackjack()
  else:
    exit()


def blackjack():

  print(logo)
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  
  player_score = 0
  player_cards = random.sample(set(cards), 2)
  for card in player_cards:
    player_score += card
  
  computer_score = 0
  computer_cards = random.sample(set(cards), 2)
  for card in computer_cards:
    computer_score += card
  
  print(f"    Your cards: {player_cards}, current score is {player_score}")
  print(f"\n    Computer's first card: {computer_cards[0]}")
  
  
  while player_score < 22:
  
    another_card = input(f"\nType \'y\' to get another card, type \'n\' to pass: ").lower()
    
    if another_card == "y":
      player_draw = random.choice(cards)
      player_cards.append(player_draw)
      player_score += player_draw
      print(f"\nYour cards: {player_cards}, score: {player_score}")
      print(f"\n    Computer's first card: {computer_cards[0]}")
      
  
      if player_score > 21:
        print(f"\n    Your cards: {player_cards}, score: {player_score}")
        print(f"    Computer's cards: {computer_cards}, score: {computer_score}")
        print("\n    Bust. You lose")
        restart()
    
    
    else:
      if player_score == 21:
        print(f"\n    Your cards: {player_cards}, score: {player_score}")
        print(f"    Computer's cards: {computer_cards}, score: {computer_score}")
        print("\n    BLACKJACK!")
        player_score = 22
        restart()
        
      elif player_score < 17:
        player_draw = random.choice(cards)
        player_cards.append(player_draw)
        player_score += player_draw
        print("\nYour score was less than 17, drawing another card.")
        print(f"    Your cards: {player_cards}, score: {player_score}")
        
        
        if player_score > 21:
          print(f"    Computer's cards: {computer_cards}, score: {computer_score}")
          print("\n    Bust. You lost.")
          restart()
        else:
          print(f"\n    Computer's first card: {computer_cards[0]}")
        
      elif player_score > computer_score:
        print(f"\n    Your cards: {player_cards}, score: {player_score}")
        print(f"    Computer's cards: {computer_cards}, score: {computer_score}")
        print("\n    You win!")
        restart()
        
      elif player_score == computer_score:
        print(f"\n    Your cards: {player_cards}, score: {player_score}")
        print(f"    Computer's cards: {computer_cards}, score: {computer_score}")
        print("\n    Draw")
        restart()
        
      else:
        print(f"\n    Your cards: {player_cards}, score: {player_score}")
        print(f"    Computer's cards: {computer_cards}, score: {computer_score}")
        print("\n    You lose")
        restart()

blackjack()
