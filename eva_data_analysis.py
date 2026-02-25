# Copyright (c) 2026 thatgardnerone. Licensed under the MIT License.
# See LICENSE file in the project root for full license information.

from __future__ import annotations

import re
import sys

import matplotlib.pyplot as plt
import pandas as pd


# https://data.nasa.gov/resource/eva.json (with modifications)


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
    duration_hours = int(hours) + int(minutes) / 60
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


def calculate_crew_size(crew) -> int | None:
    """Calculate crew_size for a single crew entry.

    Args:
        crew (str): The text entry in the crew column.

    Returns:
        int: The crew size.
    """
    if crew.split() == []:
        return None
    else:
        return len(re.split(r';', crew)) - 1


def add_crew_size_variable(df_):
    """Add crew size (crew_size) variable to the dataset.

    Args:
        df_ (pd.DataFrame): The input data frame.

    Returns:
        df_copy (pd.DataFrame): A copy of df_ with the new crew_size variable added.
    """
    print('Adding crew size variable (crew_size) to dataset')
    df_copy = df_.copy()
    df_copy["crew_size"] = df_copy["crew"].apply(
        calculate_crew_size
    )
    return df_copy


def summarise_categorical(df_, varname_) -> pd.DataFrame:
    """Tabulate the distribution of a categorical variable.

    Args:
        df_ (pd.DataFrame): The input dataframe.
        varname_ (str): The name of the variable.

    Returns:
        pd.DataFrame: dataframe containing the count and percentage of
        each unique value of varname_.
    """
    print(f'Tabulating distribution of categorical variable {varname_}')

    # Prepare statistical summary
    count_variable = df_[[varname_]].copy()
    count_summary = count_variable.value_counts(dropna=False)
    percentage_summary = round(count_summary / count_variable.size, 2) * 100

    # Combine results into a summary data frame
    df_summary = pd.concat([count_summary, percentage_summary], axis=1)
    df_summary.columns = ['count', 'percentage']
    df_summary.sort_index(inplace=True)

    df_summary = df_summary.reset_index()
    return df_summary


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


def main(input_file, output_file, graph_file):
    """Main function to execute the EVA data analysis pipeline.

    Args:
        input_file (str): The path to the input JSON file.
        output_file (str): The path to the output CSV file.
        graph_file (str): The path to the output graph file.
    """
    print("--START--")

    # Read the EVA dataset from JSON
    print(f'Reading JSON file {input_file}')
    eva_df = read_json_to_dataframe(input_file)

    # Write the cleaned data to CSV for downstream use
    print(f'Saving CSV file to {output_file}')
    write_dataframe_to_csv(eva_df, output_file)

    # Plot cumulative time spent in space over the years
    eva_df.sort_values('date', inplace=True)
    print(f'Plotting cumulative time in space to {graph_file}')
    plot_cumulative_time_in_space(eva_df, graph_file)

    print("--END--")


if __name__ == "__main__":

    if len(sys.argv) < 3:
        input_file = 'data/eva-data.json'
        output_file = 'results/eva-data.csv'
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]

    graph_file = 'results/cumulative_eva_graph.png'

    main(input_file, output_file, graph_file)
