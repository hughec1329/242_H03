import numpy as np
import scipy.misc.pilutil as smp
data = np.zeros( (1024,1024,3))
data[3,] = [255,0,0]
img = smp.toimage( data )
img.show()
def draw(n,l):
	dat = np.zeros( (n,n,3))
	dat[l,] = [255,0,0]
	img = smp.toimage( dat )
	img.show()

posx = np.repeat(np.linspace(1,n,n),n)
posy = np.tile(np.linspace(1,n,n),n)
poss = np.vstack((posx,posy))
poscar = np.arange(n*n)
np.random.shuffle(poscar)
ncars = np.round(n*n*p)
cars = poss[:,poscar[0:ncars]]
cols = np.repeat(np.arange(1,3),ncars/2)
carrs = np.vstack((cars,cols))

cars = np.random.randint(0,n*n,size = ncars)

pos = np.matrix(poss).transpose()
