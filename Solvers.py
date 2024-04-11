from collections import deque
import heapq 
import copy
from Node import Node
from Heuristics import Heuristics 
from queue import PriorityQueue
import time

class Solvers:

    INF = float("inf")

    def __init__(self, rubik):
        self.rubik = rubik

    def bfs(self):
        initial_state = Node(copy.deepcopy(self.rubik.faces), 0)
        desired_state = self.rubik.faces_solved

        visited = set()
        queue = deque([initial_state])

        while queue:
            current_node = queue.popleft()

            if current_node.rubik == desired_state:
                return current_node.path

            visited.add(current_node)

            for move_func in [self.rubik.move_U, self.rubik.move_R, self.rubik.move_F, self.rubik.move_L, self.rubik.move_D, self.rubik.move_B]:
                for clockwise in [True, False]:
                    self.rubik.faces = copy.deepcopy(current_node.rubik)
                    move_func(clockwise)
                    new_state_rubik = copy.deepcopy(self.rubik.faces)

                    new_node = Node(new_state_rubik, path=current_node.path[:])
                    new_node.add_move(move_func, clockwise)

                    if new_node not in visited:
                        queue.append(new_node)
                        visited.add(new_node)

        return False

    def best_first_search(self, heuristic_function):
        initial_rubik = copy.deepcopy(self.rubik.faces)
        initial_heuristic = heuristic_function(initial_rubik)
        initial_state = Node(initial_rubik, initial_heuristic)

        queue = PriorityQueue()
        queue.put((initial_state.heuristic_value, initial_state))
        visited = set()

        while not queue.empty():
            _, current_node = queue.get()

            if self.is_goal(current_node.rubik):
                return current_node.path

            state_hash = hash(str(current_node.rubik))  # Convierte el estado del Rubik a una cadena para el hash
            if state_hash not in visited:
                visited.add(state_hash)

                for move_func in [self.rubik.move_U, self.rubik.move_R, self.rubik.move_F, self.rubik.move_L, self.rubik.move_D, self.rubik.move_B]:
                    for clockwise in [True, False]:
                        move_name = f"{move_func.__name__} ({'CW' if clockwise else 'CCW'})"

                        if current_node.last_move:
                            last_move_name, last_move_dir = current_node.last_move.split(' ')
                            if move_func.__name__ == last_move_name and clockwise != (last_move_dir == '(CW)'):
                                continue

                        new_rubik = copy.deepcopy(current_node.rubik)
                        self.rubik.faces = new_rubik
                        move_func(clockwise)
                        new_rubik_state = copy.deepcopy(self.rubik.faces)

                        new_heuristic = heuristic_function(new_rubik_state)
                        new_node = Node(new_rubik_state, new_heuristic, move_name, current_node.path + [move_name])

                        new_state_hash = hash(str(new_rubik_state))
                        if new_state_hash not in visited:
                            queue.put((new_heuristic, new_node))

        return False

    def a_star(self,heuristic_function):
        initial_rubik = copy.deepcopy(self.rubik.faces)
        initial_heuristic = heuristic_function(initial_rubik)
        initial_state = Node(initial_rubik, initial_heuristic)

        queue = PriorityQueue()
        queue.put((initial_state.heuristic_value, initial_state))
        visited = set()

        while not queue.empty():
            _, current_node = queue.get()

            if self.is_goal(current_node.rubik):
                return current_node.path

            state_hash = hash(current_node)
            if state_hash not in visited:
                visited.add(state_hash)

                for move_func in [self.rubik.move_U, self.rubik.move_R, self.rubik.move_F, self.rubik.move_L, self.rubik.move_D, self.rubik.move_B]:
                    for clockwise in [True, False]:
                        move_name = f"{move_func.__name__} ({'CW' if clockwise else 'CCW'})"

                        if current_node.last_move:
                            last_move_name, last_move_dir = current_node.last_move.split(' ')
                            if move_func.__name__ == last_move_name and clockwise != (last_move_dir == '(CW)'):
                                continue

                        new_rubik = copy.deepcopy(current_node.rubik)
                        self.rubik.faces = new_rubik
                        move_func(clockwise)
                        new_rubik_state = copy.deepcopy(self.rubik.faces)

                        new_heuristic = heuristic_function(new_rubik_state)
                        new_path_length = len(current_node.path) + 1  # Añade 1 por el movimiento actual
                        new_node = Node(new_rubik_state, new_heuristic, move_name, current_node.path + [move_name])

                        if hash(new_node) not in visited:
                            total_cost = new_path_length + new_heuristic  # Suma del costo del camino y el valor heurístico
                            queue.put((total_cost, new_node))

        return False
    

    def iterative_deepening_A_star(self, heuristic):
        initial_rubik = copy.deepcopy(self.rubik.faces)
        initial_heuristic = heuristic(initial_rubik)
        start_node = Node(initial_rubik, initial_heuristic)
        bound = start_node.heuristic_value
        path = [start_node]
        
        while True:
            t = self.__search(path, 0, bound, heuristic)
            if t is True:
                return [node.last_move for node in path[1:]]  # Returns only the moves
            if t == float('inf'):
                return None
            bound = t

    def __search(self, path, g, bound, heuristic):
        node = path[-1]
        f = g + node.heuristic_value
        if f > bound:
            return f
        if self.is_goal(node.rubik):
            return True

        min = float('inf')
        for move_func in [self.rubik.move_U, self.rubik.move_R, self.rubik.move_F, self.rubik.move_L, self.rubik.move_D, self.rubik.move_B]:
            for clockwise in [True, False]:
                self.rubik.faces = copy.deepcopy(node.rubik)  # Reset the state of the cube to the current node
                move_func(clockwise)  # Apply the move
                new_heuristic = heuristic(self.rubik.faces)
                move_name = f"{move_func.__name__} ({'CW' if clockwise else 'CCW'})"
                new_node = Node(copy.deepcopy(self.rubik.faces), new_heuristic, move_name, node.path + [move_name])
                if new_node not in path:  # Check for cycle in the path
                    path.append(new_node)
                    t = self.__search(path, g + 1, bound, heuristic)
                    if t is True:
                        return True
                    if t < min:
                        min = t
                    path.pop()
        return min

    def is_goal(self, rubik):
        return rubik == self.rubik.faces_solved