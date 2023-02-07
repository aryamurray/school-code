import matplotlib.pyplot as plt
import numpy as np

labels = np.array(["18-24", "25-34","35-44","45-54", "55-64","65+"])
xlabels = ["18-24", "25-34","35-44","45-54", "55-64","65+"]



y = smart_phone = np.array([49,58,44,28,22,11,])
z = other_cell_phone = np.array([46,35,45,58,59,45])
v = no_smart_phone = np.array([5,7,11,14,19,44])

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars


  
plt.bar(x, y, width, label='Smart Phone')
plt.xticks(x+width, xlabels)
plt.bar(x+width, z, width, label='Other Phone')
plt.bar(x+width*2, v, width, label='No Phone')
plt.xlabel("Age")
plt.ylabel("Number of People")
plt.title("Comparing Age in relation to phone usage")
plt.legend()
plt.show()