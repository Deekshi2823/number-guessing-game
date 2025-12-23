import random
secret_num=random.randint(1,50)
attempts=0
print("Welcome!\nI have selected a number between 1 to 50.\nTry to guess it!.")
while True:
  guess=int(input("Enter your guess:"))
  attempts+=1
  if guess<secret_num:
    print("Low! Try again")
  elif guess>secret_num:
    print("High! Try again")
  else:
    print(f"Congrats! You guessed in {attempts} attempts.")
    break
