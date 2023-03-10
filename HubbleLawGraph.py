import matplotlib.pyplot as plt
import numpy as np

infile = 'GalaxyListsAllStudents - GalaxyListsAllStudents.csv'
galaxies = np.genfromtxt(infile, skip_header=1,skip_footer=0,delimiter=',')
speed = galaxies[:,2]
distance = galaxies[:,4]
speedcalc= np.array(galaxies[:,2])
distancecalc = np.array(galaxies[:,4])
combinedcalc = np.concatenate((speedcalc,distancecalc), axis=0)
print(combinedcalc)
curveX = np.arange(0,300,5)
curveY = curveX * 65
h0 = np.linalg.lstsq(combinedcalc,25)
#   Still working on this
print("Hubble constant is",h0)
plt.scatter(speed,distance)
plt.plot(curveX,curveY)
plt.title('Galaxy Speed (km/s) vs. Distance (Mpc)')
plt.xlabel('Galaxy Distance (Mpc)')
plt.ylabel('Galaxy Speed (km/s)')
plt.text(170,17500,'H0: 65km/s/Mpc')
plt.show()