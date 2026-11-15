import json
from pathlib import Path

file_path = Path("api/responses/heatmap_20m.json")

with open(file_path, "r", encoding="utf-8") as file:
    response = json.load(file)

features = response["data"]["result"]["map_data"]["features"]

tile_ids = []
missing_ids = 0
missing_temperatures = 0

for feature in features:
    properties = feature.get("properties", {})

    tile_id = properties.get("tile_id")
    temperature = properties.get("average_temperature")

    if tile_id is None:
        missing_ids += 1
    else:
        tile_ids.append(tile_id)

    if temperature is None:
        missing_temperatures += 1

print("Total cells:", len(features))
print("Unique tile IDs:", len(set(tile_ids)))
print("Duplicate IDs:", len(tile_ids) - len(set(tile_ids)))
print("Missing IDs:", missing_ids)
print("Missing temperatures:", missing_temperatures)

print("\nTemperature fields:")
for field in [
    "average_temperature",
    "min_temperature",
    "max_temperature"
]:
    values = [
        f["properties"].get(field)
        for f in features
    ]
    print(field, "missing:", sum(v is None for v in values))