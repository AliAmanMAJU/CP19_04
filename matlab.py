import matplotlib.pyplot as plt
import numpy as np
label = ['TCP', 'DNS', 'IRC']
no_movies = [
    4000,
    555,
    1442,
  
]

def bargraph():
    # this is for plotting purpose
    index = np.arange(len(label))
    plt.bar(index, no_movies)
    plt.xlabel('Packet type', fontsize=15)
    plt.ylabel('No of data packets', fontsize=15)
    plt.xticks(index, label, fontsize=15, rotation=30)
    plt.title('Data Packets captured')
    plt.show()

bargraph()