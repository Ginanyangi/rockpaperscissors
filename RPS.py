import random

user_choice= input('Enter a choice(rock,paper,scissors): ')
choices = ['rock','paper','scissors']
computer_choice = random.choice(choices)
print(f'You chose {user_choice}, computer chose {computer_choice}.')

if user_choice == computer_choice:
    print(f'It is a tie!')
elif user_choice == 'rock':     
    if computer_choice == 'scissors':
        print('Rock smashes scissors! You win')
    else:
        print('Paper covers rock! You lose')
elif user_choice == 'paper':
    if computer_choice == 'rock':
        print('Paper covers rock! You win')
    else:
        print('Scissors cuts paer! You lose')
elif  user_choice == 'scissors':
    if computer_choice == 'psper':
        print('Scissors cuts paper! You win')
    else:
        print('Rock smashes scissors! You lose.')

