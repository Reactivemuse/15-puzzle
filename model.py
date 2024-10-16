class Situation:
    def __init__(self, board, position, goal):
        self.board = board
        self.position = position
        self.goal = goal

    def is_solved(self):
        return self.board == self.goal

    def isValid(self, row, col):
        return 0 <= row < len(self.board) and 0 <= col < len(self.board[0])

    def convertation(self, board):
        return [num for row in board for num in row]

    def print_board(self):
        for row in self.board:
            for num in row:
                print(num, end=" ")
            print()
        print("-" * 15)
        