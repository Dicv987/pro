class Heuristics:

    @staticmethod
    def no_heuristic(faces):
        return 0
    
    @staticmethod
    def colores_correctos(faces):
        # Colores esperados en cada cara
        colores_esperados = {
            'U': 'W',  # Blanco
            'D': 'Y',  # Amarillo
            'L': 'O',  # Naranja
            'R': 'R',  # Rojo
            'F': 'G',  # Verde
            'B': 'B'   # Azul
        }
        
        contador_correctos = 0
        
        # Recorre cada cara y cuenta los colores correctos
        for cara, matriz in faces.items():
            color_esperado = colores_esperados[cara]
            for fila in matriz:
                for color in fila:
                    if color == color_esperado:
                        contador_correctos += 1
                        
        return contador_correctos
    

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
    def piezas_descolocadas(faces):
        # Inicializa el contador de posiciones correctas a 0.
        correct_positions = 0
        
        # Define el color esperado para cada cara del cubo en su estado resuelto.
        correct_faces = {'U': 'W',  # Arriba (Up) debe ser blanco
                         'D': 'Y',  # Abajo (Down) debe ser amarillo
                         'L': 'O',  # Izquierda (Left) debe ser naranja
                         'R': 'R',  # Derecha (Right) debe ser rojo
                         'F': 'G',  # Frente (Front) debe ser verde
                         'B': 'B'}  # Atrás (Back) debe ser azul

        # Recorre cada cara del cubo.
        for face in faces.keys():
            # Obtiene el color correcto para la cara actual basado en el estado resuelto.
            correct_color = correct_faces[face]
            
            # Recorre cada fila de la cara actual.
            for row in faces[face]:
                # Recorre cada pieza (color) en la fila actual.
                for color in row:
                    # Si el color de la pieza actual coincide con el color esperado de la cara,
                    # significa que la pieza está en la cara correcta.
                    if color == correct_color:
                        # Incrementa el contador de posiciones correctas.
                        correct_positions += 1
                        
        # Calcula el número total de piezas descolocadas restando las posiciones correctas
        # del total de piezas en el cubo (54, ya que hay 9 piezas por cada una de las 6 caras).
        # Este valor representa qué tan "lejos" está el cubo de estar completamente resuelto,
        # con un valor menor indicando un estado más cercano al objetivo.
        return 54 - correct_positions
