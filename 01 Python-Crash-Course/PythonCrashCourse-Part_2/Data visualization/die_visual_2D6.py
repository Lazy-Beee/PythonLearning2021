from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create two D6
die1 = Die()
die2 = Die()

# Roll the die
results = [die1.roll() + die2.roll() for i in range(50_000)]

# Analysis the results
max_result = die1.num_sides + die2.num_sides
frequencies = [results.count(i) for i in range(2, max_result + 1)]

# Visualize the results
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of result'}
my_layout = Layout(title='Results of rolling two D6 50,000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='images/2d6.html')