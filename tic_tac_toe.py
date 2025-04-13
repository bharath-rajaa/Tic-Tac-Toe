class TicTacToe:
    def __init__(self):
        self.board = [None] * 9
        self.current_player = 'X'
        self.game_over = False

    def make_move(self, position):
        if self.game_over or self.board[position] is not None:
            return {'message': 'Invalid move!', 'game_over': self.game_over}
        
        self.board[position] = self.current_player
        if self.check_winner(self.current_player):
            self.game_over = True
            return {'message': f'Player {self.current_player} wins!', 'game_over': True}
        elif None not in self.board:
            self.game_over = True
            return {'message': 'Draw!', 'game_over': True}
        
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return {'message': f'Player {self.current_player}\'s turn', 'game_over': False}

    def check_winner(self, player):
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        return any(all(self.board[i] == player for i in combo) for combo in wins)

    def reset(self):
        self.board = [None] * 9
        self.current_player = 'X'
        self.game_over = False
