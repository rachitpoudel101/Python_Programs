#the use of the import json , it leads the easy method to the reading and writing the data of the gamewho is winner nad who is the looser,current player trun and save in the leaderboard.txt

import json
import random
import os.path

#Printing the board using def function.

def draw_board(board):
    print('-----------')
    print('|' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2] + '|') #Row 1
    print('-----------')
    print('|' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2] + '|') #Row 2
    print('-----------')
    print('|' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2] + '|') #Row 3
    print('-----------')



 #welcoming the user in the game.

def welcome(board):
    print("Welcome to a simple tic tac toe game in python \n The board layout is shown below:")
    draw_board(board) 
    print("When prompted, enter the number corresponding to the square you want.")




#it make initial board 
def initialise_board(board): #it initialize a tik tak toe board by the assigning the blank spaces,
#inside this function the nested loop is used to interate over 2 dimentional list or array "board" the outer loop is for the i in range (3)
#and the inner loop is for the j in range. (3)
     
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '


#player move\ user input for the game .
def get_player_move(board):
    while True:
        player_move = input(
            " 1 2 3 \n 4 5 6 \n 7 8 9 \n choose your square:")
        if player_move in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            player_move = int(player_move) - 1  #here the player_move is converted by subtracting 1 from the user input. 
            if board[int(player_move / 3)][player_move % 3] == ' ':
                return int(player_move / 3), player_move % 3
            else:
                print("This cell is already occupied. Please choose a different cell.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")

#computer move using def function.
def choose_computer_move(board):
   
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return i, j

# checking the winner of the game using def function

def check_for_win(board, mark):
    
    if  (board[0][0] == mark and board[0][1] == mark and board[0][2] == mark) or \
            (board[1][0] == mark and board[1][1] == mark and board[1][2] == mark) or \
            (board[2][0] == mark and board[2][1] == mark and board[2][2] == mark) or \
            (board[0][0] == mark and board[1][0] == mark and board[2][0] == mark) or \
            (board[0][1] == mark and board[1][1] == mark and board[2][1] == mark) or \
            (board[0][2] == mark and board[1][2] == mark and board[2][2] == mark) or \
            (board[0][0] == mark and board[1][1] == mark and board[2][2] == mark) or \
            (board[0][2] == mark and board[1][1] == mark and board[2][0] == mark):
        return True                     
    else:
        return False

def check_for_draw(board):
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def play_game(board):
    initialise_board(board)
    while True:
        player_move = get_player_move(board)
        if player_move != None:
            board[player_move[0]][player_move[1]] = "X"
            draw_board(board)
            if check_for_win(board, "X"):
                return 1
            elif check_for_draw(board):
                return 0
            computer_move = choose_computer_move(board)
            board[computer_move[0]][computer_move[1]] = "O"
            print("Computer made a choice")
            draw_board(board)
            if check_for_win(board, "O"):
                return -1
            elif check_for_draw(board):
                return 0
            else:
                continue


def menu():
        choice = input(
            "1. Play game\n2. Save score\n3. Leaderboard \nq. Quit\nEnter your choice: ")
        
        if choice in ['1', '2', '3', 'q']:
            
            return choice
        else:
            
            print("Invalid input. Please enter a valid choice.")

def load_scores():
    """ Loads the leaderboard from a .txt file and returns it as a dictionary"""
    try:
        
        with open("leaderboard.txt", "r") as file:
            leaderboard = json.load(file)
    except:
        
        leaderboard = {}

    return leaderboard

def save_score(score):
    
    player_name = input("Enter your name: ")
    try:
        with open("leaderboard.txt", "r") as file:
            data = json.load(file)
    except:
        data = {}
    data[player_name] = score
    with open("leaderboard.txt", "w") as file:
        json.dump(data, file)



def display_leaderboard(leaders):
    
    print("Name: Score")
    for name, score in leaders.items():
        print(f"{name}: {score}")


def main():
    
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    
    welcome(board)
    total_score = 0
    
    while True:
        
        choice = menu()
        if choice == '1':
            score = play_game(board)
            total_score += score
            print('Your current score is:', total_score)
        if choice == '2':
            save_score(total_score)
        if choice == '3':
            leader_board = load_scores()
            display_leaderboard(leader_board)
        if choice == 'q':
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Good bye')
            return

if __name__ == '__main__':
    main()