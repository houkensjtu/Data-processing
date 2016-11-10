import numpy as np
from subprocess import call
import os
import matplotlib.pyplot as plt

for filename in os.listdir("."):
    if filename.endswith(".CSV"): 
        data = np.genfromtxt(filename,delimiter=",",skiprows=16)
        data = np.hstack((np.transpose([np.linspace(0,2,10010)]),data[:,1:9]))
        data[:,8] = (data[:,8] - 2.5)*56.027
        data[:,7] = (data[:,7] - 2.5)*56.027
#        np.savetxt("test.csv",data,delimiter=" ")
        plt.plot(data[:,0],data[:,7])
        plt.plot(data[:,0],data[:,8])
        output_name = filename+".png"
        plt.legend(('Left', 'Right'), 'upper left')
        plt.xlabel("Time [sec]")
        plt.ylabel("Displacement [mm]")
        plt.savefig(output_name)
        plt.clf()

