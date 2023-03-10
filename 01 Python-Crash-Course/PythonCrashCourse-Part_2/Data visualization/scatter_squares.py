import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and labels
ax.set_title('Square Numbers', fontsize=14)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Square of value', fontsize=12)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1100000])

plt.savefig('images/squares_plot.png', bbox_inches='tight')
# plt.show()