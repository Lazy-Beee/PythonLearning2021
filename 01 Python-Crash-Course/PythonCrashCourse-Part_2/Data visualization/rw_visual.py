import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep generating new random walks while program is active
while True:
    # Make a random walk
    rw = RandomWalk(numpoints=50000)
    rw.fill_walk()

    # Plot points in the walk
    plt.style.use('classic')
    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.numpoints)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors='none', s=15)

    # Emphasize the first and last points
    ax.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolors='none',
               s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
               s=100)

    # Remove the axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Plot and save the walk
    plt.savefig('images/random_walk_plot.png', bbox_inches='tight')
    plt.show()

    # Let user determine continue/stop generating walks
    keep_running = input("Make another walk? (y/n)")
    if not keep_running == 'y':
        break