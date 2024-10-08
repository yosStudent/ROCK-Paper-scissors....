import random

amount_of_games = 0
amount_of_wins = 0
decision=''

while True:

    user_input = input("\n Rock - 1\n Paper - 2\n Scissors - 3\nStop game - \'STOP\'\nYour choice: ")
    all_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(all_choices)

    user_choice = None

    all_messages = {"p-r": "Paper covers rock!", "r-s": "Rock smashes scissors!", "s-p": "Scissors cuts paper!"}
    if user_input in ['1', 'rock','Rock']:
        user_choice = 'rock'
    elif user_input in ['2', 'paper','Paper']:
        user_choice = 'paper'
    elif user_input in ['3', 'scissors','Scissors']:
        user_choice = 'scissors'
    else:
        exit()

    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

    if user_choice == computer_choice:
        print("It's a tie! Do you want to play again?\nY-yes N-no")
        decision= str(input())
        amount_of_games +=1
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            print(f"{all_messages['r-s']} You win! Do you want to play again?\nY-yes N-no")
            amount_of_games +=1
            amount_of_wins += 1
            decision=str(input())
        else:
            print(f"{all_messages['p-r']} You lose. Do you want to play again?\nY-yes N-no")
            amount_of_games +=1
            decision=str(input())
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print(f"{all_messages['p-r']} You win! Do you want to play again?\nY-yes N-no")
            amount_of_games +=1
            amount_of_wins += 1
            decision=str(input())
        else:
            print(f"{all_messages['s-p']} You lose. Do you want to play again?\nY-yes N-no")
            amount_of_games +=1
            decision=str(input())
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            print(f"{all_messages['s-p']} You win! Do you want to play again?\nY-yes N-no")
            amount_of_games +=1
            amount_of_wins += 1
            decision=str(input())
        else:
            print(f"{all_messages['r-s']} You lose Do you want to play again?\nY-yes N-no.")
            amount_of_games +=1
            decision=str(input())


    decision = decision.lower()
    if decision == 'y':
        continue
    elif decision == "n":
        print(f'You played {amount_of_games} times and won {amount_of_wins} rounds! Overall you score is {amount_of_wins - amount_of_games}')
        break
    else:
        print('There is no such option')
        break