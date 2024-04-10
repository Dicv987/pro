import matplotlib.pyplot as plt
import random
import copy

class Rubik:
    # Inicialización del cubo
    def __init__(self):
        self.faces = {
            'U': [['W' for _ in range(3)] for _ in range(3)],
            'D': [['Y' for _ in range(3)] for _ in range(3)],
            'L': [['O' for _ in range(3)] for _ in range(3)],
            'R': [['R' for _ in range(3)] for _ in range(3)],
            'F': [['G' for _ in range(3)] for _ in range(3)],
            'B': [['B' for _ in range(3)] for _ in range(3)]
        }

        self.faces_solved = copy.deepcopy(self.faces)

    # Rotación de una cara
    def rotate_face(self, face, clockwise=True):
        if clockwise:
            self.faces[face] = [list(row) for row in zip(*self.faces[face][::-1])]
        else:
            self.faces[face] = [list(row) for row in zip(*self.faces[face])][::-1]

    # Movimientos de Rubik
    def move_U(self, clockwise=True):
        self.rotate_face('U', clockwise)
        if clockwise:
            temp = self.faces['F'][0][:]    # Copia de la primera fila de la cara frontal
            self.faces['F'][0] = self.faces['R'][0]
            self.faces['R'][0] = self.faces['B'][0]
            self.faces['B'][0] = self.faces['L'][0]
            self.faces['L'][0] = temp
        else:
            temp = self.faces['F'][0][:]
            self.faces['F'][0] = self.faces['L'][0]
            self.faces['L'][0] = self.faces['B'][0]
            self.faces['B'][0] = self.faces['R'][0]
            self.faces['R'][0] = temp
        return self.faces
    
    def move_D(self, clockwise=True):
        self.rotate_face('D', clockwise)
        if clockwise:
            temp = self.faces['F'][2][:]
            self.faces['F'][2] = self.faces['L'][2]
            self.faces['L'][2] = self.faces['B'][2]
            self.faces['B'][2] = self.faces['R'][2]
            self.faces['R'][2] = temp
        else:
            temp = self.faces['F'][2][:]
            self.faces['F'][2] = self.faces['R'][2]
            self.faces['R'][2] = self.faces['B'][2]
            self.faces['B'][2] = self.faces['L'][2]
            self.faces['L'][2] = temp
        return self.faces


    def move_F(self, clockwise=True):
        self.rotate_face('F', clockwise)
        if clockwise:
            temp = self.faces['U'][2][:]
            self.faces['U'][2] = [row[2] for row in self.faces['L'][::-1]]
            
            for i in range(3):
                self.faces['L'][i][2] = self.faces['D'][0][i]
            
            self.faces['D'][0] = [row[0] for row in self.faces['R'][::-1]]

            for i in range(3):
                self.faces['R'][i][0] = temp[i]  
        else:
            temp = self.faces['U'][2][:] 
            self.faces['U'][2] = [row[0] for row in self.faces['R']]

            for i in range(3):
                self.faces['R'][i][0] = self.faces['D'][0][2 - i]
            
            self.faces['D'][0] = [row[2] for row in self.faces['L']]
            for i in range(3):
                self.faces['L'][i][2] = temp[2 - i]  

    
    def move_B(self, clockwise=True):
        self.rotate_face('B', clockwise)
        if clockwise:
            temp = self.faces['U'][0][:]  # Guarda la primera fila de U
            self.faces['U'][0] = [row[2] for row in self.faces['R']]
            
            for i in range(3):
                self.faces['R'][i][2] = self.faces['D'][2][2 - i]
            
            self.faces['D'][2] = [row[0] for row in self.faces['L']]
            for i in range(3):
                self.faces['L'][i][0] = temp[2 - i]  
        else:
            temp = self.faces['U'][0][:]  # Guarda la primera fila de U
            self.faces['U'][0] = [row[0] for row in self.faces['L'][::-1]]

            for i in range(3):
                self.faces['L'][i][0] = self.faces['D'][2][i]
            
            self.faces['D'][2] = [row[2] for row in self.faces['R'][::-1]]  # La primera columna de R se convierte en la fila inferior de D

            for i in range(3):
                self.faces['R'][i][2] = temp[i]  # La primera fila de U (guardada en temp) se convierte en la primera columna de R
        return self.faces

    def move_L(self, clockwise=True):
        self.rotate_face('L', clockwise)
        if clockwise:
            temp = [row[0] for row in self.faces['U']]  # Guarda la primera columna de U
            for i in range(3):
                self.faces['U'][i][0] = self.faces['B'][2-i][2]
            
            for i in range(3):
                self.faces['B'][i][2] = self.faces['D'][i][0]

            for i in range(3):
                self.faces['D'][i][0] = self.faces['F'][i][0]
                        
            for i in range(3):
                self.faces['F'][i][0] = temp[i]
            
        else:
            temp = [row[0] for row in self.faces['U']]
            for i in range(3):
                self.faces['U'][i][0] = self.faces['F'][i][0]
            
            for i in range(3):
                self.faces['F'][i][0] = self.faces['D'][i][0]
            
            for i in range(3):
                self.faces['D'][i][0] = self.faces['B'][2-i][2]

            for i in range(3):
                self.faces['B'][i][2] = temp[2 - i]

        return self.faces

    def move_R(self, clockwise=True):
        self.rotate_face('R', clockwise)
        if clockwise:
            temp = [row[2] for row in self.faces['U']]
            for i in range(3):
                self.faces['U'][i][2] = self.faces['F'][i][2]
            
            for i in range(3):
                self.faces['F'][i][2] = self.faces['D'][i][2]
            
            for i in range(3):
                self.faces['D'][i][2] = self.faces['B'][2 - i][0]
            
            for i in range(3):
                self.faces['B'][i][0] = temp[2 - i]
        else:
            temp = [row[2] for row in self.faces['U']]
            for i in range(3):
                self.faces['U'][i][2] = self.faces['B'][2 - i][0]
            
            for i in range(3):
                self.faces['B'][i][0] = self.faces['D'][2 - i][2]
            
            for i in range(3):
                self.faces['D'][i][2] = self.faces['F'][i][2]
            
            for i in range(3):
                self.faces['F'][i][2] = temp[i]
        return self.faces

    
    # Funciones para mostrar el cubo
    def display(self,faces):
            color_map = {'W': 'white', 'Y': 'yellow', 'O': 'orange', 'R': 'red', 'G': 'green', 'B': 'blue'}
            face_order = ['U', 'L', 'F', 'R', 'B', 'D']
            fig, axs = plt.subplots(3, 4, figsize=(4, 3))  # Ajusta el tamaño aquí

            for ax in axs.flatten():
                ax.axis('off')

            positions = {
                'U': (0, 1),
                'L': (1, 0),
                'F': (1, 1),
                'R': (1, 2),
                'B': (1, 3),
                'D': (2, 1)
            }

            for face in face_order:
                row, col = positions[face]
                ax = axs[row, col]
                ax.clear()
                ax.axis('on')
                for i in range(3):
                    for j in range(3):
                        ax.fill_between([j, j+1], [3-i-1, 3-i-1], [3-i, 3-i], color=color_map[faces[face][i][j]])
                ax.set_xlim(0, 3)
                ax.set_ylim(0, 3)
                ax.set_xticks([])
                ax.set_yticks([])
                ax.set_title(face)

            plt.tight_layout()
            plt.show()

    def display_text(self):
        for face in self.faces:
            print(face)
            for row in self.faces[face]:
                print(row)
            print()

    def scrambles(self, n):
        moves = [self.move_U, self.move_R, self.move_F, self.move_L, self.move_D, self.move_B]
        last_move = None
        last_clockwise = None

        for _ in range(n):
            # Seleccionar un movimiento que no sea el inverso del último movimiento
            move = random.choice(moves)
            clockwise = random.choice([True, False])

            # Asegurarse de que el movimiento actual no sea el inverso del anterior
            while move == last_move and clockwise == (not last_clockwise):
                move = random.choice(moves)
                clockwise = random.choice([True, False])

            # Imprimir y ejecutar el movimiento
            print(f"{move.__name__} ({'CW' if clockwise else 'CCW'})")
            move(clockwise)

            # Guardar este movimiento como el último realizado
            last_move = move
            last_clockwise = clockwise
