import numpy as np
import scipy.misc.pilutil as smp
data = np.zeros( (1024,1024,3))
data[3,] = [255,0,0]
img = smp.toimage( data )
img.show()
def draw(p,n):
	posx = np.repeat(np.arange(n,dtype=int),n) 	# possible x
	posy = np.tile(np.arange(n,dtype=int),n)
	poss = np.vstack((posx,posy))
	poscar = np.arange(n*n)                 # index of cats
	np.random.shuffle(poscar)               # randomise (Wasnt working on 2dim)
	ncars = np.round(n*n*p)
	carrs = poss[:,poscar[0:ncars]]         # choose random cars
	cols = np.repeat(np.arange(1,3),ncars/2)
	cars = np.vstack((carrs,cols))          # colorize
	
	dat = np.zeros( (n,n,3))
	redcar = cars[:,cars[2,] == 1]
	bluecar = cars[:,cars[2,] == 2]
	dat[redcar[0,:],redcar[1:],] = [255,0,0]
	dat[bluecar[0,:],bluecar[1:],] = [0,0,255]

	img = smp.toimage( dat )
	img.show()



