#These import numpy and matplotlib, which are both necessary to calculate and display the results.
import numpy as np
import matplotlib.pyplot as plt

###   Read Data   ###

#   This allows us to read the data from the text or csv file, you need to make sure it's in the same folder as the python file though.

infile = 'Cepheid_Stars_1.txt'
dat = np.genfromtxt(infile,skip_header=61, skip_footer=4, delimiter=' ', usecols=(0,1))


#   I used these to test which sections we were pulling from, to verify that we were getting the correct values.
#print (dat[:,0])
#print (dat[:,1])

###  Create Graph ###

#   These are used to read in the first and second columns of the text file, which we can then display later. 
RightAscension = (dat[:,0])*(np.pi/180)
Declination = dat[:,1]

#   This converts our declination into radians.
RadDec = Declination*(np.pi/180.0)

#   This gives us our tangent measurement.
TanDec = np.tan(RadDec)

#   X-axis for our curve fit sine wave.
sineX = (np.arange(0,2*np.pi,0.1))
#   Y axis values for our curve fit sine wave.
#sineY = 2*np.sin(sineX*(np.pi/180)+(80*(np.pi/180)))
sineY = (np.tan(64*(np.pi/180))*np.cos(sineX-(13*(np.pi/180))))

#   This plots the array of points we get from both the right ascension and sine wave.
plt.plot(RightAscension,TanDec,'.')
plt.plot(sineX,sineY)

#   These add labels to the graph.
plt.xlabel('Right Ascension')
plt.ylabel('Declination')

#   This displays our graph. It may not be necessary in Spyder, but it is for me since I'm working in Visual Studio.
plt.show()