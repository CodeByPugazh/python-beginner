count = 0
guess_limit = 3
secret_number = 7

while count < guess_limit:
      count += 1
      guess = int(input("Guess a number: "))
      if guess == secret_number:
            print("Your guess is correct :-)")
            break
else:
      print("Wrong guess 3 chances over :-(")


# Python has optional else block for while loop also. 
# Else block will be executed after completion of loop with out break
