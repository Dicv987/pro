from rubik import Rubik
from BFS_Solvers import Solvers
from Heuristics import Heuristics
import time  # Importa la librería de tiempo
import copy

def main():
    print("Resolviendo cubo de Rubik...")
    rubik = Rubik()
    rubik.scrambles(3)

    scrambled_state_1 = copy.deepcopy(rubik)
    scrambled_state_2 = copy.deepcopy(rubik)
    scrambled_state_3 = copy.deepcopy(rubik)
    scrambled_state_4 = copy.deepcopy(rubik)
    scrambled_state_5 = copy.deepcopy(rubik)

    # Inicia el cronómetro
    start_time = time.time()

    # Ejecuta el algoritmo BFS (Breath First Search)
    solver = Solvers(scrambled_state_1)
    solution = solver.bfs()

    # Detiene el cronómetro
    end_time = time.time()

    print("\nSolución con BFS:")
    print(solution)
    print("Longitud de la solución:", len(solution))
    print("Tiempo de ejecución: {:.2f} segundos".format(end_time - start_time))


    #Inicia el cronómetro
    start_time = time.time()

    # Ejecuta el algoritmo A* con la heurística de colores correctos
    solver = Solvers(scrambled_state_2) 
    solution = solver.a_star()

    # Detiene el cronómetro
    end_time = time.time()

    print("\nSolución con A estrella:")
    print(solution)
    print("Longitud de la solución:", len(solution))
    print("Tiempo de ejecución: {:.2f} segundos".format(end_time - start_time))

    # Inicia el cronómetro
    start_time = time.time()

    # Ejecuta el algoritmo BFS con la heurística de colores correctos
    solver = Solvers(scrambled_state_3)
    solution = solver.best_first_search(heuristic_function=Heuristics.exact_position_heuristic)

    # Detiene el cronómetro
    end_time = time.time()

    print("\nSolución con BFS y heurística de colores correctos:")
    print(solution)
    print("Longitud de la solución:", len(solution))
    print("Tiempo de ejecución: {:.2f} segundos".format(end_time - start_time))


if __name__ == "__main__":
    main()