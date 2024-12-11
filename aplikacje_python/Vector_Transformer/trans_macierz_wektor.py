import matplotlib.pyplot as plt
import numpy as np


def read_matrix_vector_angle():

    matrix = []
    vector = []
    section = None

    with open("data.csv", "r") as file:

        for line in file: 

            line = line.strip()

            if not line:
                section = None
                continue

            elif "Matrix" in line:
                section = "Matrix"
                continue
            
            elif "Vector" in line:
                section = "Vector"
                continue
            
            elif "Angle" in line:
                section = "Angle"
                continue

            if section == "Matrix":
                matrix.append(list(map(float, line.split())))

            elif section == "Vector":
                vector.extend(map(float, line.split()))

            elif section == "Angle":
                angle = float(line)


    return np.array(matrix), np.array(vector), angle


def rotation_matrix(angle):

    angle_rad = np.radians(angle)
    
    return np.array([
        [np.cos(angle_rad), -np.sin(angle_rad)],
        [np.sin(angle_rad), np.cos(angle_rad)]
    ])


def plot_vectors(vector, transformed_vector):

    origin = np.array([0, 0])
 
    plt.quiver(*origin, *vector, color='blue', angles='xy', scale_units='xy', scale=1, label='Original Vector')
    plt.quiver(*origin, *transformed_vector, color='red', angles='xy', scale_units='xy', scale=1, label='Transformed Vector')

    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Vector Transformation")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


matrix, vector, angle = read_matrix_vector_angle()
rotation = rotation_matrix(angle)
transformed_vector = transformed_vector = matrix @ rotation @ vector
plot_vectors(vector, transformed_vector)


