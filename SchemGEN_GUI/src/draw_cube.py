import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def draw_cube(ax, origin, size=1):
    # Define the vertices of a unit cube
    vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
                         [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])
    
    # Scale and translate the vertices to the correct size and position
    vertices = vertices * size + origin
    
    # Define the faces of the cube by connecting vertices
    faces = [[vertices[0], vertices[1], vertices[2], vertices[3]],  # Bottom
             [vertices[4], vertices[5], vertices[6], vertices[7]],  # Top
             [vertices[0], vertices[1], vertices[5], vertices[4]],  # Front
             [vertices[2], vertices[3], vertices[7], vertices[6]],  # Back
             [vertices[1], vertices[2], vertices[6], vertices[5]],  # Right
             [vertices[0], vertices[3], vertices[7], vertices[4]]]  # Left
    
    # Create a 3D polygon for each face
    poly3d = [faces]
    ax.add_collection3d(Poly3DCollection(poly3d, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
    
# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Draw a cube
draw_cube(ax, origin=[0, 0, 0], size=1)

# Set the axes limits so all sides of the cube are visible
ax.set_xlim([0, 2])
ax.set_ylim([0, 2])
ax.set_zlim([0, 2])

plt.show()