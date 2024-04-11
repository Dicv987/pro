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

    # print ("A* con heurística exacta")
    # solver = Solvers(scrambled_state_1)
    # start_time = time.time()
    # path = solver.best_first_search(Heuristics.exact_position_heuristic)
    # end_time = time.time()
    # print(f"Tiempo de ejecución: {end_time - start_time} segundos")
    # print(f"Longitud del camino: {len(path)}")

    # print ("A* con heurística de coincidencia de patrones")
    # solver = Solvers(scrambled_state_2)
    # start_time = time.time()
    # path = solver.best_first_search(Heuristics.pattern_matching)
    # end_time = time.time()
    # print(f"Tiempo de ejecución: {end_time - start_time} segundos")
    # print(f"Longitud del camino: {len(path)}")

    print ("A* con heuristica de orientaciones incorrectas")    
    solver = Solvers(scrambled_state_3)
    start_time = time.time()
    path = solver.best_first_search(Heuristics.orientaciones_incorrectas)
    end_time = time.time()
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")
    print(f"Longitud del camino: {len(path)}")

    






if __name__ == "__main__":
    main()