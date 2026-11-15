# FortyGuard Product Evaluation

**Candidate:** Lam Kim Ngan  
**Position:** Data Engineering Intern  
**Evaluation Scope:** Temperature Dashboard, Temperature API, and FortyGuard Temperature MCP  
**Evaluation Period:** November 2026

## 1. Overview

This repository contains my exploratory evaluation of FortyGuard's urban heat intelligence products.

The evaluation focuses on product usability, API design, data quality, documentation, MCP integration, and potential improvements.

My objective was to explore the products from a data engineering perspective by testing available functionality, inspecting returned data, validating basic data properties, comparing outputs, and documenting observations.

## 2. Products Evaluated

| Product | Evaluation Activities |
|---|---|
| Temperature Dashboard | Explored temperature reports, satellite imagery, geographic analysis, and environmental and urban indicators |
| Temperature API | Tested heatmap generation at different spatial resolutions and exceedance analytics; inspected GeoJSON features and statistical outputs |
| FortyGuard Temperature MCP | Integrated with Codex in Visual Studio Code and tested environmental parameters, heatmap generation, and temperature routing |

## 3. Dashboard Evaluation

The dashboard evaluation focused on report structure, temperature information, satellite imagery, and the presentation of geographic, environmental, and urban indicators.

### Key observations

- The dashboard provides a broad view of urban heat conditions by combining temperature information with geographic and environmental context.
- Satellite imagery provides useful visual context for understanding the physical characteristics of an area.
- Indicators such as impervious surface fraction, Sky View Factor (SVF), and anthropogenic heat flux offer additional dimensions for investigating urban heat.
- Clearer explanations of temperature definitions, data sources, and calculation methods would improve data interpretation.

I also see potential in combining satellite imagery with structured environmental and geographic data for future AI and machine learning applications, including LLM-powered analytical workflows.

Further investigation would be needed to assess the suitability of these datasets for specific model development tasks.

Detailed observations are available in `dashboard/observations.md`.

## 4. API Testing

The API evaluation included three main test scenarios.

### Test 01 – 100m Heatmap

Retrieved temperature data for Downtown Los Angeles and validated:

- Feature count and tile identifiers.
- Temperature fields.
- GeoJSON geometry validity.
- Spatial coverage and AOI intersections.
- Basic data completeness.

### Test 02 – Exceedance

Tested hourly temperature exceedance analytics and inspected:

- Threshold configuration.
- Time windows and timezone interpretation.
- Units and output distributions.
- Returned statistical values.

### Test 03 – 20m Heatmap

Compared the 20m output with the 100m result for the same area and timestamp, examining differences in spatial resolution and temperature statistics.

### Key observations

- Both spatial resolutions returned valid GeoJSON geometries and unique tile identifiers in the tested area.
- The 20m and 100m outputs showed a noticeable difference in average temperature.
- In the tested 100m response, individual tiles returned identical values for `average_temperature`, `min_temperature`, and `max_temperature`.
- The exceedance response raised questions about timezone conversion and hourly window interpretation.
- The tested responses contained complete temperature values and valid geometries.

These findings are documented as observations and questions for clarification rather than confirmed product defects.

Detailed results are available in `api/test_results.md`, with individual response files stored in `api/responses/`.

## 5. MCP Testing

The FortyGuard Temperature MCP server was integrated with the Codex extension in Visual Studio Code through a remote Streamable HTTP connection.

Three workflows were tested:

1. **Environmental parameters:** Used `env_params` to retrieve hourly environmental information for Phoenix, Arizona.
2. **Heatmap generation:** Used `heatmap` and `heatmap_read` to generate and retrieve a heatmap for Downtown Los Angeles.
3. **Temperature routing:** Used `temperature_routing` and `temperature_routing_read` to evaluate thermal exposure along a route in Phoenix.

The MCP heatmap statistics were also compared with the REST API output for the same test scenario. The returned statistics were consistent.

### Additional observation

The MCP documentation described nine tools, while my connected Codex session exposed eleven tools, including `credit_balance` and `monitoring`.

This may reflect differences between the documentation and the currently available tool catalog.

Detailed observations are available in `mcp/observations.md`.

## 6. Repository Structure

```text
fortyguard-evaluation/
├── README.md
├── api/
│   ├── responses/
│   │   ├── exceedance_100m.json
│   │   ├── heatmap_20m.json
│   │   └── heatmap_100m.json
│   ├── compare_granularity.py
│   ├── inspect_exceedance.py
│   ├── test_01_heatmap.py
│   ├── test_02_exceedance.py
│   ├── test_03_heatmap_20m.py
│   ├── test_results.md
│   ├── validate_20m_quality.py
│   ├── validate_20m.py
│   ├── validate_exceedance.py
│   ├── validate_geojson.py
│   ├── validate_heatmap.py
│   ├── validate_spatial_coverage.py
│   └── validate_tile_quality.py
├── dashboard/
│   └── observations.md
├── feedback/
│   └── final_feedback.md
├── mcp/
│   └── observations.md
└── .gitignore
```

### Key Files

| File | Purpose |
|---|---|
| `api/test_results.md` | Summary of API test results and findings |
| `api/test_*.py` | Scripts used to execute API test scenarios |
| `api/validate_*.py` | Scripts for validating response structure, data quality, and spatial coverage |
| `api/compare_granularity.py` | Comparison between 20m and 100m heatmap outputs |
| `api/inspect_exceedance.py` | Inspection of exceedance analytics |
| `dashboard/observations.md` | Dashboard evaluation observations |
| `mcp/observations.md` | MCP integration and testing observations |
| `feedback/final_feedback.md` | Consolidated product evaluation feedback |

## 7. Evaluation Approach

My testing approach included:

- Exploring product functionality and user workflows.
- Inspecting API request and response structures.
- Validating GeoJSON geometry and basic data completeness.
- Checking tile identifiers, duplicate records, and missing values.
- Comparing statistical outputs across spatial resolutions.
- Cross-checking REST API and MCP results.
- Documenting confusing behavior, potential risks, and improvement opportunities.

## 8. Limitations

This was an exploratory evaluation using a limited number of locations, dates, spatial resolutions, and analytical scenarios.

The tests do not establish the overall accuracy of FortyGuard's temperature products or validate all available API and MCP capabilities.

Differences observed between spatial resolutions may be related to their underlying data catalogs and should not be interpreted as evidence of incorrect data without further investigation.

Further testing across additional locations, dates, resolutions, and analytical types would be necessary for a more comprehensive assessment.

## 9. Security

API credentials and authentication tokens are intentionally excluded from this repository.

Environment variables are stored locally and should not be committed to version control.

No API keys, access tokens, or other authentication secrets should be included in public files or repository history.