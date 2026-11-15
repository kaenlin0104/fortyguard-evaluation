import json
from pathlib import Path
from shapely.geometry import shape

# Load API response
file_path = Path("api/responses/heatmap_100m.json")

with open(file_path, "r", encoding="utf-8") as file:
    response = json.load(file)

# Extract GeoJSON features
features = response["data"]["result"]["map_data"]["features"]

# Validate geometries
valid_count = 0
invalid_count = 0
empty_count = 0

for feature in features:
    geometry = shape(feature["geometry"])

    if geometry.is_empty:
        empty_count += 1
    elif geometry.is_valid:
        valid_count += 1
    else:
        invalid_count += 1

print("Total features:", len(features))
print("Valid geometries:", valid_count)
print("Invalid geometries:", invalid_count)
print("Empty geometries:", empty_count)