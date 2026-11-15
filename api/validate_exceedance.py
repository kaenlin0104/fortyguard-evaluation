import json
import numpy as np
from pathlib import Path

# Load API response
file_path = Path("api/responses/exceedance_100m.json")

with open(file_path, "r", encoding="utf-8") as file:
    response = json.load(file)

result = response["data"]["result"]

features = result["map_data"]["features"]
stats = result["stats_data"]

# Extract values
values = [
    feature["properties"]["value"]
    for feature in features
]

# Calculate independently
print("Total cells:", len(values))
print("Unique values:", sorted(set(values)))
print("Calculated minimum:", min(values))
print("Calculated maximum:", max(values))
print("Calculated mean:", np.mean(values))

print("\nFortyGuard statistics:")
print("Minimum:", stats["min"])
print("Maximum:", stats["max"])
print("Mean:", stats["mean"])

# Check data quality
print("\nData quality:")
print("Missing values:", sum(v is None for v in values))
print("Values below zero:", sum(v < 0 for v in values))
print("Values above 8 hours:", sum(v > 8 for v in values))

from collections import Counter

distribution = Counter(values)

print("\nExceedance distribution:")

for hours, count in sorted(distribution.items()):
    percentage = count / len(values) * 100

    print(
        f"{hours} hours: {count} cells "
        f"({percentage:.2f}%)"
    )