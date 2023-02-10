import random

# r = random.randrange(-5, 11)
# r = random.randint(-5, 11)

top_of_range = input("Type a number: ")

#isdigit() check if it is numbers
if top_of_range.isdigit():
  top_of_range = int(top_of_range)
  
  if top_of_range <= 0:
    print('Type a number larger than 0')
    quit()
else:
  print("Type a number")
  quit()   

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
  guesses += 1
  user_guess = input("Make a guess: ")
  
  if user_guess.isdigit():
    user_guess = int(user_guess)

  else: 
    print("Type a number")
    continue

  if user_guess == random_number:
    print("You got it!")
    break
  else:
    if user_guess > random_number:
      print("number is lower")
    else:
      print("number is higher")

print("You got it in", guesses, "guesses")