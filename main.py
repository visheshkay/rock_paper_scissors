import random

print("TERMINAL ROCK PAPER SCISSORS")
player_score,computer_score = 0, 0
play = True
choices = ['s', 'r', 'p']
while play:
    player_choice = str(input("Enter your choice 'r' for rock , 'p' for paper and 's' for scissors: "))
    computer_choice = random.choice(choices)
    if player_choice == computer_choice:
        print("THE GAME IS A TIE")
    elif player_choice == 'r':
        if computer_choice == 's':
            print("YOU WIN")
            player_score += 1
        else:
            print("YOU LOSE")
            computer_score += 1
    elif player_choice == 'p':
        if computer_choice == 's':
            print("YOU LOSE")
            computer_score += 1
        else:
            print("YOU WIN")
            player_score += 1
    elif player_choice == 's':
        if computer_choice == 'r':
            print("YOU LOSE")
            computer_score += 1
        else:
            print("YOU WIN")
            player_score += 1
    print(f"YOUR CHOICE WAS {player_choice}, THE COMPUTER CHOICE WAS {computer_choice}")
    print("SCORES")
    print(f"PLAYER = {player_score} | COMPUTER = {computer_score}")
    play_again = str(input("Do you want to play again? (y/n): "))
    if play_again != 'y':
        print("THANKS FOR PLAYING")
        play = False
