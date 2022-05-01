price = 1000000
print ("Price of the housr is ",price)
is_good_score = True

if is_good_score:
    print("Your credit score is Good.")
    print("Your down payment will be : ", price*10/100)
elif not(is_good_score):
    print("Your credit score is not good.")
    print('Your down payment will be : ', price*20/100)
else:
    print("Your input is not recognized.")
    print("Please try again...!")
print("Thanks for using our service.")