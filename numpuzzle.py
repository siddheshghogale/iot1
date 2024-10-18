import numpy as np
import heapq

class PuzzleState:
    def __init__(self, board, zero_pos, moves=0, previous=None):
        self.board = board
        self.zero_pos = zero_pos
        self.moves = moves
        self.previous = previous
        self.cost = self.moves + self.heuristic()
    def heuristic(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                value = self.board[i][j]
                if value != 0:  # Ignore the blank tile
                    target_x, target_y = divmod(value - 1, 3)
                    distance += abs(i - target_x) + abs(j - target_y)
        return distance
    def get_neighbors(self):
        neighbors = []
        x, y = self.zero_pos
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_board = np.copy(self.board)
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                neighbors.append(PuzzleState(new_board, (new_x, new_y), self.moves + 1, self))
        return neighbors
    def __lt__(self, other):
        return self.cost < other.cost
def a_star(initial_board):
    initial_zero_pos = tuple(np.argwhere(initial_board == 0)[0])  # Get the first matching position
    initial_state = PuzzleState(initial_board, initial_zero_pos)
    goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    priority_queue = []
    visited = set()
    heapq.heappush(priority_queue, initial_state)
    while priority_queue:
        current_state = heapq.heappop(priority_queue)
        if np.array_equal(current_state.board, goal_state):
            return current_state
        visited.add(tuple(map(tuple, current_state.board)))
        for neighbor in current_state.get_neighbors():
            if tuple(map(tuple, neighbor.board)) not in visited:
                heapq.heappush(priority_queue, neighbor)
    return None
def print_solution(solution):
    path = []
    while solution:
        path.append(solution.board)
        solution = solution.previous
    for step in reversed(path):
        print(step,"\n")


if __name__ == "__main__":
    initial_board = np.array([[1, 2, 3],
                              [5, 7, 8],
                              [6, 0, 4]])
    solution = a_star(initial_board)
    if solution:
        print("\nSolution found in {} moves:".format(solution.moves))
        
        print_solution(solution)

    else:
        print("No solution found.")
