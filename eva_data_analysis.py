# https://data.nasa.gov/resource/eva.json (with modifications)
import matplotlib.pyplot as plt
import pandas as pd


def read_json_to_dataframe(input_file):
    eva_df = pd.read_json(input_file, convert_dates=['date'], encoding='ascii')
    eva_df['eva'] = eva_df['eva'].astype(float)
    eva_df.dropna(axis=0, subset=['duration', 'date'], inplace=True)
    return eva_df


def write_dataframe_to_csv(df, output_file):
    df.to_csv(output_file, index=False, encoding='utf-8')


def plot_cumulative_time_in_space(df, graph_file):
    df.sort_values('date', inplace=True)
    df['duration_hours'] = df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
    df['cumulative_time'] = df['duration_hours'].cumsum()

    plt.plot(df['date'], df['cumulative_time'], 'ko-')
    plt.xlabel('Year')
    plt.ylabel('Total time spent in space to date (hours)')
    plt.tight_layout()
    plt.savefig(graph_file)
    plt.show()


print("--START--")

input_file = open('./eva-data.json', 'r', encoding='ascii')
output_file = open('./eva-data.csv', 'w', encoding='utf-8')
graph_file = './cumulative_eva_graph.png'

# Read the EVA dataset from JSON
print(f'Reading JSON file {input_file.name}')
eva_df = read_json_to_dataframe(input_file)

# Write the cleaned data to CSV for downstream use
print(f'Saving CSV file to {output_file.name}')
write_dataframe_to_csv(eva_df, output_file)

# Plot cumulative time spent in space over the years
print(f'Plotting cumulative time in space to {graph_file}')
plot_cumulative_time_in_space(eva_df, graph_file)

print("--END--")
