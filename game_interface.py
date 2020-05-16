#Haotian Hu ,ID:21271767
import othello_logic

def read_row_num() -> int:
    '''Read the number of rows of the game board
    '''
    return int(input())
    
def read_col_num() -> int:
    '''Read the number of columns of the game board
    '''
    return int(input())

def read_first_move() -> str:
    '''Read the color of the first move
    '''
    return input().upper()

def read_winner_rule() -> str:
    '''Read the rule of who is the winner(by most or least)
    '''
    return input()

def read_move() -> list:
    '''Read the move that users take
    '''
    move_list = input().split(' ')
    return move_list

def read_board(row:int,col:int) ->list:
    '''Read the initial board that the user what to start with
    '''
    board = []
    for i in range(row):
        board.append(input().split())
    return board

def main():
    '''The main function to run the whole game
    '''
    score_list=[]
    
    row = read_row_num()
    col = read_col_num()
    color = read_first_move()
    winner_rule = read_winner_rule()
    initial_board = read_board(row,col)
    
    Game = othello_logic.Board(col,row)
    
    Game.who_goes_first(color)
    Game.get_new_board(initial_board)

    score_list = Game.get_score_list()
    print('B: '+str(score_list[-1])+'  '+'W: '+str(score_list[0]))#print the initial score
    
    Game.draw_board()#Draw the game board

    print_turn_changer = 'valid'#enable to print the turn if the move is valid,do not print the turn if the move is invalid

    while Game.check_gameover() ==  False:

        if print_turn_changer == 'valid':
            print('TURN: '+Game._turn)

        move = read_move()
        row = int(move[0]) -1 #beacause of index, -1
        col = int(move[-1]) -1

        try:
            
            if len(Game.valid_move_test(row,col)) != 0:

                print('VALID')
                
                Game.make_move(row,col)
                
                score_list = Game.get_score_list()
                print('B: '+str(score_list[-1])+'  '+'W: '+str(score_list[0]))
                  
                Game.draw_board()
                Game.switch()
                print_turn_changer = 'valid'

        except TypeError:
            print('INVALID')
            print_turn_changer = 'invalid'
           
    Game.check_winner(winner_rule)
            


    
if __name__ == '__main__':
    '''run the game
    '''
    print('FULL')
    main()
    












    
