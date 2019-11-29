import numpy as np

Nvec = np.array([0,0,0,0,0,100]) #100 EDs no SF12 
def exploraAT(Nvec):
	SFset = np.array([7,8,9,10,11,12])
	w = np.array([1,1.83,3.33,6.67,13.34,24.04])
	q = np.power(w,-1)
	P = Nvec * w
	old_P = 0
	p = 1
	while old_P!=p:
		old_P = 12 - 7
		P[12-7] = 