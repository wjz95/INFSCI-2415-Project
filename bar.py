import matplotlib.pyplot as plt
import pandas as pd
import os

# Define the directory where your CSV files are located
data_directory = './data/'

# Initialize lists to store data from all CSV files
all_x = []
all_y1 = []
bar_width = 0.2  # Width of each bar
index = []  # X-axis labels
line_color = ['#e377c2','c','b','#7f7f7f']

file_names =[]

# Get a list of all CSV files in the directory
csv_files = [f for f in os.listdir(data_directory) if f.endswith('.csv')]

# file_names = []  # To store CSV file names without the extension

# Iterate through each CSV file and accumulate the data
for csv_file in csv_files:
    data = pd.read_csv(os.path.join(data_directory, csv_file))
    all_x.append(data['pktloss'])  # Append X-axis data
    all_y1.append(data['percent095'])  # Append Y-axis data for line 1
    file_name_without_extension = os.path.splitext(csv_file)[0]  # Extract file name without extension
    modified_file_name = file_name_without_extension.split('p')[0]  # Remove characters after the second common character
    file_names.append(file_name_without_extension)


# Create a grouped bar chart
plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
rtt_set=['(RTT=5ms)','(RTT=78ms)','(RTT=195ms)','(RTT=31ms)']

# Plot data accumulated from all CSV files
for i, csv_file in enumerate(csv_files):
    x = [pos + bar_width * i for pos in range(len(all_x[i]))]
    # plt.bar(x, all_y1[i], width=bar_width, label=f'{file_names[i]} {rtt_set[i]}', color=line_color[i])
    plt.bar(x, all_y1[i], width=bar_width,label=f'{file_names[i]} {rtt_set[i]}', color=line_color[i])

# Customize the plot
plt.title('The Impact of Kyber on TLS Handshake Completion Time', fontsize=16)
plt.xlabel('Packet Loss Rate(%)', fontsize=14)
plt.ylabel('Handshake Completion Time(ms)', fontsize=14)

#
tick_positions = [pos + bar_width * len(csv_files) / 2 for pos in range(len(all_x[0]))]
index = all_x[0]

# plt.xticks([pos + bar_width * (len(csv_files) / 2) for pos in range(len(all_x[0]))], index, fontsize=12)
plt.xticks(tick_positions, index, fontsize=12,rotation='vertical')
plt.yticks(fontsize=12)
plt.legend(fontsize=12)
plt.gca().margins(y=0.05)
# plt.grid(True)

# Show the grouped bar chart
plt.show()