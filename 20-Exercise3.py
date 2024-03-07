import random
print("Number gussing game")
computer = random.randint(1, 20)
numberOfGusses = 0
print("Number of guess limit is 10 times")
while (numberOfGusses < 10):
    userInput = int(input('Guess the number: '))
    if(userInput > computer):
        print('You guess too high')
    elif(userInput < computer):
        print('You guess too low')
    else:
        print('You guess wright')
        break
    numberOfGusses += 1
    print(f"you guess the number in {numberOfGusses} guess")
if(numberOfGusses> 10):
    print("GameOver!")



winning_number = random.randint(1, 10)
print("Walcome to the game")
guess = 0
game_over = False
while not game_over:
    userInput = int(input("Guess the numebr: "))
    if(userInput > winning_number):
        print('You guess too high')
    elif(userInput < winning_number):
        print('You guess too low')
    else:
        print('You guess wright')
        print(f'You guess the number in {guess+1} times')
        break
    guess += 1
    if guess==5:
        print('GameOver!')
        break


