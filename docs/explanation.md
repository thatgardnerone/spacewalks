# Explanation

## Background

Extra-Vehicular Activity (EVA), commonly known as a spacewalk, is any activity performed by an astronaut or cosmonaut outside the spacecraft. NASA maintains a public dataset of all EVAs conducted since 1965.

## Data pipeline

The Spacewalks analysis pipeline performs the following steps:

1. **Read**: Load EVA records from a JSON file into a pandas DataFrame.
2. **Clean**: Remove rows with missing duration or date values.
3. **Export**: Write the cleaned data to CSV for downstream use.
4. **Plot**: Calculate cumulative hours spent in space and generate a time-series plot.

## Design decisions

- **Duration format**: The raw data stores durations as `H:MM` strings. The `text_to_duration` function converts these to decimal hours for numerical analysis.
- **Crew size parsing**: Crew members are listed as semicolon-separated strings. The `calculate_crew_size` function counts the number of semicolons (each crew member's name is followed by a semicolon).
- **Cumulative plot**: The cumulative time plot provides a visual summary of how total spacewalk hours have accumulated over the decades, highlighting periods of increased EVA activity.
