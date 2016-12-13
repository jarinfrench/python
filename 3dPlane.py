from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, proj3d
from matplotlib.patches import FancyArrowPatch
from sys import argv

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)
# Takes as a command-line argument a point and... stuff

point = np.array([1,0,0])
normal = np.array([0,1,0])

d = -point.dot(normal)

xx,yy = np.meshgrid(range(10), range(10))

z = (-normal[0]*xx - normal[1] * yy - d) * 1. / normal[2]

plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx,yy,z)
normal_vec = Arrow3D([0,normal[0]],[0,10*normal[1]],[0,normal[2]], mutation_scale=20, lw=1, arrowstyle="-|>", color='k')
plt3d.add_artist(normal_vec)
plt.axis([-5,5,-5,5])
plt.show()
