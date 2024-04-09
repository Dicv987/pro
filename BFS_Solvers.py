from collections import deque
import heapq 
import copy
from Node import Node
from Heuristics import Heuristics  

class BFS_Solver:
    def __init__(self, rubik):
        self.rubik = rubik

    def bfs(self, heuristic_func):
        initial_state = Node(copy.deepcopy(self.rubik.faces), heuristic_func(self.rubik.faces))
        desired_state = Node(copy.deepcopy(self.rubik.faces_solved))

        visited = set()
        queue = deque([initial_state])

        while queue:
            current_node = queue.popleft()

            if current_node == desired_state:
                return current_node.path

            state_hash = hash(current_node)
            if state_hash not in visited:
                visited.add(state_hash)

                for move_func in [self.rubik.move_U, self.rubik.move_R, self.rubik.move_F, self.rubik.move_L, self.rubik.move_D, self.rubik.move_B]:
                    for clockwise in [True, False]:
                        self.rubik.faces = copy.deepcopy(current_node.rubik)
                        move_func(clockwise)
                        new_state_rubik = copy.deepcopy(self.rubik.faces)
                        heuristic_value = heuristic_func(new_state_rubik)
                        new_state = Node(new_state_rubik, heuristic_value)
                        new_state.path = current_node.path + [f"{move_func.__name__} ({'CW' if clockwise else 'CCW'})"]

                        if hash(new_state) not in visited:
                            queue.append(new_state)

        return False

    def a_star(self):
        initial_rubik = copy.deepcopy(self.rubik.faces)
        initial_heuristic = self.heuristic(initial_rubik)
        initial_state = Node(initial_rubik, initial_heuristic)

        queue = [(initial_state.heuristic_value, initial_state)]
        visited = set()

        while queue:
            _, current_node = heapq.heappop(queue)

            if self.is_goal(current_node.rubik):
                return current_node.path

            state_hash = hash(current_node)
            if state_hash not in visited:
                visited.add(state_hash)

                for move_func in [self.rubik.move_U, self.rubik.move_R, self.rubik.move_F, self.rubik.move_L, self.rubik.move_D, self.rubik.move_B]:
                    for clockwise in [True, False]:
                        move_name = f"{move_func.__name__} ({'CW' if clockwise else 'CCW'})"

                        # Evitar el movimiento inverso inmediatamente después del último movimiento
                        if current_node.last_move:
                            last_move_name, last_move_dir = current_node.last_move.split(' ')
                            if move_func.__name__ == last_move_name and clockwise != (last_move_dir == '(CW)'):
                                continue

                        new_rubik = copy.deepcopy(current_node.rubik)
                        self.rubik.faces = new_rubik
                        move_func(clockwise)
                        new_rubik_state = copy.deepcopy(self.rubik.faces)

                        new_heuristic = self.heuristic(new_rubik_state)
                        new_node = Node(new_rubik_state, new_heuristic, move_name, current_node.path + [move_name])

                        if hash(new_node) not in visited:
                            heapq.heappush(queue, (len(new_node.path) + new_node.heuristic_value, new_node))

        return False

    def heuristic(self, state):
        return Heuristics.exact_position_heuristic(state)
    
    def is_goal(self, state):
        # Asume que `self.rubik.faces_solved` es el estado objetivo
        return state == self.rubik.faces_solved
