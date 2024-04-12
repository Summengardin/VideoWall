import csv
from collections import defaultdict

# Define the path to your log file
log_file_path = 'traces.log'

# Function to clean up and extract value from log components
def extract_value(part):
    # Removing the type specification and extra quotes or spaces
    return part.split('=')[1].split(')')[1].replace('"', '').strip()

# Read the log file and collect times for each element
element_times = defaultdict(list)

with open(log_file_path, 'r') as file:
    for line in file:
        if 'latency' in line:
            if 'element-latency' in line:
                parts = line.split(', ')
                element = time = None
                for part in parts:
                    if 'element=(string)' in part:
                        element = extract_value(part)
                    elif 'time=(guint64)' in part:
                        time = extract_value(part)
                if time is not None:
                    try:
                        time = int(time)
                        time = time / 1e6  # Convert to ms
                    except ValueError:
                        time = None
                if element and time is not None:
                    element_times[element].append(time)
            else:
                parts = line.split(', ')

                time = None
                for part in parts:
                    if 'time=(guint64)' in part:
                        time = extract_value(part)
                if time is not None:
                    try:
                        time = int(time)
                        time = time / 1e6  # Convert to ms
                        element_times["total"].append(time)
                    except ValueError:
                        pass
                


# Assuming elements are reported in a synchronized fashion, aligning times
elements_sorted = sorted(element_times.keys())
rows = zip(*[element_times[element] for element in elements_sorted])


# Make statistics
element_stats = {}
for element in elements_sorted:
    times = element_times[element]
    element_stats[element] = {
        'count': len(times),
        'min': min(times),
        'max': max(times),
        'avg': sum(times) / len(times),
    }

# Print statistics
for element, stats in element_stats.items():
    print(f"Element: {element}")
    print(f"  Count: {stats['count']}")
    print(f"  Min: {stats['min']:.2f} ms")
    print(f"  Max: {stats['max']:.2f} ms")
    print(f"  Avg: {stats['avg']:.2f} ms")
    print()


# Write to CSV
output_csv_path = 'element_times_cleaned.csv'
with open(output_csv_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write the header
    csvwriter.writerow(elements_sorted)
    # Write the rows
    for row in rows:
        csvwriter.writerow(row)

print(f"CSV file '{output_csv_path}' has been created.")
