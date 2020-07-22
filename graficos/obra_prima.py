
from collections import defaultdict

import matplotlib.pyplot as plt

import parameters
import main


par = parameters.parameters()
p, gov, rep = main.main(par)

print('Government ideology {:.3f}'.format(gov.ideology))
print('House ideology {:.3f}'.format(sum([x.ideology for x in rep])/len(rep)))


def results(projects):
    res = defaultdict(lambda: defaultdict(float))
    for each in projects:
        res[each.category]['num'] += 1
        res[each.category]['ideology'] += each.ideology
        res[each.category]['votes'] += each.vote

    avg_ideology = dict()

    for key in res.keys():
        _avg_ideology = res[key]['ideology'] / res[key]['num']
        avg_ideology[key] = _avg_ideology
        print('Total projects {} {:.0f}. Average ideology {:.3f}. Average votes received {:.1f}'.
              format(key, res[key]['num'], _avg_ideology, res[key]['votes'] / res[key]['num']))
    return avg_ideology


def plotting(data, name='single'):
    # TEMPLATE: MODELO PADRÃO
    # Single plotting
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    legend = ['sanctioned', 'not sanctioned', 'proposed']
    colors = ['red', 'blue', 'grey']

    for i, k in enumerate(legend):
        ax.hist([x.ideology for x in data if x.category == k], bins=50, alpha=.35, color=colors[i])

    ax.legend(legend, frameon=False)
    ax.set(xlabel='Ideology', ylabel='Frequency', title='Projects by output')

    # Using plot help from
    # https://matplotlib.org/gallery/showcase/bachelors_degrees_by_gender.html#
    # sphx-glr-gallery-showcase-bachelors-degrees-by-gender-py
    # Remove the plot frame lines. They are unnecessary here.
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    # Ensure that the axis ticks only show up on the bottom and left of the plot.
    # Ticks on the right and top of the plot are generally unnecessary.
    # ax.set_xlim(0, 360)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.yaxis.set_major_formatter(plt.FuncFormatter('{:.0f}'.format))
    # Provide tick lines across the plot to help your viewers trace along
    # the axis ticks. Make sure that the lines are light and small so they
    # don't obscure the primary data lines.
    plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)
    # Remove the tick marks; they are unnecessary with the tick lines we just
    # plotted.
    plt.tick_params(axis='both', which='both', bottom=False, top=False,
                    labelbottom=True, left=False, right=False, labelleft=True)

    plt.savefig('{}.png'.format(name), bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    avg = results(p)
    plotting(p)
