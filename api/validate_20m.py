
import json
from pathlib import Path
from shapely.geometry import shape, Polygon

file_path = Path("api/responses/heatmap_20m.json")

with open(file_path, "r", encoding="utf-8") as file:
    response = json.load(file)

features = response["data"]["result"]["map_data"]["features"]

aoi_coordinates = [
    (-118.2500, 34.0400),
    (-118.2400, 34.0400),
    (-118.2400, 34.0500),
    (-118.2500, 34.0500),
    (-118.2500, 34.0400)
]

aoi = Polygon(aoi_coordinates)

valid = 0
invalid = 0
intersecting = 0
fully_contained = 0

for feature in features:
    tile = shape(feature["geometry"])

    if tile.is_valid and not tile.is_empty:
        valid += 1
    else:
        invalid += 1

    if tile.intersects(aoi):
        intersecting += 1

    if aoi.covers(tile):
        fully_contained += 1

print("Total cells:", len(features))
print("Valid geometries:", valid)
print("Invalid geometries:", invalid)
print("Intersecting AOI:", intersecting)
print("Fully contained:", fully_contained)
print("Outside AOI:", len(features) - intersecting)
