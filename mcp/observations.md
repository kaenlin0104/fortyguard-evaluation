# FortyGuard MCP Evaluation

## Test 01 – Environmental Parameters (`env_params`)

**Status:** Successful

**Request**
- Location: Phoenix, Arizona, USA
- Coordinates: 33.4484, -112.074
- Date: 2025-09-20
- Reference temperature: 35°C
- Filter: `filter_type: 3` (single day)

**Execution**
- Returned status: `ok`
- Time coverage: 24 hourly timestamps
- Timezone: `America/Phoenix` (UTC−07:00)
- Credits consumed: 2,900

**First-hour snapshot (00:00 local time)**

| Parameter | Value |
|---|---:|
| Apparent temperature | 34.0°C |
| Relative humidity | 54.2% |
| Precipitation | 0.0 mm |
| Cloud cover | 0 octas |
| Wet-bulb temperature | 23.2°C |
| Elevation | 333 m |
| US AQI | 53.1 |

**Derived metric**
- Heat index: 42.4°C, calculated using the supplied 35°C reference temperature and returned humidity.

**Modeled estimates**
- GHI: 514.67 W/m²
- DNI: 712.88 W/m²
- DHI: 74.61 W/m²
- Clear-sky solar irradiance estimates averaged over daytime hours.

**Hourly variation**
- Apparent temperature: 28.8–39.7°C
- Relative humidity: 24.9–59.4%

**Observations**
- The MCP call succeeded and returned structured environmental data.
- The tool returned 24 hourly timestamps for a single-day request.
- The `parameters` object represents the first-hour snapshot, not the daily average.
- The output includes measured/reported environmental parameters, derived metrics, and modeled estimates. These should be clearly distinguished.
- The result provided useful temporal and environmental context.

**Evaluation status:** Passed initial functional test. Further validation against independent data sources has not yet been performed.

## Test 03 – Temperature-aware Routing

**Status:** Successfully completed

**Request**
- Origin: Phoenix, Arizona, USA (33.4484, -112.074)
- Destination: Phoenix, Arizona, USA (33.4500, -112.060)
- Departure time: 2025-09-20T14:00:00-07:00

**Execution**
- Submission tool: `temperature_routing`
- Read tool: `temperature_routing_read`
- Activity ID: `c9b887c1-0fa5-45fe-b5d0-a5d06c2dd1c8`
- Submission cost: 3,500 credits
- Read cost: 0 credits
- Final status: completed

**Route result**

| Metric | Result |
|---|---:|
| Candidate routes in metadata | 3 |
| Distinct routes returned | 1 |
| Selected routes | 1 |
| Distance | 1.865 km |
| Duration | 2.46 minutes |
| Mean thermal exposure | 41.935°C |
| Time-weighted temperature | 41.936°C |
| Distance-weighted temperature | 41.935°C |
| Peak temperature | 41.95°C |
| Segment temperature range | 41.89–41.95°C |
| Time above 32°C | 2.46 minutes |
| Degree-minutes above threshold | 24.42 |

**Selection metadata**
- Score: 10
- `no_cooling_available: true`
- `has_balanced: false`

**Observations**
- The asynchronous routing submission and retrieval workflow completed successfully.
- Only one distinct route was returned, despite metadata indicating three candidates.
- No separate route alternatives were available for comparison.
- Thermal exposure metrics and selection metadata were returned.
- The read operation consumed no additional credits.
- The meaning of the selection score and cooling/balanced flags requires further documentation.

**Evaluation status:** Passed functional test. Route diversity and selection logic remain open questions.