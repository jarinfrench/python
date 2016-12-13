# This program recreates figure 3 in Moelans et al. Phys Rev. B 78, 024113
# (2008), which describes the evolution of the homogeneous free energy along the
# eta_i = eta_j line for various values of gamma.

from __future__ import division
from matplotlib.pyplot import plot, title, xlim, ylim, xlabel, ylabel, show, legend, gca, savefig
from math import sqrt
import matplotlib.ticker as ticker

gamma = [0.7, 1, 1.5, 2, 4]
free_energy = [None] * len(gamma)
eta_saddle = [None] * len(gamma)
f0_saddle = [None] * len(gamma)
etas = []

for i in range(0, 101):
    etas.append(i / 100)

for i in range(0, len(gamma)):
    en = []
    for j in range(0, len(etas)):
        eta = etas[j]
        en.append((eta**4.0 / 4.0) - (eta**2.0 / 2.0) + (eta**4.0 / 4.0) - (eta**2.0 / 2.0) + (gamma[i] * eta**2.0 * eta**2.0) + 1.0 / 4.0)
    free_energy[i] = en
    f0_saddle[i] = (2 * gamma[i] - 1) / (4 * (2 * gamma[i] + 1))
    eta_saddle[i] = 1 / sqrt(2 * gamma[i] + 1)

    # The '$' symbols translate the line into a LaTeX string
    plot(etas, free_energy[i], label=r'$\gamma_{i,j} = %2.1f$'%(gamma[i]))
plot(eta_saddle,f0_saddle,'kx', label='Saddle point')
ax = gca()
ax.set_xlim([0,1])
ax.set_ylim([0,1.5])
ax.set_xlabel(r'$\eta_i = \eta_j$')
ax.set_ylabel(r'$f_0(\eta_i = \eta_j)$')
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5)) # Changes the major tick marks to be every 0.5
legend(loc=0, numpoints = 1) # loc = 2 specifies the upper left of the plot, numpoints specifies the number of points shown in the legend
savefig('free_energy_evolution_equal_eta.eps')
show()
