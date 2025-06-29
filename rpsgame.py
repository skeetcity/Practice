import random, sys

print('Rock, Paper, Scissors.')
# These variables will keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # main game loop until user exits
    print('%s Wins, %s Losses, %s Ties' %(wins, losses, ties))
    while True: # this is player input loop
        print('Enter your move:(R)ock, (P)aper, (S)cissors or (Q)uit')
        player_move = input('> ')
        if player_move == 'Q':
            sys.exit()
        if player_move == 'R' or player_move == 'P' or player_move == 'S':
            break
        print('Please enter a valid move.')
        # Display player move:
        if player_move == 'R':
            print ('Rock versus...')
        elif player_move == 'P':
            print('Paper versus...')
        elif player_move == 'S':
            print('Scissors versus...')
            # Display computer move:
        move_number = random.randint(1, 3)
        if move_number ==1:
            computer_move = 'R'
            print ('Rock')
        elif move_number ==2:
            computer_move = 'P'
        elif move_number ==3:
            computer_move = 'S'
            print ('Scissors')

            #display and record win/loss/ties:
        if player_move == computer_move:
            print('Its a tie!')
            ties = ties + 1
        elif player_move =="R" and computer_move == 'S':
            print('You win!')
            wins = wins + 1
        elif player_move == "P" and computer_move == 'R':
            print('You win!')
            wins = wins + 1
        elif player_move == "S" and computer_move == 'P':
            print('You win!')
            wins = wins + 1
        elif player_move == "R" and computer_move == 'P':
            print('You lose!')
            losses = losses + 1
        elif player_move == "P" and computer_move == 'S':
            print('You lose!')
            losses = losses + 1
        elif player_move == "S" and computer_move == 'R':
            print('You lose!')
            losses = losses + 1