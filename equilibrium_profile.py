# This script recreates figures 4 in Moelans et al. Phys Rev. B 78, 024113 (2008),
# which represents the equilibrium profiles of the phase field variables.
# TODO: Moelans says that she had to do a numerical integration to calculate
# the profiles for different values of gamma.  Only for gamma = 1.5 will you get
# what is currently displayed.

from __future__ import division
from math import tanh, sqrt
from matplotlib.pyplot import plot, xlim, ylim, xlabel, ylabel, title, legend, show
from numpy import arange

def calcEtai(x, m = 1, kappa = 2):
    return float(1 / 2 * (1 - tanh(sqrt(m / (2 * kappa)) * x)))

def calcEtaj(x, m = 1, kappa = 2):
    return float(1 / 2 * (1 + tanh(sqrt(m / (2 * kappa)) * x)))

gamma = [1, 1.5, 2, 4]
eta_i = []
eta_j = []
distance = []
etai_plus_etaj = []
etas = []
distances = []

for x in arange(-10, 10, 0.01):
    distance.append(float(x))
    eta_i.append(calcEtai(x))
    eta_j.append(calcEtaj(x))

#for i in range(0, len(eta_i)):
#    etai_plus_etaj.append(eta_i[i] + eta_j[i])

plot(distance, eta_i, 'r-', label=r'$\eta_i$')
plot(distance, eta_j, 'b-', label=r'$\eta_j$') # TODO: figure out how to label two lines as the same entry
legend()
show()
