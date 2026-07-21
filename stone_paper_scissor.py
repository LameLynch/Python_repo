#user_information 

def user_info():
    name = input("Name of the player: ")
    
    if len(name) == 0:
        print('Please give some name... ')
        return user_info()
    else:
        print('Welcome!',name)
        return name
player_name = user_info()


#round count
def total_rounds():
    rounds = int(input('How many rounds do you want to play: '))
    return rounds
round_count = total_rounds()




# computer choice 

def comp_choice():
    import random
    options = ['stone','paper','scissor']
    comp_ch = random.choice(options)
    print('The computer chose:',comp_ch)
    return comp_ch




#user choice
def user_choice():
    user_ch = input('What would you like to choose out of [stone,paper,scissor]: ').lower()
    print('You chose: ',user_ch)
    return user_ch



user_score = 0
comp_score = 0

#algorythm for stone paper scissor
def algo():
    global user_opted
    global comp_opted
    global user_score
    global comp_score
    # Player wins
    if comp_opted == 'stone' and user_opted == 'paper':
        user_score += 1
        print(player_name, "wins this round!")
        print(player_name, "score:", user_score, "Computer score:", comp_score)

    elif comp_opted == 'paper' and user_opted == 'scissor':
        user_score += 1
        print(player_name, "wins this round!")
        print(player_name, "score:", user_score, "Computer score:", comp_score)

    elif comp_opted == 'scissor' and user_opted == 'stone':
        user_score += 1
        print(player_name, "wins this round!")
        print(player_name, "score:", user_score, "Computer score:", comp_score)

    # Computer wins
    elif comp_opted == 'paper' and user_opted == 'stone':
        comp_score += 1
        print("Computer wins this round!")
        print(player_name, "score:", user_score, "Computer score:", comp_score)

    elif comp_opted == 'scissor' and user_opted == 'paper':
        comp_score += 1
        print("Computer wins this round!")
        print(player_name, "score:", user_score, "Computer score:", comp_score)

    elif comp_opted == 'stone' and user_opted == 'scissor':
        comp_score += 1
        print("Computer wins this round!")
        print(player_name, "score:", user_score, "Computer score:", comp_score)

    # Draw
    elif comp_opted == 'stone' and user_opted == 'stone':
        print("It's a draw!")
        print(player_name, "score:", user_score, "Computer score:", comp_score)

    elif comp_opted == 'paper' and user_opted == 'paper':
        print("It's a draw!")
        print(player_name, "score:", user_score, "Computer score:", comp_score)

    elif comp_opted == 'scissor' and user_opted == 'scissor':
        print("It's a draw!")
        print(player_name, "score:", user_score, "Computer score:", comp_score)


#UI
def UI():
    global round_count
    global comp_score
    global user_score
    global user_opted
    global comp_opted
    while round_count > 0 :
        user_opted = user_choice()
        comp_opted = comp_choice()
        algo()
        round_count -= 1
    print('The Final Score is!')
    if comp_score > user_score:
        print('The Computer Won!')
        print('Computer Scored:',comp_score)
    else:
        print('You won!')
        print('You Scored:',user_score)
UI()

        