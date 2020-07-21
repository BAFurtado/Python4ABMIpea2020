""" Terceiro exemplo
"""

import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(2, 100)

fig, axs = plt.subplots(2, 2, figsize=(5, 5))
# Visit stackoverflow...
axs[0, 0].hist(data[0], bins=20, color='red')
axs[1, 0].scatter(data[0], data[1], alpha=.5, color='green', marker='*')
axs[0, 1].plot(data[0], data[1], linewidth=.2, color='red')
axs[1, 1].hist2d(data[0], data[1], cmap='Accent')

plt.show()
