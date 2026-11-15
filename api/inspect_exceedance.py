import json
from pathlib import Path

file_path = Path("api/responses/exceedance_100m.json")

with open(file_path, "r", encoding="utf-8") as file:
    response = json.load(file)

result = response["data"]["result"]

# Inspect stats_data
stats = result["stats_data"]

print("=== STATS DATA ===")
print(json.dumps(stats, indent=4, ensure_ascii=False))

# Inspect map_data
features = result["map_data"]["features"]

print("\n=== MAP DATA ===")
print("Total features:", len(features))

if features:
    print("\nFirst feature:")
    print(json.dumps(features[0], indent=4, ensure_ascii=False))