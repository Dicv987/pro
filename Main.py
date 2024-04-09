from rubik import Rubik
from BFS_Solvers import BFS_Solver
from Heuristics import Heuristics
import time  # Importa la librería de tiempo
import copy

def main():
    print("Resolviendo cubo de Rubik...")
    rubik = Rubik()
    rubik.scrambles(4)

    scrambled_state_1 = copy.deepcopy(rubik)
    scrambled_state_2 = copy.deepcopy(rubik)
    scrambled_state_3 = copy.deepcopy(rubik)
    scrambled_state_4 = copy.deepcopy(rubik)
    scrambled_state_5 = copy.deepcopy(rubik)


    # Inicia el cronómetro
    start_time = time.time()

    # Ejecuta el algoritmo BFS
    solver = BFS_Solver(scrambled_state_1)
    solution = solver.bfs(Heuristics.no_heuristic)

    # Detiene el cronómetro
    end_time = time.time()

    print("Solución sin heurística:")
    print(solution)
    print("Longitud de la solución:", len(solution))
    print("Tiempo de ejecución: {:.2f} segundos".format(end_time - start_time))

    # Inicia el cronómetro
    start_time = time.time()

    # Ejecuta el algoritmo BFS con la heurística de colores correctos
    solver = BFS_Solver(scrambled_state_2)
    solution = solver.bfs(Heuristics.colores_correctos)

    # Detiene el cronómetro
    end_time = time.time()

    print("\nSolución con heurística de colores correctos:")
    print(solution)
    print("Longitud de la solución:", len(solution))
    print("Tiempo de ejecución: {:.2f} segundos".format(end_time - start_time))

    # Inicia el cronómetro
    start_time = time.time()

    # Ejecuta el algoritmo BFS con la heurística de piezas descolocadas
    solver = BFS_Solver(scrambled_state_3)
    solution = solver.bfs(Heuristics.piezas_descolocadas)

    # Detiene el cronómetro
    end_time = time.time()

    print("\nSolución con heurística de piezas descolocadas:")
    print(solution)
    print("Longitud de la solución:", len(solution))
    print("Tiempo de ejecución: {:.2f} segundos".format(end_time - start_time))


    # Inicia el cronómetro
    start_time = time.time()

    # Ejecuta el algoritmo BFS con la heurística de posición exacta
    solver = BFS_Solver(scrambled_state_4)
    solution = solver.bfs(Heuristics.exact_position_heuristic)

    # Detiene el cronómetro
    end_time = time.time()

    print("\nSolución con heurística de posición exacta:")
    print(solution)
    print("Longitud de la solución:", len(solution))
    print("Tiempo de ejecución: {:.2f} segundos".format(end_time - start_time))


    #Inicia el cronómetro
    start_time = time.time()

    # Ejecuta el algoritmo A* con la heurística de colores correctos
    solver = BFS_Solver(scrambled_state_5) 
    solution = solver.a_star()

    # Detiene el cronómetro
    end_time = time.time()

    print("\nSolución con A estrella:")
    print(solution)
    print("Longitud de la solución:", len(solution))
    print("Tiempo de ejecución: {:.2f} segundos".format(end_time - start_time))

if __name__ == "__main__":
    main()