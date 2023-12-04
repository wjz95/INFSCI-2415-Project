import matplotlib.pyplot as plt
import pandas as pd
import os

# Define the directory where your CSV files are located
data_directory = './data/'

# Initialize lists to store data from all CSV files
all_x = []
all_y1 = []
line_color = ['#e377c2','c','b','#7f7f7f','magenta', 'lime', 'hotpink' ]
# all_y2 = []
# Initialize lists for more lines as needed
file_names = []  # To store CSV file names without the extension

# Get a list of all CSV files in the directory
csv_files = [f for f in os.listdir(data_directory) if f.endswith('.csv')]

# Iterate through each CSV file and accumulate the data
# for csv_file in csv_files:
data = pd.read_csv(os.path.join(data_directory, csv_files[0]))
all_x.append(data['pktloss'])  # Append X-axis data
all_y1.append(data['percent025'])  # Append Y-axis data for line 1
all_y1.append(data['percent0375'])
all_y1.append(data['percent05'])  # Append Y-axis data for line 1
all_y1.append(data['percent0625'])  # Append Y-axis data for line 1
all_y1.append(data['percent075'])  # Append Y-axis data for line 1
all_y1.append(data['percent085'])  # Append Y-axis data for line 1
all_y1.append(data['percent095'])  # Append Y-axis data for line 1
index = [0,1,2,3,4,5,6]

    # all_y2.append(data['Line2'])  # Append Y-axis data for line 2
    # Append more lines as needed
    # file_name_without_extension = os.path.splitext(csv_file)[0]  # Extract file name without extension
    # modified_file_name = file_name_without_extension.split('p')[0]  # Remove characters after the second common character
    # file_names.append(file_name_without_extension)

# Create a single multi-line plot
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
# plt.figure(figsize=(8.5, 11))
perc_set=['25th percentile','37.5th percentile', '50th percentile', '62.5th percentile', '75th percentile','85th percentile', '95th percentile']
# Plot data accumulated from all CSV files

for i in index:
    plt.plot(all_x[0], all_y1[i], label=perc_set[i], marker='o', linestyle='-',color = line_color[i])
    # plt.plot(all_x[i], all_y2[i], label=f'Line 2 ({csv_file})', marker='s', linestyle='--')
    # Add more lines with plt.plot as needed

# Customize the plot
plt.title('The Impact of Kyber on TLS Handshake Completion Time(RTT=5ms)', fontsize= 16)
plt.xlabel('Packet Loss Rate(%)',fontsize = 14)
plt.ylabel('Handshake Completion Time(ms)', fontsize = 14)
plt.yscale('log')
plt.xticks(fontsize=12)  # Tick label font size
plt.yticks(fontsize=12)  # Tick label font size
plt.legend(fontsize=12)  # Legend font size
plt.grid(True)


# xmin = min(min(x) for x in all_x)
# plt.xlim(xmin, None)
# ymin = min(min(y) for y in all_y1)
# plt.ylim(ymin, None)

# Show the plot or save it to a file
plt.show()  # To display the plot
# plt.savefig('kyber_bar.pdf')
# To save the plot as an image file, use plt.savefig('output_plot.png') or another format