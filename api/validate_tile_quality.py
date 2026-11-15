import json
from pathlib import Path

file_path = Path("api/responses/heatmap_100m.json")

with open(file_path, "r", encoding="utf-8") as file:
    response = json.load(file)

features = response["data"]["result"]["map_data"]["features"]

tile_ids = []
missing_tile_ids = 0
missing_temperatures = 0
missing_geometries = 0

for feature in features:
    properties = feature.get("properties", {})

    tile_id = properties.get("tile_id")

    if tile_id is None:
        missing_tile_ids += 1
    else:
        tile_ids.append(tile_id)

    temperature = properties.get("average_temperature")

    if temperature is None:
        missing_temperatures += 1

    if not feature.get("geometry"):
        missing_geometries += 1

duplicate_ids = len(tile_ids) - len(set(tile_ids))

print("Total features:", len(features))
print("Unique tile IDs:", len(set(tile_ids)))
print("Duplicate tile IDs:", duplicate_ids)
print("Missing tile IDs:", missing_tile_ids)
print("Missing temperatures:", missing_temperatures)
print("Missing geometries:", missing_geometries)

# Check temperature value consistency
temperature_fields = [
    "average_temperature",
    "min_temperature",
    "max_temperature"
]

equal_count = 0
different_count = 0

for feature in features:
    properties = feature["properties"]

    avg_temp = properties.get("average_temperature")
    min_temp = properties.get("min_temperature")
    max_temp = properties.get("max_temperature")

    if avg_temp == min_temp == max_temp:
        equal_count += 1
    else:
        different_count += 1

print("\nTemperature consistency:")
print("All three values equal:", equal_count)
print("Values differ:", different_count)