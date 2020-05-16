import tkinter
import othello_logic

DEFAULT_FONT = ('Comic Sans MS', 14)


class InvalidInputError:
    pass

class InitialInterface:
    '''The initial window interface
    '''
    def __init__(self):
        '''The root window initial
        '''
        self._root_window = tkinter.Tk()

        game_start_button = tkinter.Button(
            master = self._root_window, text = 'Start',
            font = DEFAULT_FONT, command = self._game_start)
        game_start_button.grid(
            row = 1 ,column = 0 ,padx = 10, pady = 10,
            sticky = tkinter.N)

        self._initial_text = tkinter.StringVar()
        self._initial_text.set('Welcome to Game Othello')

        text_label = tkinter.Label(
            master = self._root_window, textvariable = self._initial_text,
            font = ('Comic Sans MS', 20))
        text_label.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.S)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

    def start(self) -> None:
        '''To start the mainloop
        '''
        self._root_window.mainloop()

    def _game_start(self) ->None:
        '''A command for the ok button to start the game
        '''
        require = RequirementsDialog()
        require.run()
        if require._change_initial_title == True:
            self._initial_text.set('Click start to re-play Game Othello')

            
##        chessboard = Chessboard()
        
            
        

        
    
class RequirementsDialog:
    '''The second window to input the row, col, first move tile and rule to win
    '''
    def __init__(self):
        self._dialog_window = tkinter.Toplevel()

        game_welcome_label = tkinter.Label(
            master = self._dialog_window, text = 'Welcome to Game Othello',
            font = ('Comic Sans MS', 20))
        game_welcome_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._input_prompt_label = tkinter.Label(
            master = self._dialog_window, text = 'Invalid Input, please re-input.',
            font = DEFAULT_FONT)

        game_rule_label = tkinter.Label(
            master = self._dialog_window, text = 'Rule: Full',
            font = ('Comic Sans MS', 18))
        game_rule_label.grid(
            row = 1, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

        row_label = tkinter.Label(
            master = self._dialog_window, text = 'Rows(Please type an even integer between 4 and 16 inclusive): ',
            font = DEFAULT_FONT)
        row_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        self._row_label_entry = tkinter.Entry(
            master = self._dialog_window, width = 10, font = DEFAULT_FONT)
        self._row_label_entry.grid(
            row = 2, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)
      
        col_label = tkinter.Label(
            master = self._dialog_window, text = 'Columns(Please type an even integer between 4 and 16 inclusive): ',
            font = DEFAULT_FONT)
        col_label.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        self._col_label_entry = tkinter.Entry(
            master = self._dialog_window, width = 10, font = DEFAULT_FONT)
        self._col_label_entry.grid(
            row = 3, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        move_label = tkinter.Label(
            master = self._dialog_window, text = 'The Player who goes first(Please type " B " (for black) or " W " (for white): ',
            font = DEFAULT_FONT)
        move_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        self._move_label_entry = tkinter.Entry(
            master = self._dialog_window, width = 10, font = DEFAULT_FONT)
        self._move_label_entry.grid(
            row = 4, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        win_rule_label = tkinter.Label(
            master = self._dialog_window, text = 'The Wining Rule(Please type " < "(for fewer wins) or " > "(for more wins): ',
            font = DEFAULT_FONT)
        win_rule_label.grid(
            row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        self._win_rule_label_entry = tkinter.Entry(
            master = self._dialog_window, width = 10, font = DEFAULT_FONT)
        self._win_rule_label_entry.grid(
            row = 5, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)
######################## Frame things
        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 6, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'Ok', font = DEFAULT_FONT,
            command = self._on_ok_button)
        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = DEFAULT_FONT,
            command = self._on_cancel_button)
        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)

        self._dialog_window.rowconfigure(6, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)
########################
        self._ok_clicked = False
        self._row_num = 0
        self._col_num = 0
        self._first_move = ''
        self._rule = ''
        self._change_initial_title = False

        
        
        
    def _on_ok_button(self) -> None:
        '''Handle the command of OK button
        '''
        self._ok_clicked = True

        try:
            self._row_num += int(self._row_label_entry.get())
            if (self._row_num < 4 or self._row_num > 16):
                self._row_num = 0
                self._col_num = 0
                self._first_move = ''
                self._rule = ''
                raise InvalidInputError()
            self._col_num += int(self._col_label_entry.get())
            if (self._col_num < 4 or self._col_num > 16):
                self._row_num = 0
                self._col_num = 0
                self._first_move = ''
                self._rule = ''
                raise InvalidInputError()
            self._first_move = self._move_label_entry.get()
            if (self._first_move != 'B' and self._first_move != 'W'):
                self._row_num = 0
                self._col_num = 0
                self._first_move = ''
                self._rule = ''
                raise InvalidInputError()
            self._rule = self._win_rule_label_entry.get()
            if (self._rule != '<' and self._rule != '>'):
                self._row_num = 0
                self._col_num = 0
                self._first_move = ''
                self._rule = ''
                raise InvalidInputError()


            self._dialog_window.destroy()######
            chessboard = Chessboard(self._row_num,self._col_num,self._first_move,self._rule)
            chessboard.show()
            if chessboard._game_over_check == True:
                self._change_initial_title = True

                
        except:
            self._input_prompt_label.grid(
                row = 0, column = 1, columnspan = 2, padx = 10, pady = 10,
                sticky = tkinter.W)   
        

    def _on_cancel_button(self) -> None:
        '''Cancle button command to close the window
        '''
        self._dialog_window.destroy()

    def run(self):
        '''run the second window
        '''
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

        

    

    
class Chessboard:
    def __init__(self, rows: int, cols: int, color:str, rule:str):
        
        self._chessboard_window = tkinter.Toplevel()
        
        self._rows = rows
        self._cols = cols
        self._color = color 
        self._rule = rule
        self._turn = 'B'
        
        self._black_point = []
        self._white_point = []

        self._final_black_list = [] 
        self._final_white_list = []

        self._board = []
        self._score_list = []
        self._B_score = 0
        self._W_score = 0

        self._Game = othello_logic.Board(self._rows,self._cols)
       
        
        self._coordinates = []
        
        for coord in range(rows):
            self._coordinates.append((0,coord*(1/rows),1,coord*(1/rows)))
        for coord in range(cols):
            self._coordinates.append((coord*(1/cols),0,coord*(1/cols),1))
        
#########################Label and button
        name_label = tkinter.Label(
            master = self._chessboard_window, text = 'Game Othello',
            font = ('Comic Sans MS', 20))
        name_label.grid(
            row = 0 , column = 0, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.N)

        self._prompt = tkinter.StringVar()
        self._prompt.set('Please place initial BLACK tiles on the board.\n Click first button when you finished drawing BLACK tile.')
        prompt_label = tkinter.Label(
            master = self._chessboard_window, textvariable = self._prompt,
            font = DEFAULT_FONT)
        prompt_label.grid(
            row = 0,column = 2 ,padx = 10,pady = 10,
            sticky = tkinter.E+tkinter.W)
        self._game_over_label = tkinter.Label(
            master = self._chessboard_window, text = 'GAME OVER!',
            font = ('Comic Sans MS', 30))
        

        rule_label = tkinter.Label(
            master = self._chessboard_window, text = 'Rule Version: Full',
            font = DEFAULT_FONT)
        rule_label.grid(
            row = 1 , column = 0, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.N)


        self._initial_black_button = tkinter.Button(
            master = self._chessboard_window,text = 'Click when finishing drawing BLACK tile',
            font = DEFAULT_FONT,
            command = self._change_turn)
        self._initial_black_button.grid(
            row = 1, column = 1 , padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.N)
        self._initial_white_button = tkinter.Button(
            master = self._chessboard_window, text = 'Click when finishing drawing WHITE tile',
            font = DEFAULT_FONT,
            command = self.white_button_clicked)
        self._initial_white_button.grid(
            row = 2, column = 1  , padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.N)
        

        
        
###################### Create a frame (Things in frame)
        self._count_frame = tkinter.Frame(master = self._chessboard_window)
        self._count_frame.grid(
            row = 2, column = 2, rowspan = 2, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S)
            
        self._black_count = tkinter.StringVar()
        self._black_count.set('Black:')
        black_count_label = tkinter.Label(
            master = self._count_frame, textvariable = self._black_count,
            font = ('Helvetica', 30))
        black_count_label.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.E)

        self._white_count = tkinter.StringVar()
        self._white_count.set('White:')
        white_count_label = tkinter.Label(
            master = self._count_frame, textvariable = self._white_count,
            font = ('Helvetica', 30))
        white_count_label.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.E)

        self._turn_count = tkinter.StringVar()
        self._turn_count.set('Turn:')
        self._turn_count_label = tkinter.Label(
            master = self._count_frame, textvariable = self._turn_count,
            font = ('Helvetica', 30))
        self._turn_count_label.grid(
            row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.E)        
