import numpy as np
import matplotlib.pyplot as plt

ax = []
ay = []
plt.ion()
n =100
for i in range(100):
    ax.append(i)
    ay.append(n)
    plt.clf()
    plt.plot(ax,ay)
    plt.pause(0.05)
