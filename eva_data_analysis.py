# https://data.nasa.gov/resource/eva.json (with modifications)
import matplotlib.pyplot as plt
import pandas as pd


def read_json_to_dataframe(input_file):
    """Read the data from a JSON file into a Pandas dataframe.

    Cleans the data by removing any incomplete rows and sort by date.

    Args:
        input_file (str): The path to the JSON file.

    Returns:
        eva_df (pd.DataFrame): The cleaned and sorted data as a dataframe structure.
    """
    eva_df = pd.read_json(input_file, convert_dates=['date'], encoding='ascii')
    eva_df['eva'] = eva_df['eva'].astype(float)
    eva_df.dropna(axis=0, subset=['duration', 'date'], inplace=True)
    return eva_df


def write_dataframe_to_csv(df, output_file):
    """Write the dataframe to a CSV file.

    Args:
        df (pd.DataFrame): The input dataframe.
        output_file (str): The path to the output CSV file.
    """
    df.to_csv(output_file, index=False, encoding='utf-8')


def text_to_duration(duration):
    """Convert a text format duration "HH:MM" to duration in hours.

    Args:
        duration (str): The text format duration.

    Returns:
        duration_hours (float): The duration in hours.
    """
    hours, minutes = duration.split(":")
    duration_hours = int(hours) + int(minutes)/6
    return duration_hours


def add_duration_hours(df):
    """Add duration in hours as a new column to the dataframe.

    Args:
        df (pd.DataFrame): The input dataframe.

    Returns:
        df_copy (pd.DataFrame): A copy of df with the new duration_hours column added.
    """
    df_copy = df.copy()
    df_copy['duration_hours'] = df_copy['duration'].apply(text_to_duration)
    return df_copy


def plot_cumulative_time_in_space(df, graph_file):
    """Plot the cumulative time spent in space over the years.

    Args:
        df (pd.DataFrame): The input dataframe.
        graph_file (str): The path to the output graph file.
    """
    df = add_duration_hours(df)
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
eva_df.sort_values('date', inplace=True)
print(f'Plotting cumulative time in space to {graph_file}')
plot_cumulative_time_in_space(eva_df, graph_file)

print("--END--")