######################### In canvas
        self._canvas = tkinter.Canvas(
            master = self._chessboard_window,
            width = 500,
            height = 500,
            background = '#993300')
        self._canvas.grid(
            row = 3, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._canvas.bind("<Button-1>",self._on_button_clicked)
        self._canvas.bind('<Configure>', self._on_canvas_resized)        
##########################
        self._chessboard_window.rowconfigure(0, weight = 1)
        self._chessboard_window.rowconfigure(1, weight = 1)
        self._chessboard_window.rowconfigure(2, weight = 1)
        self._chessboard_window.rowconfigure(3, weight = 1)
        self._chessboard_window.columnconfigure(0, weight = 1)
        self._chessboard_window.columnconfigure(1, weight = 1)
        self._chessboard_window.columnconfigure(2, weight = 1)    

        self._white_button_is_clicked = False
        self._game_over_check = False


    def _change_turn(self):
        '''Change the turn of users
        '''
        self._turn = 'W'
        self._initial_black_button.grid_remove()
        self._prompt.set('Please place initial WHITE tiles on the board.\n Click second button when you finished drawing WHITE tile.')

    
    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        '''Resize the Canvas
        '''
        self._canvas.delete(tkinter.ALL)
        self._draw_all_tiles()
        self._draw_lines()
        

    def create_initial_board(self):
        '''Create the inital board in order to translate to the game logic
        '''
        board = []
        black_tile = []
        for item in range(self._cols):
            board.append(['.'] *self._rows)
        for coord in self._final_black_list:
            xb,yb = coord
            board[xb][yb] = 'B'
        for coord in self._final_white_list:
            xw,yw = coord
            board[xw][yw] = 'W'
        self._board = board
        self._initial_white_button.grid_remove()

    def _get_black_tile_list(self,event):
        '''To get the tow dimensonal list of black tile
        '''
        black_point = self._get_point(event)
        x1,y1,x2,y2 = black_point
        (x,y)= ((int(round(y1*self._cols,0)),int(round(x1 *self._rows,0))))
        if (x,y) not in self._final_white_list:
            self._black_point.append(black_point)
        
    def _get_white_tile_list(self,event):
        '''To get the two dimensonal list of white tile
        '''
        white_point = self._get_point(event)
        x1,y1,x2,y2 = white_point
        (x,y) = ((int(round(y1*self._cols,0)),int(round(x1 *self._rows,0))))
        if (x,y) not in self._final_black_list:
            self._white_point.append(white_point)

    def _get_point(self,event:tkinter.Event):
        '''Get the frac of each step the user make
        '''
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        x = width/self._cols
        y = height/self._rows
        x1 = 0
        y1 = 0
        test = 0
        SPOT_RADIUS_FRACx = 1/(3*self._cols)
        SPOT_RADIUS_FRACy = 1/(3*self._rows)
        
        if self._rows > self._cols:
            test = self._rows
        else:
            test = self._cols
        for i in range(test):
            x1 += x
            if (x1 - x) < event.x < x1:
                for i in range(test):
                    y1 += y
                    if (y1 -y) < event.y < y1:
                        point = (((2*x1-x)/2)/width-SPOT_RADIUS_FRACx, ((2*y1-y)/2)/height-SPOT_RADIUS_FRACy, ((2*x1-x)/2)/width+SPOT_RADIUS_FRACx, ((2*y1-y)/2)/height+SPOT_RADIUS_FRACy)#frac

                        return point
                    
    def _draw_all_tiles(self) -> None:
        '''Draw all tiles on the board
        '''
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()       
        for point in self._black_point:
            topleft_frac_x, topleft_frac_y,bottomright_frac_x, bottomright_frac_y = point
            self._canvas.create_oval(
                    (topleft_frac_x * width ), (topleft_frac_y * height),
                    (bottomright_frac_x* width), (bottomright_frac_y* height),
                    fill = 'black', outline = 'white')
        for point in self._white_point:
            topleft_frac_x, topleft_frac_y,bottomright_frac_x, bottomright_frac_y = point
            self._canvas.create_oval(
                    (topleft_frac_x * width ), (topleft_frac_y * height),
                    (bottomright_frac_x* width), (bottomright_frac_y* height),
                    fill = 'white', outline = 'black')       


    def _draw_lines(self) -> None:
        '''Draw the board
        '''
        for frac_x1, frac_y1, frac_x2, frac_y2 in self._coordinates:
            self._draw_line(frac_x1, frac_y1, frac_x2, frac_y2)

    def _draw_line(self, frac_x1: float, frac_y1: float, frac_x2: float, frac_y2: float) -> None:
        '''Draw one line of the board
        '''
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        self._canvas.create_line(
            canvas_width * frac_x1, canvas_height * frac_y1,
            canvas_width * frac_x2, canvas_height * frac_y2,
            fill = 'black')
    




                        
                        
        
    def _get_board_coord(self):
        '''Get the coordinate of each step on the board, translate the coordinates
            in tkinter to the two dimensional list and put it to the game logic
        '''
        for coord in self._black_point:
            x1,y1,x2,y2 = coord
            self._final_black_list.append(((int(round(y1*self._cols,0)),int(round(x1 *self._rows,0)))))
        for coord in self._white_point:
            x1,y1,x2,y2 = coord
            self._final_white_list.append(((int(round(y1*self._cols,0)),int(round(x1 *self._rows,0)))))
        self._final_black_list = list(set(self._final_black_list))
        self._final_white_list = list(set(self._final_white_list))
        
        
    def game_play(self,event):
        '''Function that to control the game, which is the logic of the game, to
            get the point of each color tile and append to the whole flip list to
            make the game work.
        '''
        
        if self._Game.check_gameover() == False:

            point = self._get_point(event)
            x1,y1,x2,y2 = point
            move = ((int(round(y1*self._cols,0)),int(round(x1 *self._rows,0))))
            row = int(move[0])
            col = int(move[-1])
            flip_list = self._Game.valid_move_test(row,col)
            flip_point = []
            if flip_list != False:
                for i in flip_list:
                    x,y = i
                    a = x+1
                    b = y+1
                    c = 1/self._cols
                    r = 1/self._rows
                    x_center = c*(2*b-1)/2
                    y_center = r*(2*a-1)/2
                    SPOT_RADIUS_FRACx = 1/(3*self._cols)
                    SPOT_RADIUS_FRACy = 1/(3*self._rows)
                    
                    flip_point.append((x_center-SPOT_RADIUS_FRACx,y_center-SPOT_RADIUS_FRACy,x_center+SPOT_RADIUS_FRACx,y_center+SPOT_RADIUS_FRACy))



                    for i in flip_point:
                        if self._turn == 'W':
                            self._white_point.append(i)
                            if i in self._black_point:
                                self._black_point.remove(i)
                        elif self._turn == 'B':                            
                            self._black_point.append(i)
                            if i in self._white_point:
                                self._white_point.remove(i)

            try:
                if len(self._Game.valid_move_test(row,col)) != 0:
                    self._Game.make_move(row,col)
                    if self._turn == 'B':
                        self._black_point.append(point)
                    elif self._turn == 'W':
                        self._white_point.append(point)
                    self._score_list = self._Game.get_score_list()
                    self._turn = self._Game.switch()
            except TypeError:
                pass
            self._prompt.set('It is turn for '+self._turn+' player now!')
            
        
    def _on_button_clicked(self,event):
        '''Handle every time user clicked the mouse in the tkinter
        '''
        print(self._black_point) 
        if self._white_button_is_clicked == False:
            if self._turn  == 'B':
                self._get_black_tile_list(event)
            elif self._turn  == 'W':
                self._get_white_tile_list(event)
            self._draw_lines()
            self._black_point = list(set(self._black_point))
            self._white_point = list(set(self._white_point))
            self._draw_all_tiles()

            self._get_board_coord()       
        
        elif self._white_button_is_clicked == True:
            self._turn = self._Game._turn
            
            self.game_play(event)
            self._draw_lines()
            self._draw_all_tiles()
            self._black_point = list(set(self._black_point))
            self._white_point = list(set(self._white_point))
            self._get_board_coord()
            self.get_score()
            if self._Game._get_valid_moves() == []:
                self._draw_all_tiles()
                self._Game.switch()
                self._turn_count.set('Turn: '+str(self._turn)) 
                self.get_score()
                if self._turn == 'W':
                    temp_turn = 'B'
                    self._turn_count.set('Turn: '+str(temp_turn))
                elif self._turn == 'B':
                    temp_turn = 'W'
                    self._turn_count.set('Turn: '+str(temp_turn))
                self._prompt.set('It is turn for '+temp_turn+' player now!')
                if self._Game._get_valid_moves() == []:
                    self._draw_all_tiles()
                    self._game_over_check = True
            
            if self._game_over_check == True:
                self._draw_all_tiles()
                self._turn_count_label.grid_remove()
                self._game_over_label.grid(
                    row = 0 ,column = 1,padx =10,pady = 10,
                    sticky = tkinter.N)
                if self._Game.check_winner(self._rule) == 'W':
                    winner = 'WHITE PLAYER!'
                    self._prompt.set('Winner is '+ winner)
                elif self._Game.check_winner(self._rule) == 'B':
                    winner = 'BLACK PLAYER!'
                    self._prompt.set('Winner is '+ winner)
                if self._Game.check_winner(self._rule) == 'NONE':
                    self._prompt.set('There is NO WINNER for this game')

            

            

    def get_score(self):
        '''Get the current score
        '''
        self._score_list = self._Game.get_score_list()
        self._B_score = self._score_list[-1]
        self._W_score = self._score_list[0]
        
        self._black_count.set('Black: '+str(self._B_score))
        self._white_count.set('White: '+str(self._W_score))
        self._turn_count.set('Turn: '+str(self._turn))              
            
    def white_button_clicked(self):
        '''Handle command for after the white tile finished palcing
        '''
        self._white_button_is_clicked = True
        self.create_initial_board()
        self._Game.get_new_board(self._board)
        self._turn = self._color
        self.get_score()

        
        self._Game.who_goes_first(self._color)
        if self._Game._get_valid_moves() == []:
                self._Game.switch()
                if self._turn == 'W':
                    temp_turn = 'B'
                    self._turn_count.set('Turn: '+str(temp_turn))
                    
                elif self._turn == 'B':
                    temp_turn = 'W'
                    self._turn_count.set('Turn: '+str(temp_turn))
                self._prompt.set('It is turn for '+temp_turn+' player now!')
                if self._Game._get_valid_moves() == []:
                    self._game_over_check = True
        self._prompt.set('It is turn for '+self._turn+' player now!')
           
    def show(self) -> None:
        '''control the chessboard
        '''
        self._chessboard_window.grab_set()
        self._chessboard_window.wait_window()    



if __name__ == '__main__':
    InitialInterface().start()          
