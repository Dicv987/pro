class Heuristics:
    
    @staticmethod
    def no_heuristic(faces):
        return 0
    
    @staticmethod
    def exact_position_heuristic(faces):
        # Definimos la configuración resuelta del cubo de Rubik para comparar
        correct_faces = {
            'U': [['W' for _ in range(3)] for _ in range(3)],
            'D': [['Y' for _ in range(3)] for _ in range(3)],
            'L': [['O' for _ in range(3)] for _ in range(3)],
            'R': [['R' for _ in range(3)] for _ in range(3)],
            'F': [['G' for _ in range(3)] for _ in range(3)],
            'B': [['B' for _ in range(3)] for _ in range(3)]
        }

        incorrect_positions = 0

        # Recorremos cada cara y cada posición en esa cara
        for face, grid in faces.items():
            for i in range(3):
                for j in range(3):
                    if grid[i][j] != correct_faces[face][i][j]:
                        # Cuenta cada pieza que no está en la posición correcta
                        incorrect_positions += 1

        # La heurística podría ser el número total de posiciones incorrectas
        # Un valor más bajo indica un estado más cercano al resuelto
        return incorrect_positions


