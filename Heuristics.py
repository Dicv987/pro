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


    @staticmethod
    def pattern_matching(rubik_cube):
        score = 0
        correct_faces = {
            'U': 'W',
            'D': 'Y',
            'L': 'O',
            'R': 'R',
            'F': 'G',
            'B': 'B'
        }

        # Comprobación de centros alineados
        for face, color in correct_faces.items():
            if rubik_cube[face][1][1] == color:
                score += 1  # Aumenta el puntaje por cada centro alineado

        # Comprobar si la esquina superior izquierda de la cara frontal está en su lugar correcto
        if rubik_cube['F'][0][0] == 'G' and rubik_cube['L'][0][2] == 'O' and rubik_cube['U'][2][0] == 'W':
            score += 1
        
        # Comprobar si la esquina superior derecha de la cara frontal está en su lugar correcto
        if rubik_cube['F'][0][2] == 'G' and rubik_cube['R'][0][0] == 'R' and rubik_cube['U'][2][2] == 'W':
            score += 1
        
        # Comprobar si la esquina inferior izquierda de la cara frontal está en su lugar correcto
        if rubik_cube['F'][2][0] == 'G' and rubik_cube['L'][2][2] == 'O' and rubik_cube['D'][0][0] == 'Y':
            score += 1

        # Comprobar si la esquina inferior derecha de la cara frontal está en su lugar correcto
        if rubik_cube['F'][2][2] == 'G' and rubik_cube['R'][2][0] == 'R' and rubik_cube['D'][0][2] == 'Y':
            score += 1

        # Comprobar si la esquina superior izquierda de la cara trasera está en su lugar correcto
        if rubik_cube['B'][0][0] == 'B' and rubik_cube['R'][0][2] == 'R' and rubik_cube['U'][0][2] == 'W':
            score += 1
        
        # Comprobar si la esquina superior derecha de la cara trasera está en su lugar correcto
        if rubik_cube['B'][0][2] == 'B' and rubik_cube['L'][0][0] == 'O' and rubik_cube['U'][0][0] == 'W':
            score += 1

        # Comprobar si la esquina inferior izquierda de la cara trasera está en su lugar correcto
        if rubik_cube['B'][2][0] == 'B' and rubik_cube['R'][2][2] == 'R' and rubik_cube['D'][2][2] == 'Y':
            score += 1

        # Comprobar si la esquina inferior derecha de la cara trasera está en su lugar correcto
        if rubik_cube['B'][2][2] == 'B' and rubik_cube['L'][2][0] == 'O' and rubik_cube['D'][2][0] == 'Y':
            score += 1

        return -score
    
    @staticmethod
    def orientaciones_incorrectas(faces):
            incorrect_orientations = 0
        
            # Supongamos que la cara frontal (F) y la cara trasera (B) tienen 
            # una orientación especial que queremos verificar.
            for i in range(3):
                for j in range(3):
                    # Verificar la orientación correcta en la cara frontal, suponiendo
                    # que la orientación correcta de los adhesivos horizontales es
                    # igual al adhesivo central horizontalmente.
                    if j != 1 and faces['F'][i][j] != faces['F'][i][1]:
                        incorrect_orientations += 1

                    # Verificar la orientación correcta en la cara trasera, suponiendo
                    # que la orientación correcta de los adhesivos verticales es
                    # igual al adhesivo central verticalmente.
                    if i != 1 and faces['B'][i][j] != faces['B'][1][j]:
                        incorrect_orientations += 1
                    
            # Asumiendo que las caras laterales también tienen una orientación
            # vertical y horizontal que queremos verificar.
            for face in ['L', 'R', 'U', 'D']:
                for i in range(3):
                    if faces[face][i][0] != faces[face][1][0]:
                        incorrect_orientations += 1
                    if faces[face][i][2] != faces[face][1][2]:
                        incorrect_orientations += 1

            return incorrect_orientations

