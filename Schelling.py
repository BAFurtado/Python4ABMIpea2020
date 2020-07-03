""" Adpated from Think Complexity 2 edition by Allen Downey (thank you very much).
    Available at https://github.com/AllenDowney/ThinkComplexity2/blob/master/code/chap09.ipynb
    Copyright 2016 Allen Downey, MIT License

    Before running, make sure to copy thinkplot, thinkstats2 and Cell2D
    from the original repository above

    You have to run from the Terminal to work
    Also include a plt.show() command
    """

import warnings

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
from matplotlib.colors import LinearSegmentedColormap
from scipy.signal import correlate2d

import thinkplot
from Cell2D import Cell2D, Cell2DViewer

warnings.filterwarnings("ignore", category=RuntimeWarning)
rc('animation', html='jshtml')


def locs_where(condition):
    """Find cells where a logical array is True.

    condition: logical array

    returns: list of location tuples
    """
    return list(zip(*np.nonzero(condition)))


class Schelling(Cell2D):
    """Represents a grid of Schelling agents."""

    options = dict(mode='same', boundary='wrap')

    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]], dtype=np.int8)

    def __init__(self, n, p):
        """Initializes the attributes.

        n: number of rows
        p: threshold on the fraction of similar neighbors
        """
        self.p = p
        # 0 is empty, 1 is red, 2 is blue
        choices = np.array([0, 1, 2], dtype=np.int8)
        probs = [0.1, 0.45, 0.45]
        self.array = np.random.choice(choices, (n, n), p=probs)

    def count_neighbors(self):
        """Surveys neighboring cells.

        returns: tuple of
            empty: True where cells are empty
            frac_red: fraction of red neighbors around each cell
            frac_blue: fraction of blue neighbors around each cell
            frac_same: fraction of neighbors with the same color
        """
        a = self.array

        empty = a == 0
        red = a == 1
        blue = a == 2

        # count red neighbors, blue neighbors, and total
        num_red = correlate2d(red, self.kernel, **self.options)
        num_blue = correlate2d(blue, self.kernel, **self.options)
        num_neighbors = num_red + num_blue

        # compute fraction of similar neighbors
        frac_red = num_red / num_neighbors
        frac_blue = num_blue / num_neighbors

        # no neighbors is considered the same as no similar neighbors
        # (this is an arbitrary choice for a rare event)
        frac_red[num_neighbors == 0] = 0
        frac_blue[num_neighbors == 0] = 0

        # for each cell, compute the fraction of neighbors with the same color
        frac_same = np.where(red, frac_red, frac_blue)

        # for empty cells, frac_same is NaN
        frac_same[empty] = np.nan

        return empty, frac_red, frac_blue, frac_same

    def segregation(self):
        """Computes the average fraction of similar neighbors.

        returns: fraction of similar neighbors, averaged over cells
        """
        _, _, _, frac_same = self.count_neighbors()
        return np.nanmean(frac_same)

    def step(self):
        """Executes one time step.

        returns: fraction of similar neighbors, averaged over cells
        """
        a = self.array
        empty, _, _, frac_same = self.count_neighbors()

        # find the unhappy cells
        unhappy = frac_same < self.p
        unhappy_locs = locs_where(unhappy)

        # find the empty cells
        empty_locs = locs_where(empty)

        # shuffle the unhappy cells
        if len(unhappy_locs):
            np.random.shuffle(unhappy_locs)

        # for each unhappy cell, choose a random destination
        num_empty = np.sum(empty)
        for source in unhappy_locs:
            i = np.random.randint(num_empty)
            dest = empty_locs[i]

            # move
            a[dest] = a[source]
            a[source] = 0
            empty_locs[i] = source

        # check that the number of empty cells is unchanged
        num_empty2 = np.sum(a == 0)
        assert num_empty == num_empty2

        # return the average fraction of similar neighbors
        return np.nanmean(frac_same)


def make_cmap(color_dict, vmax=None, name='mycmap'):
    """Make a custom color map.

    color_dict: map from numbers to colors
    vmax: high end of the range,
    name: string name for map

    If vmax is None, use the max value from color_dict

    returns: pyplot color map
    """
    if vmax is None:
        vmax = max(color_dict.keys())

    colors = [(value / vmax, color) for value, color in color_dict.items()]

    cmap = LinearSegmentedColormap.from_list(name, colors)

    return cmap


class SchellingViewer(Cell2DViewer):
    # colors from http://colorbrewer2.org/#type=qualitative&scheme=Accent&n=5
    colors = ['#7fc97f','#beaed4','#fdc086','#ffff99','#386cb0']
    cmap = make_cmap({0:'white', 1:colors[2], 2:colors[4]})
    options = dict(interpolation='none', alpha=0.8)


if __name__ == '__main__':
    # grid = Schelling(n=10, p=0.3)
    # viewer = SchellingViewer(grid)
    # viewer.draw()
    # grid.segregation()
    # plt.show()

    grid = Schelling(n=200, p=0.5)
    viewer = SchellingViewer(grid)
    anim = viewer.animate(frames=80)
    plt.show()

    # for p in [0.5, 0.4, 0.3, 0.2]:
    #     #     grid = Schelling(n=100, p=p)
    #     #     segs = [grid.step() for i in range(12)]
    #     #     thinkplot.plot(segs, label='p = %.1f' % p)
    #     #     print(p, segs[-1], segs[-1] - p)
    #     #
    #     # thinkplot.config(xlabel='Time steps', ylabel='Segregation',
    #     #                  loc='lower right', ylim=[0, 1])
    #     #
    #     # thinkplot.save('chap09-2')
