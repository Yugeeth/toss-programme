import random

coin = ["Heads", "Tails"]
toss = random.choice(coin)

selection = input("Heads or Tails:")

if selection == toss:
  print("You win! the coin landed on " +  toss)
else:
  print("You lose! The coin landed on " + toss)
