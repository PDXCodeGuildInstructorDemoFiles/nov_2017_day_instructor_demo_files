class CoordsTTTBoard:
    def __init__(self):
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    def place_token(self, x, y, token):
        self.board[x][y] = token

    def calc_winner(self):

        for row in self.board:
            if row[0] != ' ' and all(x == row[0] for x in row):
                return row[0]

        for col in zip(*self.board):
            if col[0] != ' ' and all(x == col[0] for x in col):
                return col[0]

        if self.board[1][1] != " ":
            if (self.board[1][1] == self.board[0][0] == self.board[2][2]) or (self.board[1][1] == self.board[0][2] == self.board[2][0]):
                return self.board[1][1]
        return None

    def __str__(self):
        string = ''
        for row in self.board:
            string += '{}|{}|{}\n'.format(row[0], row[1], row[2])
        return string


if __name__ == '__main__':
    b = CoordsTTTBoard()
    b.place_token(1, 1, 'X')
    b.place_token(0, 0, 'O')
    b.place_token(1, 0, 'X')
    print(b)
