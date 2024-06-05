import pandas as pd
from collections import defaultdict
import argparse
import os

parser = argparse.ArgumentParser(description='Extract timing data from a GStreamer log file and generate statistics')
parser.add_argument('log_file_path', nargs='?' , type=str, default='traces.log', help='Path to the input .log file')
args = parser.parse_args()

log_file_path = args.log_file_path

def extract_value(part):
    return part.split('=')[1].split(')')[1].replace('"', '').strip().replace(';', '')

def calculate_fps(df, column=None):
    if column:
        df = df.dropna(subset=[column]).copy()

    df['timestamp_diff'] = df['ts'].astype(float).diff() 
    df['fps'] = 1 / (df['timestamp_diff'] / 1e9)    

    return df

frame_times = []
current_frame = defaultdict(lambda: float('nan')) 
elements_in_current_frame = set()

with open(log_file_path, 'r') as file:
    for line in file:
        if 'latency' in line:
            parts = line.split(', ')
            element = time = ts = None
            for part in parts:
                if 'element=(string)' in part:
                    element = extract_value(part)
                elif 'time=(guint64)' in part:
                    time = extract_value(part)
                elif 'ts=(guint64)' in part:
                    ts = extract_value(part)

            if time is not None:
                try:
                    time = int(time)
                    time = time / 1e6  # Convert to ms
                except ValueError:
                    time = None

            if element and time is not None:
                if ts is not None and 'ts' not in current_frame:
                    current_frame['ts'] = ts
                if element in elements_in_current_frame:
                    # A duplicate element indicates a new frame
                    frame_times.append(current_frame)
                    current_frame = defaultdict(lambda: float('nan'))
                    elements_in_current_frame = set()


                current_frame[element] = time
                elements_in_current_frame.add(element)

if current_frame:
    frame_times.append(current_frame)

df = pd.DataFrame(frame_times)

outname = 'element_times_cleaned.csv'
outdir = './output'
if not os.path.exists(outdir):
    os.mkdir(outdir)

output_csv_path = os.path.join(outdir, outname)  

df.to_csv(output_csv_path, index_label='Frame', mode='w')
print(f"CSV file '{output_csv_path}' has been created.")

element_stats = {}
for element in df.columns[1:]:
    times = df[element].dropna()
    element_stats[element] = {
        'count': len(times),
        'min': times.min(),
        'max': times.max(),
        'avg': times.mean(),
    }

output_txt_path = 'output/Summary.txt'
with open(output_txt_path, 'w') as file:
    for element, stats in element_stats.items():
        file.write(f"Element: {element}\n")
        file.write(f"  Count: {stats['count']}\n")
        file.write(f"  Min: {stats['min']:.2f} ms\n")
        file.write(f"  Max: {stats['max']:.2f} ms\n")
        file.write(f"  Avg: {stats['avg']:.2f} ms\n")
        file.write("\n")

    df = calculate_fps(df)

    file.write("Frames Per Second (FPS)\n")
    file.write(f"  Count: {len(df['fps'])}\n")
    file.write(f"  Min: {df['fps'].min():.2f} fps\n")
    file.write(f"  Max: {df['fps'].max():.2f} fps\n")
    file.write(f"  Avg: {df['fps'].mean():.2f} fps\n")

outname = 'Summary.txt'
output_txt_path = os.path.join(outdir, outname)  

print(f"Text file '{output_txt_path}' has been created.")

