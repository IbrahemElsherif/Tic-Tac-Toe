import os 
# Declare who has won
# and declare the final board
def clear_screen():
    os.system("cls" if os.name =="nt" else "clear" )



class Player:
    
    def __init__(self):
        self.name=''
        self.symbol=''
        
    def choose_name(self):
        while True:
            name = input("Enter your name: ")
            if name.isalpha():
                self.name=name
                break
            print("Invalid name")
        
    def choose_symbol(self,other_symbol):
        while True:
            symbol=input(f"{self.name} Enter a symbol: ").upper()
            if symbol.isalpha() and len(symbol) ==1 and symbol!=other_symbol:
                self.symbol=symbol
                break
            print("Invlaid symbol")
            
class Menu:
        
    def display_main_menu(self):
        print("Let's Play tic tac toe")
        print("1- Start game")
        print("2- Quit game")
        while True:
            choice = input("Choose 1 or 2:\n")
            if choice == '1'  or choice=='2':
                return choice
            else:
                print("Please choose 1 or 2")
        
    def display_end_menu(self):
        menu_text = """
        1- Restart game
        2- Quit game
        Choose 1 or 2:
        """
        while True:
            choice = input(menu_text)
            if choice == '1' or choice == '2':
                return choice
            else:
                print("Please choose 1 or 2.")
    
class Board:
    
    def __init__(self):
        self.board=[str(i) for i in range(1,10)]
        
    def display_board(self):
        for i in range(0,9,3):
            print("|".join(self.board[i:i+3]))
            if i<6:
                print('-'*5)
        
    def update_board(self,choice,symbol):
        if self.is_valid_move(choice):
            self.board[choice-1]=symbol
            return True
        return False
    
    def is_valid_move(self,choice):
        return self.board[choice-1].isdigit()
             
    def reset_board(self):
        self.board = [str(i) for i in range(1,10)]      

class Game:
    
    def __init__(self):
        self.players=[Player(),Player()]
        self.board=Board()
        self.menu=Menu()
        self.current_player_index=0
        
    def start_game(self):
        choice=self.menu.display_main_menu()
        if choice == "1" :
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()
            
    def setup_players(self):
        other_symbol = None  # Initialize to None to ensure it's defined
        for number, player in enumerate(self.players, start=1):
            print(f"Player {number}, enter your details:")
            player.choose_name()
            player.choose_symbol(other_symbol)
            other_symbol = player.symbol  # Store the symbol of the first player
            clear_screen()

    def play_game(self):
        while True:
            self.play_turn()
            winner=self.check_win()
            if winner:
                clear_screen()
                self.board.display_board()  # Display the final board
                print(f"Congratulations, {winner.name}! You have won the game!")
                break
            if self.check_draw():
                clear_screen()
                self.board.display_board()  # Display the final board
                print("It's a draw!")
                break
        choice = self.menu.display_end_menu()
        if choice =="1":
            self.restart_game()
        else:
            self.quit_game()
       
            
    def  play_turn(self):
        player=self.players[self.current_player_index]
        clear_screen()
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice=int(input("Choose a cell (1-9): "))
                if 1<=cell_choice<=9 and self.board.update_board(cell_choice,player.symbol):
                 break
                else:
                    print("Invalid move")
            except ValueError:
                print("please a number between (1-9)")
        self.switch_player()
        clear_screen()
        
    def switch_player(self):
        self.current_player_index= 1-self.current_player_index
    
    def check_win(self):
        winning_combination=[
            [0,1,2],[3,4,5],[6,7,8], # rows
            [0,3,6],[1,4,7],[2,5,8], # columns
            [0,4,8],[2,4,6] # diagonals
        ]
    
        for combo in winning_combination:
            if (self.board.board[combo[0]]==self.board.board[combo[1]]
                ==self.board.board[combo[2]]):
                return self.players[1 - self.current_player_index]  # Return the winning player object
        return None 
    
    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board) # generator expression
    
    def restart_game(self):
        self.board.reset_board()
        self.current_player_index=0
        self.play_game()
    
    def quit_game(self):
        print("Thank you for playing ^_^ ")
        exit()
    
    
game=Game()
game.start_game()