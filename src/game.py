class Game(object):
    """
    Game class responsible for initializing the game. Requires an array of
    two players and a board
    """

    def __init__(self, players=[]):
        self.players = players  # mock for players
        self.board = []  # mock for board
        self.play_index = 0

    def current_player(self):
        return self.players[self.play_index]

    def take_turn(self):
        self.print_board()
        try:
            self.place_piece()
        except ValueError:
            print("This isn't a valid location, try again")
            self.place_piece()

        self.print_board()
        self.switch_player()

    def switch_player(self):
        self.play_index = 1 if self.play_index == 0 else self.play_index == 0

    def place_piece(self):
        loc = self.current_player.place_piece()
        self.board.place_piece(loc)

    def game_over(self):
        return self.board.check_winnner

    def is_draw(self):
        return self.play_index == 8 and not self.board.check_winnner()

    def play(self):
        while not self.game_over():
            if self.is_draw():
                print("Draw!")
                return None
            else:
                self.take_turn()

        prev_player = self.players[(self.play_index - 1) % 2]["name"]
        print("You win {:s}!").format(prev_player)


p1 = {"name": 'm', "mark": 'x'}
p2 = {"name": 'l', "mark": 'y'}
g = Game(players=[p1, p2])
