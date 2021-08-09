# To do
# - add command line flags, for data input and flags for what sort of solve, also add help flag
# - error handling, check statically determinant and files correct format
# - write a solver for beams and frames
# - enclose parts of this script into functions
# - write a visualisations function using tikz
# - can add calculation for stress in members if material data is given

# Loading Libraries
import numpy as np
import pandas as pd
import sys

# Taking Command Line Flags
for i in range(0,len(sys.argv)):
    if sys.argv[i] == "-h":
        print("The arguments should be; nodes elements reactions external \nCheck the documentation for format")
        quit()

# Loading Data
nodes = np.array(pd.read_csv(sys.argv[1]))
elements = np.array(pd.read_csv(sys.argv[2]))
reactions = np.array(pd.read_csv(sys.argv[3]))
external = np.array(pd.read_csv(sys.argv[4]))

# Calculating
geometryMatrix = np.zeros((len(nodes) * 2, len(nodes) * 2))

for i in range(0, len(elements)):
    member = elements[i, 0]
    nodeFrom = elements[i, 1]
    nodeTo = elements[i, 2]

    dx = nodes[nodeTo - 1, 1] - nodes[nodeFrom - 1, 1]
    dy = nodes[nodeTo - 1, 2] - nodes[nodeFrom - 1, 2]
    dis = np.sqrt(dx ** 2 + dy ** 2)

    geometryMatrix[(2 * nodeFrom - 1) - 1, member - 1] = dx / dis
    geometryMatrix[(2 * nodeTo - 1) - 1, member - 1] = -dx / dis
    geometryMatrix[(2 * nodeFrom) - 1, member - 1] = dy / dis
    geometryMatrix[(2 * nodeTo) - 1, member - 1] = -dy / dis

for i in range(0, len(reactions)):
    reaction = reactions[i, 0]
    node = reactions[i, 1]
    direction = reactions[i, 2]

    if direction == 'y' or direction == 'Y':
        geometryMatrix[(2 * node) - 1, (len(elements) + reaction) - 1] = geometryMatrix[(2 * node) - 1, (
                    len(elements) + reaction) - 1] + 1

    elif direction == 'x' or direction == 'X':
        geometryMatrix[(2 * node - 1) - 1, (len(elements) + reaction) - 1] = geometryMatrix[(2 * node - 1) - 1, (
                    len(elements) + reaction) - 1] + 1

externalForces = np.zeros((len(nodes) * 2, 1))

for i in range(0, len(external)):
    node = external[i, 0]
    force = external[i, 1]
    direction = external[i, 2]

    externalForces[(2 * node - 1) - 1] = -force * np.cos(direction * np.pi / 180)
    externalForces[(2 * node) - 1] = -force * np.sin(direction * np.pi / 180)

results = np.dot(np.linalg.pinv(geometryMatrix), externalForces)

# Printing
for i in range(0, len(elements)):
    print("The force in member %d is %5.2f kN" % (i + 1, results[i]))

for i in range(0, len(reactions)):
    print("The reaction at %d in the %s direction is %5.2f" % (
    reactions[i, 1], reactions[i, 2], results[(len(results) - 3) + i]))
