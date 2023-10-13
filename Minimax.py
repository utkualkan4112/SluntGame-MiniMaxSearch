import random
import copy
class Game:
    def __init__(self, size):
        self.size = size
        self.board, self.board_numbers = self.create_board(size)
        self.players = [Player(1), Player(2)]

    def create_board(self, size):
        # Initialize an empty grid with circles containing numbers from 1 to 3.
        # Initialize an empty grid with size x size
        board = [[None for _ in range(size)] for _ in range(size)]
        board_points = [[None for _ in range(size + 1)] for _ in range(size + 1)]
        # Assign circles with numbers from 1 to 3 randomly at 20% of the intersections
        for i in range(size + 1):
            for j in range(size + 1):
                if random.random() < 0.35:  # 20% chance
                    board_points[i][j] = (random.randint(1, 3), 0)
        #board = [[None,None],[None,None]]
        #board_points = [[(1, 0), None, (1, 0)],[None, (2, 0), None],[None, None, (1, 0)]]
        return board, board_points

    def is_state_form_diamond(self, state):

        def is_diamond(x, y):
            if x + 1 < self.size and y + 1 < self.size:
                if state[x][y] == "/":
                    if state[x][y+1] == "\\":
                        if state[x+1][y+1] == "/":
                            if state[x+1][y] == "\\":
                               return True
            return False

        for x in range(len(state) - 1):
            for y in range(len(state)):
                if is_diamond(x, y):
                    return True

        return False
    def is_matrix_form_a_loop(self, matrix):

        visited = [[False for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

        def find_loops(x, y, parentx, parenty, count):
            visited[x][y] = True
            count = count + 1
            if matrix[x][y] == '/':
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, -1), (-1, 1)]
                i = 0
                while i < len(directions):
                    a, b = directions[i]
                    if x + a == goal[0] and y + b == goal[
                        1] and parentx != -1 and parenty != -1 and x + a != parentx and y + b != parenty and count > 4:
                        return True
                    if len(matrix) - 1 < x + a or x + a < 0 or len(matrix) - 1 < y + b or y + b < 0 or (
                            x + a == parentx and y + b == parenty) or visited[x + a][y + b]:
                        directions.remove(directions[i])
                    else:
                        i = i + 1
                for dx, dy in directions:
                    if dx == 1 and dy == -1:
                        if matrix[x + dx][y + dy] == '/':
                            if find_loops(x + dx, y + dy, x, y, count):
                                return True

                    elif dx == -1 and dy == 1:
                        if matrix[x + dx][y + dy] == '/':
                            if find_loops(x + dx, y + dy, x, y, count):
                                return True

                    else:
                        if matrix[x + dx][y + dy] == '\\':
                            if find_loops(x + dx, y + dy, x, y, count):
                                return True

            elif matrix[x][y] == '\\':
                directions = [(-1, -1), (1, 1), (-1, 0), (0, -1), (0, 1), (1, 0)]
                i = 0
                while i < len(directions):
                    a, b = directions[i]
                    if x + a == goal[0] and y + b == goal[
                        1] and parentx != -1 and parenty != -1 and x + a != parentx and y + b != parenty and count > 4:
                        return True
                    if len(matrix) - 1 < x + a or x + a < 0 or len(matrix) - 1 < y + b or y + b < 0 or (
                            x + a == parentx and y + b == parenty) or visited[x + a][y + b]:
                        directions.remove(directions[i])
                    else:
                        i = i + 1
                for dx, dy in directions:
                    if dx == -1 and dy == -1:
                        if matrix[x + dx][y + dy] == '\\':
                            if find_loops(x + dx, y + dy, x, y, count):
                                return True
                    elif dx == 1 and dy == 1:
                        if matrix[x + dx][y + dy] == '\\':
                            if find_loops(x + dx, y + dy, x, y, count):
                                return True
                    else:
                        if matrix[x + dx][y + dy] == '/':
                            if find_loops(x + dx, y + dy, x, y, count):
                                return True

            return False

        for x in range(len(matrix) - 1):
            for y in range(len(matrix)):
                goal = [x, y]
                count = 0
                if find_loops(x, y, -1, -1, count):
                    return True
                visited = [[False for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        return False

    def is_terminal_state(self, state):
        # Check if all cells are filled.
        for row in state:
            for cell in row:
                if cell is None:
                    return False
        return True

    def transition(self, board, state_numbers, move):
        state = copy.deepcopy(board)
        state_points = copy.deepcopy(state_numbers)
        # Change the state according to the given move.
        row, col, diagonal = move
        if state[row][col] is None:
            state[row][col] = diagonal
            #if self.is_matrix_form_a_loop(state) or self.is_state_form_diamond(state):  # Add loop condition for illegal moves
                #raise ValueError("Invalid move. Cell is formed a loop")
            #else:
            if diagonal == "/":
                if state_points[row][col + 1] != None and state_points[row][col + 1][1] == 0:
                    if self.intersect_points(state, row, col + 1):
                        state_points[row][col + 1] = (state_points[row][col + 1][0], 1)
                    #if not self.intersects_constraint(state, row, col + 1):
                        #raise ValueError("Invalid move. Number of intersect is exceed.")

                if state_points[row + 1][col] != None and state_points[row + 1][col][1] == 0:
                    if self.intersect_points(state, row + 1, col):
                        state_points[row + 1][col] = (state_points[row + 1][col][0], 1)
                    #if not self.intersects_constraint(state, row + 1, col):
                        #raise ValueError("Invalid move. Number of intersect is exceed.")
            elif diagonal == "\\":
                if state_points[row][col] != None and state_points[row][col][1] == 0:
                    if self.intersect_points(state, row, col):
                        state_points[row][col] = (state_points[row][col][0], 2)
                    #if not self.intersects_constraint(state, row, col):
                        #raise ValueError("Invalid move. Number of intersect is exceed.")
                if state_points[row + 1][col + 1] != None and state_points[row + 1][col + 1][1] == 0:
                    if self.intersect_points(state, row + 1, col + 1):
                        state_points[row + 1][col + 1] = (state_points[row + 1][col + 1][0], 2)
                    #if not self.intersects_constraint(state, row + 1, col + 1):
                        #raise ValueError("Invalid move. Number of intersect is exceed.")
        else:
            raise ValueError("Invalid move. Cell is already filled.")
        return state, state_points

    def alpha_beta_search(self, state, state_points, player, alpha, beta, depth = 0, max_depth = 9):
        if depth == max_depth or self.is_terminal_state(state):
            return self.payoff(state_points), None
        elif len(self.get_possible_moves(player, state)) == 0:
            best_score = float('-inf') if player == self.players[1] else float('inf')
            best_move = None
            return best_score, best_move

        best_score = float('-inf') if player == self.players[0] else float('inf')
        best_move = None

        for move in self.get_possible_moves(player, state):
            new_state, new_state_points = self.transition(state, state_points, move)
            score, _ = self.alpha_beta_search(new_state, new_state_points, self.get_opponent(player), alpha, beta, depth + 1)
            if player == self.players[0]:  # Player 1 wants to maximize the score
                if score > best_score:
                    best_score = score
                    best_move = move
                alpha = max(alpha, score)
            else:  # Player 2 wants to minimize the score
                if score < best_score:
                    best_score = score
                    best_move = move
                beta = min(beta, score)
            if alpha >= beta:  # Prune the remaining branches
                break
        return best_score, best_move

    def intersects_constraint(self, state, x, y):
        count = 0
        if x-1 >= 0 and y-1 >= 0:
            if state[x-1][y-1] == '\\':
                count+=1
        if x-1 >= 0 and y < self.size:
            if state[x-1][y] == '/':
                count+=1
        if x < self.size and y < self.size:
            if state[x][y] == '\\':
                count+=1
        if x < self.size and y-1 >= 0:
            if state[x][y-1] == '/':
                count+=1
        if count > self.board_numbers[x][y][0]:
            return False
        return True

    def intersect_points(self, state, x, y):
        count = 0
        if x - 1 >= 0 and y - 1 >= 0:
            if state[x - 1][y - 1] == '\\':
                count += 1
        if x - 1 >= 0 and y < self.size:
            if state[x - 1][y] == '/':
                count += 1
        if x < self.size and y < self.size:
            if state[x][y] == '\\':
                count += 1
        if x < self.size and y - 1 >= 0:
            if state[x][y - 1] == '/':
                count += 1
        if count == self.board_numbers[x][y][0]:
            return True
        return False
    def get_possible_moves(self, player, state):
        # Return a list of all possible moves for the player in the current state
        possible_moves = []

        diagonal = '/' if player == self.players[0] else '\\'
        for i in range(self.size):
            for j in range(self.size):
                if state[i][j] is None: # Also add loop condition here
                    #try_state = copy.deepcopy(state)
                    #try_state[i][j] = diagonal
                    #if (not self.is_matrix_form_a_loop(try_state)) and (not self.is_state_form_diamond(try_state)):
                    possible_moves.append((i, j, diagonal))
                        #if diagonal == '/':
                            #if self.board_numbers[i][j + 1] != None:
                                #if self.intersects_constraint(try_state, i, j + 1):
                                    #possible_moves.append((i, j, diagonal))
                            #if self.board_numbers[i + 1][j] != None:
                                #if self.intersects_constraint(try_state, i + 1, j):
                                    #possible_moves.append((i, j, diagonal))
                        #else:
                            #if self.board_numbers[i][j] != None:
                                #if self.intersects_constraint(try_state, i, j):
                                    #possible_moves.append((i, j, diagonal))
                            #if self.board_numbers[i + 1][j + 1] != None:
                                #if self.intersects_constraint(try_state, i + 1, j + 1):
                                    #possible_moves.append((i, j, diagonal))

        random.shuffle(possible_moves)
        return possible_moves

    def get_opponent(self, player):
        # Return the opponent of the given player
        return self.players[0] if player == self.players[1] else self.players[1]


    def payoff(self, state_points):
        # Calculate the score for the player in the given state
        points = 0
        for row in range(self.size + 1):
            for col in range(self.size + 1):
                if state_points[row][col] != None and state_points[row][col][1] == 1:
                    points = points + state_points[row][col][0]
                elif state_points[row][col] != None and state_points[row][col][1] == 2:
                    points = points - state_points[row][col][0]
        return points


    def play(self):
        print("Current board:")
        for row in self.board:
            print(row)
        print("Point Board:")
        for row in self.board_numbers:
            print(row)
        while not self.is_terminal_state(self.board):
            for player in self.players:
                print(f"It's Player {player.player_number}'s turn.")
                if player == self.players[0]:  # User's turn
                    while True:
                        try:
                            row = int(input("Enter the row: "))
                            col = int(input("Enter the column: "))
                            move = (row, col, '/')
                            self.board, self.board_numbers = self.transition(self.board, self.board_numbers, move)
                            break
                        except ValueError:
                            print("Invalid move. Try again.")
                else:  # Computer's turn
                    _, move = self.alpha_beta_search(self.board, self.board_numbers, player, float('-inf'), float('inf'))
                    #if move == None:
                        #for row in range(self.size):
                            #for col in range(self.size):
                                #if self.board[row][col] == None:
                                    #move = (row, col, '\\')
                    self.board, self.board_numbers = self.transition(self.board, self.board_numbers, move)



                print(f"Player {player.player_number} moved: {move}")
                print("Current board:")
                for row in self.board:
                    print(row)
                print("Point Board:")
                for row in self.board_numbers:
                    print(row)
        if(self.get_winner() != None):
            print(f"Game over! The winner is Player {self.get_winner().player_number}")
        else:
            print(f"Game over! Draw")

    def get_winner(self):
        if self.payoff(self.board_numbers) > 0:
            return self.players[0]
        elif self.payoff(self.board_numbers) == 0:
            return None
        else:
            return self.players[1]



class Player:
    def __init__(self, player_number):
        self.player_number = player_number
        self.score = 0


if __name__ == "__main__":
    game = Game(4)
    game.play()
