import os



class Tictactoe():

    def __init__(self):
        '''define the list to update user inputs'''
        self.list1=['-' for x in range(1,10)]

        '''graphical representation of the board'''
        self.board=(f'{self.list1[0]} | {self.list1[1]} | {self.list1[2]}\n_________\n{self.list1[3]} | {self.list1[4]} | {self.list1[5]}\n_________\n{self.list1[6]} | {self.list1[7]} | {self.list1[8]}' )
        print (self.board)
        
        '''User selects X or O'''
        self.y1=''
        self.x1=input('Player 1 starts, please pick "X" or "O" to start: ').upper()
        while self.x1!='X' and self.x1!='O':
            print ('Invalid selection \n')
            self.x1=input('Player 1 starts, please pick "X" or "O" to start: ').upper()
        if self.x1=='X':
            self.y1='O'
            print ('Player 1 is X')
            print ('Plyaer 2 is O')
        elif self.x1=='O':
            self.y1='X'
            print ('Player 1 is O')
            print ('Plyaer 2 is X')

        self.flag=True
        '''Keeps track who played the last'''
        self.turn='Player 1'

    '''to update the display board after each user input'''
    def update_board(self):
        self.board=(f'{self.list1[0]} | {self.list1[1]} | {self.list1[2]}\n_________\n{self.list1[3]} | {self.list1[4]} | {self.list1[5]}\n_________\n{self.list1[6]} | {self.list1[7]} | {self.list1[8]}' )
        print (self.board)

    '''record player1 turns and update the board'''
    def player1_turn(self):
        p1=int(input('Player1, Please pick a position on the board between 1-9:  '))
        while p1<=0 or p1>9:
            print ('Invalid selection')
            p1=int(input('Player1,Please pick a position on the board between 1-9:  '))
        act_p1=p1-1
        while self.list1[act_p1]!='-':
            print ('Position already taken, please pick an empty position')
            p1=int(input('Player1, Please pick a position on the board between 1-9:  '))
            act_p1=p1-1
        self.list1[act_p1]=self.x1
        self.update_board()
        self.turn='Player 1'
    '''record player2 turns and update the board'''
    def player2_turn(self):
        p1=int(input('Player2, Please pick a position on the board between 1-9:  '))
        while p1<=0 or p1>9:
            print ('Invalid selection')
            p1=int(input('Player2, Please pick a position on the board between 1-9:  '))
        act_p1=p1-1
        while self.list1[act_p1]!='-':
            print ('Position already taken, please pick an empty position')
            p1=int(input('Player2, Please pick a position on the board between 1-9:  '))
            act_p1=p1-1
        self.list1[act_p1]=self.y1
        self.update_board()
        self.turn='Player 2'

    '''To check if there's a winner or if it's a tie and stop the gameplay'''
    def logic(self):
        if (self.list1[0]==self.list1[1]==self.list1[2]!='-') or (self.list1[3]==self.list1[4]==self.list1[5]!='-') or (self.list1[6]==self.list1[7]==self.list1[8]!='-'):
            self.flag=False
        elif (self.list1[0]==self.list1[4]==self.list1[8]!='-') or (self.list1[2]==self.list1[4]==self.list1[6]!='-'):
            self.flag=False
        elif (self.list1[0]==self.list1[3]==self.list1[6]!='-') or (self.list1[1]==self.list1[4]==self.list1[7]!='-') or (self.list1[2]==self.list1[5]==self.list1[8]!='-'):
            self.flag=False
        elif '-' not in self.list1:
            self.turn='No one'
            self.flag=False
            
        else:
            pass

     '''clears the screen each time to prevent multiple boards being printed on screen for each input'''       
    def screenwipe(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.update_board()
        
    


if __name__=='__main__':

    test=Tictactoe()
    while test.flag:
        test.player1_turn()
        test.logic()
        '''tests the logic and breaks out of the loop as soon as player1 wins'''
        if test.flag==False:
            print (f'Game over, {test.turn} has won the game. ')
            break
        test.screenwipe()
        test.player2_turn()
        test.logic()
        '''tests the logic and breaks out of the loop as soon as player2 wins'''
        if test.flag==False:
            print (f'Game over, {test.turn} has won the game. ')
            break
        test.screenwipe()
        
      

    



