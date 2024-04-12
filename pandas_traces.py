import pandas as pd
import re

log_file_path = 'traces.log'  # Path to your log file

# Regular expression to extract timestamp (ts) values
regex = r"ts=\(guint64\)(\d+);"

timestamps = []

# Read the log file and extract timestamp data
with open(log_file_path, 'r') as file:
    for line in file:
        match = re.search(regex, line)
        if match:
            ts_ns = int(match.group(1))
            timestamps.append(ts_ns)

# Create a pandas DataFrame with the timestamps
df = pd.DataFrame({'Timestamp_ns': timestamps})

# Calculate the time difference between consecutive entries in nanoseconds
df['Delta_ns'] = df['Timestamp_ns'].diff()

# Convert time difference from nanoseconds to seconds
df['Delta_sec'] = df['Delta_ns'] / 1e9

# Calculate FPS from the average time difference between frames
# Exclude the first row since it does not have a delta
average_delta_sec = df['Delta_sec'][1:].mean()
fps = 1 / average_delta_sec if average_delta_sec else 0

print(f"Average Frame Time: {average_delta_sec:.6f} seconds")
print(f"Estimated FPS: {fps:.2f}")

# Save the DataFrame to a CSV file
df.to_csv('timestamps.csv', index=False)