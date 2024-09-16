from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

x_y, c = make_blobs(cluster_std = 20, n_samples= 100000, centers= 2)
print(x_y, c)

plt.scatter(x_y[:, 0], x_y[:, 1], c=c)
plt.show()