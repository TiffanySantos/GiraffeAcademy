secret_word = "giraffe"
guess = " " 
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess!= secret_word and not (out_of_guesses): #2 condtitions not met
    if guess_count < guess_limit: # does the user have any guesses left?
        guess = input("Enter guess: ")
        guess_count += 1 #adds 1 to guess count
    else:
        out_of_guesses = True
if out_of_guesses: # either the user has no guesses or has guessed correctly, print differently for each outcome
    print("Out of guesses, YOU LOSE!")
else:
    print("You win!")

