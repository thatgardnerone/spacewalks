# https://data.nasa.gov/resource/eva.json (with modifications)
import matplotlib.pyplot as plt
import pandas as pd

print("--START--")

input_file = open('./eva-data.json', 'r', encoding='ascii')
output_file = open('./eva-data.csv', 'w', encoding='utf-8')
graph_file = './cumulative_eva_graph.png'

# Read the EVA dataset from JSON
print(f'Reading JSON file {input_file.name}')
eva_df = pd.read_json(input_file, convert_dates=['date'], encoding='ascii')
eva_df['eva'] = eva_df['eva'].astype(float)

# Clean data by removing rows with missing duration or date values
eva_df.dropna(axis=0, subset=['duration', 'date'], inplace=True)

# Write the cleaned data to CSV for downstream use
print(f'Saving CSV file to {output_file.name}')
eva_df.to_csv(output_file, index=False, encoding='utf-8')

# Sort by date and calculate cumulative EVA hours
eva_df.sort_values('date', inplace=True)
eva_df['duration_hours'] = eva_df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()

# Plot cumulative time spent in space over the years
print(f'Plotting cumulative time in space to {graph_file}')
plt.plot(eva_df['date'], eva_df['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()

print("--END--")
