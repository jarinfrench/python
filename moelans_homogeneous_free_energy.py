# This program creates an animation that steps through various gamma values and
# plots the resultant free energy landscape.  The saddle point is identified with
# a white data point and label.  This recreates figures 2 in Moelans et al. Phys
# Rev. B 78, 024113 (2008)

from __future__ import division
from sys import argv
from matplotlib.pyplot import contourf, show, subplots, figure, axes, xlim, ylim, xlabel, ylabel, colorbar, title, plot, annotate
from matplotlib.animation import FuncAnimation
from matplotlib import cm
from math import sqrt
from numpy import meshgrid, array, linalg

if len(argv) == 1: # Don't save the animation by default
    saveMovie = False
else:
    if "--save" in argv or "-s" in argv:
        saveMovie = True
        # TODO: Maybe look into defining how many contour lines will be shown via command line
    else:
        print("Warning: Unrecognized command line option. Animation not being saved.")
        saveMovie = False

fig = figure()
ax = axes(xlim=(0,1), ylim=(0,1))
gamma = [i / 20.0 for i in range(81)]
eta_saddle = [1.0 / sqrt(2.0 * gamma[i] + 1.0) for i in range(81)]
eta_i = [i / 100.0 for i in range(101)]
eta_j = [i / 100.0 for i in range(101)]

eta_i, eta_j = meshgrid(eta_i, eta_j)

# This function returns a contour plot with the saddle point identified.
def animate(k):
    fig.clear() # clear the figure so we don't have a plot that consists of colorbars
    # This is how the free energy is calculated according to Moelans et al.
    free_energy = array((eta_i**4.0 / 4.0) - (eta_i**2.0 / 2.0) + (eta_j**4.0 / 4.0) - (eta_j**2.0 / 2.0) + (gamma[k] * eta_i**2.0 * eta_j**2.0) + 0.25)
    #free_energy = free_energy / linalg.norm(free_energy)
    cont = contourf(eta_i, eta_j, free_energy, [0.05, 0.1, 0.125, 0.15, 0.2, 0.25], cmap = cm.jet, extend = 'both')
    plot(eta_saddle[k], eta_saddle[k],'wx') # Saddle point plot command - plotted as a white cross ('wx')
    # This next line creates the annotation that identifies where the saddle point is.
    xlabel(r'$\eta_i$')
    ylabel(r'$\eta_j$')
    annotate("(%2.2f, %2.2f)" %(eta_saddle[k], eta_saddle[k]), xy=(eta_saddle[k], eta_saddle[k]), xytext=(eta_saddle[k] - 0.1, eta_saddle[k]+.05), color='white')
    title(r"Free energy with $\gamma_{i,j}$ = %2.2f. $\eta_{saddle}$ = %2.4f" %(gamma[k], eta_saddle[k]))
    colorbar() # useful for scaling
    return cont

ani = FuncAnimation(fig, animate, frames = len(gamma), interval=1000)
if saveMovie:
    ani.save('homogeneous_free_energy_landscape.mp4')
show()
