#reading and ploting Breakthrough Listen Open Data Archive http://seti.berkeley.edu/opendata
#import python libraries
import matplotlib.pyplot as plt
from matplotlib import interactive
interactive(True)
from blimpy import Waterfall
#load data file
file_path = 'GBT_57523_70769_HIP17147_mid.h5'
obs = Waterfall(file_path)
obs.info()
print(obs.header) #print object info
print(obs.data.shape)
plt.figure(figsize=(80, 60))
plt.subplot(3,1,1)
obs.plot_spectrum(f_start=800, f_stop=9000)
plt.savefig(file_path + "spectrum.png") #save png detailed graphic with the spectrum
obs.plot_waterfall(f_start=800, f_stop=9000)
plt.savefig(file_path + "waterfall.png") #save png detailed waterfall image