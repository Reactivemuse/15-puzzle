class Situation:
    def __init__(self, board, position, goal, depth=0):
        self.board = board  # Не копируем board в __init__, копирование происходит в make_move
        self.position = position
        self.goal = goal
        self.size = 3
        self.depth = depth
        self.n = 4


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
    
    def __hash__(self):
        return hash((tuple(self.position), tuple(self.convertation(self.board))))
    
    def __eq__(self, other):
        if len(self.board) != len(other.board) or len(self.board[0]) != len(other.board[0]):
            return False
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] != other.board[i][j]:
                    return False
        return True  # Если все элементы совпадают