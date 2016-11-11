import numpy as np
import os
import matplotlib.pyplot as plt

# Function for parsing CSV files from Yokogawa DL850
def DL850_parser(filename):
    # The first 16 rows are header information, thus can be skiped
    # using genfromtxt instead of loadtxt because it can handle data with blank space
    # using loadtxt will lead to some strange errors
    data = np.genfromtxt(filename,delimiter=",",skiprows=16)

    # Add a time column at the first column
    # np.linspace generates a single row, which is 1D.
    # In order to transpose it, it first need to be converted to 2D:
    # np.linspace -> [np.linspace]
    data = np.hstack((np.transpose([np.linspace(0,2,10010)]),data[:,1:9]))
    return data


# Only excute the following contents if the script is called from commandline.
# Will not be excute if being imported as a module.
if __name__ == '__main__':

    # Loop over all the files in the current directory.
    for filename in os.listdir("."):
        if filename.endswith(".CSV"): 
            
            # Extract data
            data = DL850_parser(filename)
            # For example, plot some data.
            plt.plot(data[:,0],data[:,7])

            plt.title(filename)
            plt.xlim(0,2)
            plt.ylim(-5,50)

            # Save the image file. DPI can be mannually changed.
            output_name = filename+".png"
            plt.savefig(output_name, dpi=320)
            # Clear the plot before exit the loop. Otherwise all plot may overlap.
            plt.clf()
