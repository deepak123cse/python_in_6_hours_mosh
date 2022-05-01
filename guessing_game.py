correct_guess = 9

guess_counter = 1
won =False

while guess_counter <=3:
    input_guess = int(input('Guess : '))
    if input_guess == correct_guess:
        print('You won...!!!')
        guess_counter = 4 # You can use break to break out of loop
        won = True
    elif guess_counter != correct_guess:
        print('Wrong guess.')
        guess_counter += 1
if not(won):  # while loop also has a else clause. You can use it.
    print('Sorry you did not win..!')
print('Thanks for playing the game')