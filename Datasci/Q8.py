import pandas as pd
import matplotlib.pyplot as plt

smokers = [225,258,250,225,213,232,216,216,183,287,200,211,216,200,256,246,267,243,271,280,217,280,209,196,209,243,225,232,200,230,217,246,209,284,288,280,200,237,216,155,309,305,351]
ex_smokers = [250,249,175,160,213,200,238,192,242,217,217,134,213,174,188,257,271,163,242,267,267,183,300,310,328,321,292,227,263,249,243,218,228]

 
box_plot_data=[smokers, ex_smokers]
plt.title("Cholesterol Levels throughout Smokers vs Non-Smokers")
plt.boxplot(box_plot_data,patch_artist=True,labels=['Smokers', 'Ex-Smokers'])
plt.show()


