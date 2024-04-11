from rubik import Rubik
from Solvers import Solvers
from Heuristics import Heuristics
import time
import copy

def main():
    print("Resolviendo cubo de Rubik...")
    rubik = Rubik()
    rubik.scrambles(6)


    scrambled_state_1 = copy.deepcopy(rubik)
    scrambled_state_2 = copy.deepcopy(rubik)
    scrambled_state_3 = copy.deepcopy(rubik)
    scrambled_state_4 = copy.deepcopy(rubik)
    scrambled_state_5 = copy.deepcopy(rubik)
    scrambled_state_6 = copy.deepcopy(rubik)
    scrambled_state_7 = copy.deepcopy(rubik)
    scrambled_state_8 = copy.deepcopy(rubik)

    # #BFS No Heurístico
    # print("BFS No Heurístico")
    # start_time = time.time()
    # solver = Solvers(scrambled_state_1)
    # solution = solver.bfs()
    # print(solution)
    # print("Longitud de la solución: ", len(solution))
    # print("--- %s seconds ---" % (time.time() - start_time))

    # #BFS Heurístico exact_position_heuristic

    # print("BFS Heurístico exact_position_heuristic")
    # start_time = time.time()
    # solver = Solvers(scrambled_state_2)
    # solution = solver.best_first_search(Heuristics.exact_position_heuristic)
    # print(solution)
    # print("Longitud de la solución: ", len(solution))
    # print("--- %s seconds ---" % (time.time() - start_time))

    # #BFS Heurístico pattern_matching
    # print("BFS Heurístico pattern_matching")
    # start_time = time.time()
    # solver = Solvers(scrambled_state_3)
    # solution = solver.best_first_search(Heuristics.pattern_matching)
    # print(solution)
    # print("Longitud de la solución: ", len(solution))
    # print("--- %s seconds ---" % (time.time() - start_time))

    # #BFS Heurístico orientaciones_incorrectas
    # print("BFS Heurístico orientaciones_incorrectas")
    # start_time = time.time()
    # solver = Solvers(scrambled_state_4)
    # solution = solver.best_first_search(Heuristics.orientaciones_incorrectas)
    # print(solution)
    # print("Longitud de la solución: ", len(solution))
    # print("--- %s seconds ---" % (time.time() - start_time))
    

    # # A* Heurístico exact_position_heuristic
    # print("A* Heurístico exact_position_heuristic")
    # start_time = time.time()
    # solver = Solvers(scrambled_state_5)
    # solution = solver.a_star(Heuristics.exact_position_heuristic)
    # print(solution)
    # print("Longitud de la solución: ", len(solution))
    # print("--- %s seconds ---" % (time.time() - start_time))

    # # A* Heurístico pattern_matching
    # print("A* Heurístico pattern_matching")
    # start_time = time.time()
    # solver = Solvers(scrambled_state_6)
    # solution = solver.a_star(Heuristics.pattern_matching)
    # print(solution)
    # print("Longitud de la solución: ", len(solution))
    # print("--- %s seconds ---" % (time.time() - start_time))

    # # A* Heurístico orientaciones_incorrectas
    # print("A* Heurístico orientaciones_incorrectas")
    # start_time = time.time()
    # solver = Solvers(scrambled_state_7)
    # solution = solver.a_star(Heuristics.orientaciones_incorrectas)
    # print(solution)
    # print("Longitud de la solución: ", len(solution))
    # print("--- %s seconds ---" % (time.time() - start_time))

    # # A* bidireccional Heurístico orientaciones_incorrectas
    # print("A* bidireccional Heurístico orientaciones_incorrectas")
    # start_time = time.time()
    # solver = Solvers(scrambled_state_8)
    # solution = solver.iterative_deepening_a_star(Heuristics.orientaciones_incorrectas)
    # print(solution)
    # print("Longitud de la solución: ", len(solution))
    # print("--- %s seconds ---" % (time.time() - start_time))

    # IDA A* Heurístico orientaciones_incorrectas
    print("IDA A* Heurístico orientaciones_incorrectas")
    start_time = time.time()
    solver = Solvers(scrambled_state_8)
    solution = solver.iterative_deepening_A_star(Heuristics.orientaciones_incorrectas)
    print(solution)
    print("Longitud de la solución: ", len(solution))
    print("--- %s seconds ---" % (time.time() - start_time))



if __name__ == "__main__":
    main()