class Board(object):
    """Contains a list-grid of spaces to place pieces"""
    def __init__(self):
        self.grid = self.generate_board()

    def __str__(self):
        return self.grid

    def get(self, coord_tuple):
        x, y = coord_tuple
        return self.grid[x][y]

    def place_piece(self, coord_tuple, value):
        x, y = coord_tuple
        if self.is_valid(coord_tuple):
            self.grid[x][y] = value
        else:
            raise ValueError("The location is unavailable")

    def is_valid(self, location):
        return self.get(location) is None

    def check_winnner(self, mark):
        return (
            self.check_vertical(mark) or
            self.check_horizontal(mark) or
            self.check_diagonal(mark)
        )
        pass

    def check_horizontal(self, mark):
        horizontal_win = False
        for row in self.grid:
            won = all(
                isinstance(marker, str)
                and marker == mark
                for marker in row
            )
            if won:
                horizontal_win = True
        return horizontal_win

    def check_vertical(self, mark):
        vertical_win = False
        column = 0

        while column < len(self.grid):
            column_list = []

            for index in range(column, len(self.grid)):
                column_list.append(self.grid[index][column])

            won = all(
                isinstance(marker, str)
                and marker == mark
                for marker in column_list
            )
            if won:
                vertical_win = True

            column += 1
        return vertical_win

    def check_diagonal(self, mark):
        length = len(self.grid)
        # left to bottom right
        xL = 0
        yL = 0

        # right to bottom left
        xR = 0
        yR = 2

        # Pass from top left to bottom right
        left_marks = []
        right_marks = []

        while xL < length and yL < length:
            spot_left = self.grid[xL][yL]
            spot_right = self.grid[xR][yR]

            left_marks.append(spot_left == mark)
            right_marks.append(spot_right == mark)

            xL += 1
            yL += 1
            xR += 1
            yR -= 1

        return all(left_marks) or all(right_marks)

    def generate_board(self, dimention=3):
        """
        Helper method for generating the board for initialization. Pass one
        number into the dimention, defaults to three. Will create an NxN
        grid.
        """
        grid = []

        for row in range(dimention):
            col_row = []
            for col in range(dimention):
                col_row.append(None)
            grid.append(col_row)

        return grid
