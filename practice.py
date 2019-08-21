n=18
number_of_guess=1
print("number of guesses only limited to 9 times")
while(number_of_guess<=9):
    guess_number=int(input("guess the number\n"))
    if guess_number<18:
        print("you enter less than",n)
    elif guess_number>18:
        print("you enter greater than",n)
    else:
        print("you won\n")
        print(number_of_guess,"no of guesses tou took to finish")
        break
    print(9-number_of_guess,"no of gusses left")
    number_of_guess=number_of_guess+1
if(number_of_guess>9):
    print("game over\n you lose!")
