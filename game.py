def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )
    
score = 0
print("Guess the Animal")
guess1 = input("Which goalkeeper is the best in world? ")
check_guess(guess1, "El Shenawy")
guess2 = input("Which is the fastest player in the world? ")
check_guess(guess2, "Ma3lol")
guess3 = input("what's the best team in Egypt? ")
check_guess(guess3, "El Ahly")
print("Your Score is "+ str(score))
