import json
from pathlib import Path

def load_response(filename):
    path = Path("api/responses") / filename

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

# Load both responses
data_100m = load_response("heatmap_100m.json")
data_20m = load_response("heatmap_20m.json")

# Extract features
features_100m = data_100m["data"]["result"]["map_data"]["features"]
features_20m = data_20m["data"]["result"]["map_data"]["features"]

# Extract statistics
stats_100m = data_100m["data"]["result"]["stats_data"]
stats_20m = data_20m["data"]["result"]["stats_data"]

print("=== GRANULARITY COMPARISON ===")

print("100m cells:", len(features_100m))
print("20m cells:", len(features_20m))

print("\n100m statistics:")
print(json.dumps(stats_100m, indent=4))

print("\n20m statistics:")
print(json.dumps(stats_20m, indent=4))