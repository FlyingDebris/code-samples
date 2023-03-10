#   calculating age of the galaxy
#   using HR diagram to find falloff point for stars; age can be determined from location of falloff point
#   like that tutoring assignment we helped that one girl with a while ago
#   Clusters: 

#   NGC 7089   M 2          21 33 27.02  -00 49 23.7    53.37  -35.77   11.5  10.4   5.6   7.5  -6.7
#   NGC 7006                21 01 29.38  +16 11 14.4    63.77  -19.41   41.2  38.5  17.2  34.8 -13.7
#   Pal 5                   15 16 05.25  -00 06 41.8     0.85   45.86   23.2  18.6  16.2   0.2  16.7
#   NGC 5053                13 16 27.09  +17 42 00.9   335.70   78.95   17.4  17.8   3.0  -1.4  17.1
                         
import numpy as np
import matplotlib.pyplot as plt

ifile1 = 'NGC7006_Stars.csv'
stars1 = np.genfromtxt(ifile1, skip_header=1,skip_footer=0,delimiter=',')
print(stars1[:,10])
g = stars1[:,10]
gr = stars1[:,10]-stars1[:,11]
plt.scatter(gr,g,s=0.25)
plt.axvline(0.4,color='red')
plt.xlabel('G-R')
plt.ylabel('G')
plt.title('NGC 7006 G-R vs. G')
plt.gca().invert_yaxis()
plt.xlim(-2,3)
plt.grid()
plt.savefig('NGC7006GRvsG,pdf')
plt.show()

ifile2 = 'Pal5_Stars.csv'
stars2 = np.genfromtxt(ifile2, skip_header=1,skip_footer=0,delimiter=',')
print(stars2[:,10])
g = stars2[:,10]
gr = stars2[:,10]-stars2[:,11]
plt.scatter(gr,g,s=0.25)
plt.axvline(0.4,color='red')
plt.xlabel('G-R')
plt.ylabel('G')
plt.title('Palomar 5 G-R vs. G')
plt.gca().invert_yaxis()
plt.xlim(-1,2)
plt.grid()
plt.savefig('Palomar5GRvsG,pdf')
plt.show()

ifile3 = 'NGC7089_Stars.csv'
stars3 = np.genfromtxt(ifile3, skip_header=1,skip_footer=0,delimiter=',')
print(stars3[:,10])
g = stars3[:,10]
gr = stars3[:,10]-stars3[:,11]
plt.scatter(gr,g,s=0.25)
plt.axvline(0.3,color='red')
plt.xlabel('G-R')
plt.ylabel('G')
plt.title('NGC 7089 G-R vs. G')
plt.gca().invert_yaxis()
plt.xlim(-2,3)
plt.grid()
plt.savefig('NGC7089GRvsG,pdf')
plt.show()

ifile4 = 'NGC5053_Stars.csv'
stars4 = np.genfromtxt(ifile4, skip_header=1,skip_footer=0,delimiter=',')
print(stars4[:,10])
g = stars4[:,10]
gr = stars4[:,10]-stars4[:,11]
plt.scatter(gr,g,s=0.25)
plt.axvline(0.25,color='red')
plt.xlabel('G-R')
plt.ylabel('G')
plt.title('NGC 5053 G-R vs. G')
plt.gca().invert_yaxis()
plt.xlim(-1,2)
plt.grid()
plt.savefig('NGC5053GRvsG,pdf')
plt.show()


print(len(stars1[:,10]))
print(len(stars2[:,10]))
print(len(stars3[:,10]))
print(len(stars4[:,10]))
#   sim in textbook about how large vs small mass stars evolve and the graphs for these with that