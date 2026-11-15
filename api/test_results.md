# FortyGuard API — Test 01: Heatmap Generation

**Endpoint:** `POST /v1/heatmap`  
**Status:** Completed successfully  
**AOI:** Los Angeles, California  
**Requested date:** 2024-07-15  
**Requested time:** 14:00  
**Filter type:** 1 (Single Hour)  
**Granularity:** 100 m  
**Analytic type:** Default (`tcm`)

## Results

- HTTP response: 200
- Activity status: Completed
- Output format: GeoJSON FeatureCollection
- Number of returned tiles: 103
- Mean temperature: 32.3806°C
- Minimum temperature: 32.0285°C
- Maximum temperature: 33.3120°C
- Standard deviation: 0.3263°C

## Initial Observations

1. The API successfully accepted the heatmap request and returned a completed asynchronous task.
2. The response contains both spatial tile data (`map_data`) and aggregated statistics (`stats_data`).
3. Individual tiles contain average, minimum, and maximum temperature fields.
4. The returned tile-level minimum and maximum values are identical to the average values in the observed response.
5. AOI coverage and timestamp/timezone interpretation have not yet been independently verified.

## Next Validation Steps

- Verify spatial coverage and tile geometry.
- Compare the API output with the Dashboard for the same AOI and time.
- Test 20 m granularity and compare coverage and statistics.
- Inspect missing values and response consistency.

### Data Validation

- Retrieved 103 temperature tiles.
- Independently recalculated mean, minimum, and maximum using NumPy.
- All three metrics matched FortyGuard's aggregated statistics.
- Investigated the standard deviation discrepancy.
- Confirmed that FortyGuard's result matches NumPy sample standard deviation (`ddof=1`).
- Population standard deviation (`ddof=0`) produces a slightly different result.

### Spatial Coverage Validation

- Total returned tiles: 103
- Tiles intersecting AOI: 103 (100%)
- Tiles outside AOI: 0
- Fully contained tiles: 90 (87.38%)
- Partially overlapping tiles: 13 (12.62%)

Observation:
- All returned tiles intersect the requested AOI.
- 13 tiles extend beyond the AOI boundary.
- This may be expected behavior for a fixed-grid tiling system.
- Further confirmation is required to determine whether boundary tiles
  are clipped to the AOI or returned as complete grid cells.

### Temperature Field Consistency

- All 103 tiles have identical average_temperature,
  min_temperature, and max_temperature values.
- No tiles have differing values across these three fields.
- This behavior was observed using the default `tcm` analytic type.
- It is unclear whether this is expected behavior or a data
  representation limitation.
- Further clarification from the FortyGuard team is recommended.

### Open Questions

1. Why does the API return a UTC window ending at 23:00
   when the requested local time range is 09:00–17:00 PDT?
   Is the end_time inclusive or exclusive in practice?

2. Does each cell's `value` represent the number of hourly
   observations exceeding the threshold, and how are missing
   hourly observations handled?

### Test 02 – Exceedance

- HTTP status: 200
- Task status: Completed
- Granularity: 100m
- Time range requested: 09:00–17:00
- Threshold: 30°C
- Direction: Above
- Returned cells: 103
- Units: Hours

Validation:
- Minimum, maximum, and mean matched independently
  calculated values.
- No missing values.
- No negative values.
- No values exceeding the requested 8-hour duration.

Observation:
- API returned a UTC window of 16:00–23:00.
- Time window interpretation requires clarification.
- All 103 cells returned valid exceedance values.

### Exceedance Distribution

| Exceedance Hours | Cells | Percentage |
|---|---:|---:|
| 2 | 16 | 15.53% |
| 3 | 67 | 65.05% |
| 4 | 20 | 19.42% |

Observations:
- 65.05% of cells recorded 3 hours of exceedance.
- 19.42% recorded 4 hours.
- 15.53% recorded 2 hours.
- No cells recorded 0 or 1 hour.

The distribution is concentrated around 3 hours.

### Test 03 – Granularity Comparison

| Metric | 100m | 20m |
|---|---:|---:|
| Cells | 103 | 2,530 |
| Minimum | 32.0285°C | 28.3269°C |
| Maximum | 33.3120°C | 29.5989°C |
| Mean | 32.3806°C | 29.1372°C |
| Standard deviation | 0.3263°C | 0.2137°C |

Observations:
- 20m returned approximately 24.56 times more cells.
- Mean temperature differed by approximately 3.24°C.
- The 20m catalog returned substantially lower temperature values.
- Temperature frequency counts summed to 2,530 cells.
- The 20m catalog may use different source data or processing
  methodology from the 100m catalog.

Open questions:
- Are the 20m and 100m catalogs based on different source datasets?
- Are their temperature values directly comparable?
- Does 20m return complete or partial spatial coverage?
- How should users interpret differences between resolutions?

### Test 03 – Spatial Validation (20m)

- Total cells: 2,530
- Valid geometries: 2,530
- Invalid geometries: 0
- Intersecting AOI: 2,530 (100%)
- Fully contained: 2,439 (96.40%)
- Partially overlapping: 91 (3.60%)
- Outside AOI: 0

Observations:
- All returned cells have valid geometries.
- All cells intersect the requested AOI.
- 91 cells extend beyond the AOI boundary.
- Spatial validation results are positive.