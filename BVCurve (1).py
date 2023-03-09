import numpy as np
import matplotlib.pyplot as plt

infile = 'AtanasijevicDatabase.txt'

longitude = np.genfromtxt(infile,skip_header=11, skip_footer=1, delimiter=(12,5), usecols=1)
latitude = np.genfromtxt(infile, skip_header=11, skip_footer=1, delimiter=(15,6), usecols=1)
bv = np.genfromtxt(infile, skip_header=11, skip_footer=1, delimiter=(25,3), usecols=1)

print('--------------B-V CURVE START---------------')
print(bv)
print('--------------B-V CURVE END---------------')

for i in range(len(longitude)) :
    if longitude[i] >180:
        longitude[i] = longitude[i] - 360

print('-----------LATITUDE START------------')
print(latitude[:])
print('-----------LATITUDE END------------')


###          LATITUDE STARTS HERE        ###
x2 = longitude[:]
y2 = latitude[:]
freqlat = np.histogram(longitude, bins=36, range=(-90,90))
yy=freqlat[0]
xlim=freqlat[1]
print('XLIM = ',xlim)
xwidth = 10
xmid=np.zeros(len(xlim)-1)

for i in range(len(xlim)-1) :
    xmid[i]=xlim[i]+(0.5*xwidth)
print('XMID = ',xmid)

#       Latitude Plot

print('lengths=',len(xmid),len(yy))
plt.bar(xmid,yy,4,)
plt.xlabel('Longitude')
plt.ylabel('Frequency')
plt.savefig('LongitudeBins.pdf')
plt.show()


### LONGITUDE STARTS HERE ###

freqlong = np.histogram(latitude, bins=36, range=(-180,180))
yy2=freqlong[0]
xlim2=freqlong[1]
print('XLIM 2 = ', xlim2)
xwidth2 = 10
xmid2=np.zeros(len(xlim2)-1)

for i in range(len(xlim2)-1) :
    xmid2[i]=xlim2[i]+(0.5*xwidth2)

print('lengths=',len(xmid2),len(yy2))

#       Longtitude Plot

plt.bar(xmid2,yy2,8)
plt.xlabel('Latititude')
plt.ylabel('Frequency')
plt.savefig('LatitudeBins.pdf')
plt.show()

#       B-V Plot
x3 = 1/(np.sin(np.absolute(latitude)))
y3 = np.absolute(bv)
plt.scatter(x3,y3)
plt.xlabel('CSC(Latitude')
plt.ylabel('B-V Value')
plt.savefig('BVPlot.pdf')
plt.show()
