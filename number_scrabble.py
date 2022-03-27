"""
Author: Ziad Nasser Shaaban
ID: 20210153
Date: 2022/2/21
purpose: cs112 course assignment.
institution: FCAI_CU.

this is a number scrubble game : which take numbers from two player until one of them wins( a player can win if the sum
of the input number exactly  equal to 15) or the game end as a draw( it is a draw when the board is no longer contain
numbers to be picked )
"""

# the main board of the game.
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# two arrays each one save the chosen number from a specified player.
new_p1_num = []
new_p2_num = []


# showing the board of number scrabble game.
def print_board():
    global board
    print(board)


# checking the input from the user.
def get_action(player):
    num = input(player + "Enter a number from the board : ")

    # checking the conditions for the input number from the user.
    while True:
        if not num.isdigit():  # checking if the number is digit or not.
            num = input(player + "Enter a number please : ")

        elif 0 < int(num) <= 9 and board[int(num) - 1] != "X":  # checking the number is in the given list or not.
            return int(num)

        else:
            num = str(
                input(player + "please enter another number from the board : "))  # asking for a not taken before num or
                                                                                  # a number in the range of the list.


# updating and showing the new board after taking the input from the user.
def update_board(num):
    board[num - 1] = "X"
    print_board()


# taking the number from the two players.
def players_nums():
    p1_num = get_action("player 1 ")
    new_p1_num.append(p1_num)  # creating a list to save player1 input.
    update_board(p1_num)

    # check if it is a draw or player 1 hadn't already won.
    if not is_draw() and score_calc(new_p1_num) != 15:
        p2_num = get_action("player 2 ")
        new_p2_num.append(p2_num)  # creating a list to save player2 input.
        update_board(p2_num)

    return new_p1_num, new_p2_num


# calculating the score of the player.
def score_calc(arr):
    score = 0
    for num in arr:  # abstracting the numbers from the made array it was saved in.
        score += num  # calculating the score.

    return score


# checking the draw state if reached.
def is_draw():
    if board[0] == "X" and board[1] == "X" and board[2] == "X" and board[3] == "X" and board[4] == "X" and \
            board[5] == "X" and board[6] == "X" and board[7] == "X" and board[8] == "X":
        return True

    return False


# the main function for playing the number scrabble game.
def playing_game():
    print("------------------------------------------------------------------------------------------------------- \n"
          " Enter numbers from the board where \n the sum of them is exactly equal to 15 \n the player that reach 15"
          " first wins! \n "
          "-------------------------------------------------------------------------------------------------------")
    print_board()

    while True:
        player1_num, player2_num = players_nums()
        if score_calc(player1_num) == 15:  # checking the score of player 1 for winning state .
            print("player 1 win!")
            break
        elif score_calc(player2_num) == 15:  # checking the score of player 2 for winning state .
            print("player 2 wins!")
            break
        elif is_draw():
            print("Draw!")
            break


playing_game()
