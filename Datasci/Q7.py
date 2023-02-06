import matplotlib.pyplot as plt
import pandas as pd

data = [71,70,124,113,108,61,91,51,263,112,231,72,87,61,58,443,146,149,54,118,71,104,101,64,76,48,74,102,51,55,60,62,43,48,84,44,47,61,52,65,47,51,59,81,118,97,59,406,61,52]

plt.hist(data, bins= 10)
plt.xlabel("Annual Revenue in Billions of Dollars")
plt.ylabel("Number of Companies")
plt.title("Revenue Distribution by 50 Fortune 500 Companies")
plt.show()