import numpy as np

def count(mat, val):
    cnt = 0
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if mat[i,j]> val:
                cnt += 1
    return cnt

def exploraSF(rssi, sfvector):
    sensi = -133.25
    # self.sfvector = sfvector
    D = len(sfvector) #quantidade de EDs que podem se comunicar(RSSI<sensibility)
    SFset = [7, 8, 9, 10, 11, 12]
    l = len(SFset)
    for i in range(len(SFset)):
        cnt = count(rssi,sensi)
        if cnt > D/l:
            z = D/l
        else:
            z = cnt
        for p in range(z):
            x = np.argwhere(rssi==np.max(rssi))[0][0]
            y = np.argwhere(rssi==np.max(rssi))[0][1]
            sfvector[y] = SFset[i-6]
            rssi[:,y] = -200
            D = D - 1
        l = l - 1
    return sfvector

#Example:
RSSI = np.matrix([[-134.14577591,-131.83360217,-130.89285002,-132.23943237,-136.12312746,-133.84531368,-135.79119379,-132.17132145,-134.57831317,-137.52937992]]) #[[-147, -138, -130],[-120, -150, -122]]) #2GWs e 3EDs
sf = np.ones(RSSI.shape[1])*12

print RSSI
print sf
newsf = exploraSF(RSSI, sf)
print "\n"
print RSSI
print newsf