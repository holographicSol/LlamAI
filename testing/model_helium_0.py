import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

# Define constants
R_H = 0.57  # Bohr radius of Hydrogen (used as a proxy for Helium)
ELEC_CHARGE = -1e-19  # Electron charge in Coulombs
PROTON_MASS = 1.67e-27  # Proton mass in kg
NUM_ATOMS = 4  # Number of electrons around the nucleus

# Define the atom's structure
def create_atom(radius):
    atoms = []
    for i in range(NUM_ATOMS):
        angle = np.pi / NUM_ATOMS * i
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        z = 0.1 * radius  # slight vertical offset to avoid overlap
        atom = {
            'x': [x],
            'y': [y],
            'z': [z],
            'color': '#FF69B4'  # highly saturated pink (He nucleus)
        }
        atoms.append(atom)

    return atoms

# Animation function
def animate(atom):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('black')  # Black background

    for i in range(NUM_ATOMS):
        atom[i]['x'].append(np.cos(i*np.pi/NUM_ATOMS)*R_H*0.9)  # Move the electron around the nucleus
        atom[i]['y'].append(np.sin(i*np.pi/NUM_ATOMS)*R_H*0.9)
        atom[i]['z'].append(0)

    ax.scatter(atom[0]['x'], atom[0]['y'], atom[0]['z'], c=atom[0]['color'])
    for i in range(NUM_ATOMS):
        ax.plot([atom[i]['x'][-1], atom[i]['x'][0]], [atom[i]['y'][-1], atom[i]['y'][0]], [atom[i]['z'][-1], atom[i]['z'][0]], c=atom[i]['color'], zorder=10)

    plt.draw()
    plt.pause(0.01)  # adjust this value to change animation speed
    plt.clf()

# Create and animate the Helium atom
atom = create_atom(R_H)
for _ in range(200):  # Run for 10 seconds (at 60 FPS)
    animate(atom)