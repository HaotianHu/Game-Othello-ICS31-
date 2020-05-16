#Haotian Hu, ID:21271767
BLACK = 'B'
WHITE = 'W'


class Board:
    def __init__(self,Column,Row):
        '''Initializes the Board's column, row, original board and turn
        '''
        self._Column = Column
        self._Row = Row
        self._board = []
        self._turn = ''

    def get_new_board(self,board:[[int]])->[[int]]:
        '''Returns a new board with empty spaces
        '''
        self._board = board

        return self._board

    

    def draw_board(self):
        """draws the board with every move taken
        """
        for row in range(len(self._board)):
            for col in range(len(self._board[row])):
                if self._board[row][col] == '.':
                    print('.',end = '')
                    if col < len(self._board[row])-1:
                        print(' ',end = '')
                if self._board[row][col] == 'B':
                    print('B',end = '')
                    if col < len(self._board[row])-1:
                        print(' ',end = '')
                if self._board[row][col] == 'W':
                    print('W',end = '')
                    if col < len(self._board[row])-1:
                        print(' ',end = '')
            print()                   
            
    def who_goes_first(self,color):
        '''Choose which color goes first
        '''
        if color == 'B':
            self._turn = BLACK
        if color == 'W':
            self._turn = WHITE
            
    def switch(self):
        '''switch the color or say switch to another player
        '''
        if self._turn == BLACK:
            self._turn = WHITE
            return self._turn
        elif self._turn == WHITE:
            self._turn = BLACK
            return self._turn
       
    def valid_move_test(self,row:int,col:int):
        '''Test the given row and col are valid or not
            and return a list of those tiles that are needed to be flipped
        '''
        color = self._turn
        other_color = self._inverse_color()
        dir_coord = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1,   0], [-1, 1]] #8 directions

        if not self._on_the_board(row,col) or self._board[row][col] != '.':
             return False

        self._board[row][col] = color #put the tile on the board in order to test if the col and row are valid

        flip_list = []

        for xaxis,yaxis in dir_coord:
            x = row
            y = col
            x += xaxis           
            y += yaxis
            while self._on_the_board(x,y) == True and self._board[x][y] == other_color:
                x+= xaxis
                y+= yaxis
                if self._on_the_board(x,y) == True and self._board[x][y] == color:
                    x -= xaxis
                    y -= yaxis
                    while self._board[x][y] == other_color:
                        flip_list.append((x,y))
                        x -= xaxis
                        y -= yaxis

        self._board[row][col] = '.' #restore the board 

        if len(flip_list) == 0:
            return False

        return flip_list
           
    def make_move(self,row:int,col:int):
        '''Make the move with given row and col
        '''
        flip_list = self.valid_move_test(row,col)

        if flip_list == False:
            return False
        self._board[row][col] = self._turn
        
        for x,y in flip_list:
            self._board[x][y] = self._turn

        return True
    
    def get_score_list(self)->list:
        '''Return a list of score of different color or say score of different player
        '''
        score_list = []
        white = 0
        black = 0

        for x in range(self._Column):
            for y in range(self._Row):
                if self._board[x][y] == 'W':
                    white +=1
        score_list.append(white)
        
        for x in range(self._Column):
            for y in range(self._Row):
                if self._board[x][y] == 'B':
                    black +=1
        score_list.append(black)

        return score_list

    def check_gameover(self):
        '''Check if the game is over
        '''
        valid_move_list = self._get_valid_moves()

        if len(valid_move_list) == 0:
            return True
        else:
            return False

    def check_winner(self,rule:str):
        '''Check who is the winner
        '''
        white = int(self.get_score_list()[0])
        black = int(self.get_score_list()[1])

        if rule == '<':
            if white < black:
                return 'W'
            elif white > black:
                return 'B'
            elif white == black:
                return 'NONE'
            
        elif rule == '>':
            if white < black:
                return 'B'
            elif white > black:
                return 'W'
            elif white == black:
                return 'NONE'
            
    def _on_the_board(self,row:int,col:int):
        '''Test if the given col and row are on the board or not
            and give the True or False.
        '''
        return row >= 0  and row <= self._Row-1 and col >= 0 and col <=self._Column-1 #because of index, need to -1

    def _get_valid_moves(self) -> list:
        '''Get all valid col and row
        '''
        valid_move_list = []

        for x in range(self._Row):
            for y in range(self._Column):
                if self.valid_move_test(x,y) != False:
                    valid_move_list.append((x,y))
        return valid_move_list
        
    def _inverse_color(self):
        '''Change the color
        '''
        color = self._turn
        if color == 'B':
            color = 'W'
        elif color == 'W':
            color = 'B'
        return color


        
