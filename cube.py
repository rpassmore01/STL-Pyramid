import numpy as np
import math
from stl import mesh


def pyramid(numSides):
    # Define the vertices of the pyramid
    vertices = np.array([
        [0, 0, 0],
        [0, 0, 1],
        [1, 0, 0]
    ])

    # Define the triangles that make up the pyramid
    faces = np.empty((0,3),int)

    theta = 360 / numSides

    # Adds all vertices to vertices array
    for i in range(numSides - 1):
        newPoint = [round(math.cos(math.radians(theta)),5), round(math.sin(math.radians(theta)), 5), 0]
        vertices = np.append(vertices, np.array([newPoint]), axis=0)
        theta += 360 / numSides

    for i in range(2):
        for j in range(len(vertices) - 2):
            if j + 3 == numSides + 2:
                faces = np.append(faces, np.array([[i, j + 2 , 2]]), axis=0)
            else:
                faces = np.append(faces, np.array([[i, j + 2, j + 3]]), axis=0)

    print(vertices)

    # Create the mesh
    cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            cube.vectors[i][j] = vertices[f[j], :]

    # Write the mesh to file "cube.stl"
    cube.save(str(numSides) + ' sided_pyramid.stl')


if __name__ == '__main__':
    pyramid(100)
