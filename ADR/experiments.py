def exp0():
	self.sf = 12
	self.cr = 4
	self.bw = 125
	Lpl = Lpld0 + 10*gamma*math.log10(distance/d0)
	Prx = Ptx - GL - Lpl

	# SF vector to know how many devices are in especific SF
    global sfVector
    sfVector[int(self.sf)-6] += 1
    # transmission range, needs update XXX
    # self.transRange = 150
    self.pl = plen
    self.symTime = (2.0**self.sf)/self.bw
    self.arriveTime = 0
    self.rssi = Prx
    # frequencies: lower bound + number of 61 Hz steps
    self.freq = 860000000 + random.randint(0,2622950)
    self.freq = 860000000

    # for certain experiments override these and
    # choose some random frequences
    self.rectime = airtime(self.sf,self.cr,self.pl,self.bw)
    # denote if packet is collided
    self.collided = 0
    self.processed = 0
    # mark the packet as lost when it's rssi is below the sensitivity
    # don't do this for experiment 3, as it requires a bit more work
    global minsensi
    self.lost = self.rssi < minsensi
    print "node {} bs {} lost {}".format(self.nodeid, self.bs, self.lost)

def exp1():
	self.sf = 12
	self.cr = 4
	self.bw = 125
	# log-shadow
    Lpl = Lpld0 + 10*gamma*math.log10(distance/d0)
    Prx = Ptx - GL - Lpl
    # SF vector to know how many devices are in especific SF
    global sfVector
    sfVector[int(self.sf)-6] += 1

    # transmission range, needs update XXX
    # self.transRange = 150
    self.pl = plen
    self.symTime = (2.0**self.sf)/self.bw
    self.arriveTime = 0
    self.rssi = Prx
    # frequencies: lower bound + number of 61 Hz steps
    self.freq = 860000000 + random.randint(0,2622950)
    self.freq = 860000000

    # for certain experiments override these and
    # choose some random frequences
    self.freq = random.choice([860000000, 864000000, 868000000])
    self.rectime = airtime(self.sf,self.cr,self.pl,self.bw)
    # denote if packet is collided
    self.collided = 0
    self.processed = 0
    # mark the packet as lost when it's rssi is below the sensitivity
    # don't do this for experiment 3, as it requires a bit more work
    global minsensi
    self.lost = self.rssi < minsensi
    print "node {} bs {} lost {}".format(self.nodeid, self.bs, self.lost)

def exp2():    
	self.sf = 6
	self.cr = 1
    self.bw = 500
    # log-shadow
    Lpl = Lpld0 + 10*gamma*math.log10(distance/d0)
    Prx = Ptx - GL - Lpl
    # SF vector to know how many devices are in especific SF
    global sfVector
    sfVector[int(self.sf)-6] += 1

    # transmission range, needs update XXX
    # self.transRange = 150
    self.pl = plen
    self.symTime = (2.0**self.sf)/self.bw
    self.arriveTime = 0
    self.rssi = Prx
    # frequencies: lower bound + number of 61 Hz steps
    self.freq = 860000000 + random.randint(0,2622950)
    self.freq = 860000000

    # for certain experiments override these and
    # choose some random frequences
    self.freq = random.choice([860000000, 864000000, 868000000])
    self.rectime = airtime(self.sf,self.cr,self.pl,self.bw)
    # denote if packet is collided
    self.collided = 0
    self.processed = 0
    # mark the packet as lost when it's rssi is below the sensitivity
    # don't do this for experiment 3, as it requires a bit more work
    global minsensi
    self.lost = self.rssi < minsensi
    print "node {} bs {} lost {}".format(self.nodeid, self.bs, self.lost)

def exp3():    
	minairtime = 9999
	minsf = 0
    minbw = 0
    for i in range(0,6):
        for j in range(1,4):
            if (sensi[i,j] < Prx):
                self.sf = sensi[i,0]
                if j==1:
                    self.bw = 125
                elif j==2:
                    self.bw = 250
                else:
                    self.bw=500
                at = airtime(self.sf,4,20,self.bw)
                if at < minairtime:
                    minairtime = at
                    minsf = self.sf
                    minbw = self.bw

    self.rectime = minairtime
    self.sf = minsf
    self.bw = minbw
    if (minairtime == 9999):
        print "does not reach base station"
        exit(-1)
    # SF vector to know how many devices are in especific SF
    global sfVector
    sfVector[int(self.sf)-6] += 1

    # transmission range, needs update XXX
    # self.transRange = 150
    self.pl = plen
    self.symTime = (2.0**self.sf)/self.bw
    self.arriveTime = 0
    self.rssi = Prx
    # frequencies: lower bound + number of 61 Hz steps
    self.freq = 860000000 + random.randint(0,2622950)
    self.freq = 860000000

    # for certain experiments override these and
    # choose some random frequences
    self.rectime = airtime(self.sf,self.cr,self.pl,self.bw)
    # denote if packet is collided
    self.collided = 0
    self.processed = 0

def exp4():    
	# log-shadow
    Lpl = Lpld0 + 10*gamma*math.log10(distance/d0)
    Prx = Ptx - GL - Lpl
    # SF vector to know how many devices are in especific SF
    global sfVector
    sfVector[int(self.sf)-6] += 1

    # transmission range, needs update XXX
    # self.transRange = 150
    self.pl = plen
    self.symTime = (2.0**self.sf)/self.bw
    self.arriveTime = 0
    self.rssi = Prx
    # frequencies: lower bound + number of 61 Hz steps
    self.freq = 860000000 + random.randint(0,2622950)

    # for certain experiments override these and
    # choose some random frequences
    self.freq = 860000000
    self.rectime = airtime(self.sf,self.cr,self.pl,self.bw)
    # denote if packet is collided
    self.collided = 0
    self.processed = 0
    # mark the packet as lost when it's rssi is below the sensitivity
    # don't do this for experiment 3, as it requires a bit more work
    global minsensi
    self.lost = self.rssi < minsensi
    print "node {} bs {} lost {}".format(self.nodeid, self.bs, self.lost)

def exp5():    
	# log-shadow
    Lpl = Lpld0 + 10*gamma*math.log10(distance/d0)
    Prx = Ptx - GL - Lpl
    # SF vector to know how many devices are in especific SF
    global sfVector
    sfVector[int(self.sf)-6] += 1

    # transmission range, needs update XXX
    # self.transRange = 150
    self.pl = plen
    self.symTime = (2.0**self.sf)/self.bw
    self.arriveTime = 0
    self.rssi = Prx
    # frequencies: lower bound + number of 61 Hz steps
    self.freq = 860000000 + random.randint(0,2622950)

    # for certain experiments override these and
    # choose some random frequences
    self.freq = 860000000
    self.rectime = airtime(self.sf,self.cr,self.pl,self.bw)
    # denote if packet is collided
    self.collided = 0
    self.processed = 0
    # mark the packet as lost when it's rssi is below the sensitivity
    # don't do this for experiment 3, as it requires a bit more work
    global minsensi
    self.lost = self.rssi < minsensi
    print "node {} bs {} lost {}".format(self.nodeid, self.bs, self.lost)

def exp6():
	global nr
	if self.nodeid!=

