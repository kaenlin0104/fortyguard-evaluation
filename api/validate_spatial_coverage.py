import json
from pathlib import Path
from shapely.geometry import shape, Polygon

# Load response
file_path = Path("api/responses/heatmap_100m.json")

with open(file_path, "r", encoding="utf-8") as file:
    response = json.load(file)

features = response["data"]["result"]["map_data"]["features"]

# Reconstruct original AOI
aoi_coordinates = [
    (-118.2500, 34.0400),
    (-118.2400, 34.0400),
    (-118.2400, 34.0500),
    (-118.2500, 34.0500),
    (-118.2500, 34.0400)
]

aoi = Polygon(aoi_coordinates)

# Check tile intersection with AOI
intersecting = 0
outside = 0
fully_contained = 0

for feature in features:
    tile = shape(feature["geometry"])

    if tile.intersects(aoi):
        intersecting += 1
    else:
        outside += 1

    if aoi.covers(tile):
        fully_contained += 1

print("Total tiles:", len(features))
print("Tiles intersecting AOI:", intersecting)
print("Tiles outside AOI:", outside)
print("Tiles fully contained in AOI:", fully_contained)