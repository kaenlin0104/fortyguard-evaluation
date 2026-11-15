import json
import numpy as np
from pathlib import Path

# Load API response
file_path = Path("api/responses/heatmap_100m.json")

with open(file_path, "r", encoding="utf-8") as file:
    response = json.load(file)

# Extract map data and statistics
result = response["data"]["result"]

features = result["map_data"]["features"]
stats = result["stats_data"]["temperature_stats"]

# Extract temperature from each tile
temperatures = [
    feature["properties"]["average_temperature"]
    for feature in features
]

# Calculate statistics independently
print("Number of tiles:", len(temperatures))
print("Calculated mean:", np.mean(temperatures))
print("Calculated minimum:", np.min(temperatures))
print("Calculated maximum:", np.max(temperatures))
print("Calculated standard deviation:", np.std(temperatures))

print("\nFortyGuard statistics:")
print("Mean:", stats["mean"])
print("Minimum:", stats["minimum"])
print("Maximum:", stats["maximum"])
print("Standard deviation:", stats["standard_deviation"])

print("\nStandard deviation comparison:")
print("NumPy population std:", np.std(temperatures))
print("NumPy sample std:", np.std(temperatures, ddof=1))
print("FortyGuard std:", stats["standard_deviation"])