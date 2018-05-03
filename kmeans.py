import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time


""" This python script generates a sequence of plots illustrating how the k-means 
clustering algorithm works. It also saves these plots in separate image files.

Author: http://wesamelshamy.com
https://github.com/welshamy/k-means-illustrator
"""


def main():
    n_clusters = 3       # Number of clusters
    n_points = 20        # Number of points
    iterations = 10      # Number of iterations
    dimensions = (5, 5)  # Dimension of the figure

    colors = ['red', 'green', 'blue', 'orange', 'turquoise', 'yellow', 'pink', 'purple']

    pad = dimensions[0]/10.
    scale = dimensions[0]/6.

    points = pd.DataFrame({
        'x': np.random.rand(n_points) * scale * dimensions[0] + pad,
        'y': np.random.rand(n_points) * scale * dimensions[1] + pad,
        'cluster': np.zeros(n_points)
    })

    centers = pd.DataFrame({
        'x': np.random.rand(n_clusters) * scale * dimensions[0] + pad,
        'y': np.random.rand(n_clusters) * scale * dimensions[1] + pad,
        'color': colors[:3]
    })

    def find_nearest_cluster(p):
        """Return index of center closest to passed point."""
        dist = np.sqrt((centers.x - p.x)**2 + (centers.y - p.y)**2)
        return dist.idxmin()

    plt.figure(figsize=dimensions)
    plt.ion()
    plt.show()

    for i in range(iterations):
        points['cluster'] = points.apply(find_nearest_cluster, axis=1)

        plt.subplot(aspect='equal')
        plt.scatter(points.x, points.y, s=100, c=centers.iloc[points.cluster].color, alpha=0.5)
        plt.scatter(centers.x, centers.y, s=50, c=centers.color, alpha=0.5, marker='+')
        plt.text(dimensions[0] * 0.1, dimensions[1] * 0.9, 'Iteration {}'.format(i), fontsize=14)

        plt.axis([0, dimensions[0], 0, dimensions[1]])

        new_centers = points.groupby(by='cluster').mean()
        centers[['x', 'y']] = new_centers[['x', 'y']]

        plt.savefig('knn_{}_points_{}_clusters_{}_iterations.png'.format(n_points, n_clusters, i))
        plt.draw()
        plt.pause(0.001)
        time.sleep(2)
        plt.clf()


if __name__ == '__main__':
    main()
