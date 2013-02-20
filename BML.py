import numpy as np
import scipy.misc.pilutil as smp
data = np.zeros( (1024,1024,3))
data[3,] = [255,0,0]
img = smp.toimage( data )
img.show()
def car(p,n):
	posx = np.repeat(np.arange(n,dtype=int),n) 	# possible x
	posy = np.tile(np.arange(n,dtype=int),n)
	poss = np.vstack((posx,posy))
	poscar = np.arange(n*n)                 # index of cats
	np.random.shuffle(poscar)               # randomise (Wasnt working on 2dim)
	ncars = np.round(n*n*p)
	carrs = poss[:,poscar[0:ncars]]         # choose random cars
	cols = np.repeat(np.arange(1,3),ncars/2)
	cars = np.vstack((carrs,cols))          # colorize
	return cars

def move(cars):
	redcar = cars[:,cars[2,] == 1]
	bluecar = cars[:,cars[2,] == 2]
	carsnew = cars
	#move cars
	carsnew[0,:] = carsnew[0,:] + 1
	# check and thow to start if off edge.
	off = carsnew[0,:] > n
	carsnew[0,off] = 0

	old = ''
	for i in range(len(cars[1,:])):
	    old += str(cars[:,i])	# build string of old positions.
	block = np.repeat(bool(),len(cars[0,:]))
	for i in range(len(cars[1,:])):
	    block[i] =  str(carsnew[:,i]) in y	# compare old and new, any conflict marked true.

	return block


for i in range(len(t[1,:])):
	    y += str(t[:,i])	# build string of old positions.

for i in range(len(t[1,:])):
	    print str(tnew[:,i]) in y	# compare old and new, any conflict marked true.



#	for i range(o,t):
#		if t%2==0:	#move red across

#		else:


		


def draw(cars,n):
	dat = np.zeros( (n,n,3))
	redcar = cars[:,cars[2,] == 1]
	bluecar = cars[:,cars[2,] == 2]
	dat[redcar[0,:],redcar[1:],] = [255,0,0]
	dat[bluecar[0,:],bluecar[1:],] = [0,0,255]
	img = smp.toimage( dat )
	img.show()



