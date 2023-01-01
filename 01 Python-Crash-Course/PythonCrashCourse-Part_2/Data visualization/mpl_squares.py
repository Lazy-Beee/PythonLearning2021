import matplotlib.pyplot as plt

numbers = []
squares = []
for i in range(1, 5):
    numbers.append(i)
    squares.append(i * i)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(numbers, squares, linewidth=3)

# Set chart title and labels
ax.set_title('Square Numbers', fontsize=14)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Square of value', fontsize=12)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)

plt.show()