import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['Key Gen.', 'Encaps. Time', 'Decaps. Time']
values = [0.007, 0.009, 0.006]
colors = ['lime', 'magenta', 'blue']

x = np.arange(len(categories))

bar_width = 0.4

# Create a bar chart
plt.bar(x, values, width=bar_width, color=colors)

# Add labels and a title
# plt.xlabel('')
plt.ylabel('Time(ms)')
plt.title('Kyber Raw Performance')

plt.xticks(x, categories)

# Show the chart
plt.show()