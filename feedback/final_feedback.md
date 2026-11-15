# FortyGuard Product Evaluation Feedback

**Evaluator perspective:** New Customer / Product Evaluation  
**Products evaluated:** Temperature Dashboard, Temperature API, and FortyGuard MCP

## 1. Overall Impression

My overall impression of FortyGuard is positive. The platform offers an interesting approach to urban heat intelligence by combining temperature information with environmental, geographic, urban, and anthropogenic factors.

What I find particularly valuable is that FortyGuard goes beyond presenting temperature values. It attempts to provide context about why certain locations may experience different heat conditions and how that information can support decision-making.

I evaluated the three products from the perspective of a new customer, focusing on usability, data interpretation, technical accessibility, and consistency across interfaces.

The following are my observations and suggestions based on the tests I performed.

---

## 2. Temperature Dashboard

### What I liked

The Dashboard provides a broad perspective on urban heat conditions. Its reports cover several dimensions, including:

- Geographic Analysis
- Environmental Factors
- Urban Factors
- Events Analysis
- Anthropogenic Factors

I found this structure useful because urban heat is influenced by multiple interacting factors. Presenting these dimensions together gives users more context than a temperature value alone.

The inclusion of indicators such as impervious surface fraction, Sky View Factor (SVF), Mean Radiant Temperature (MRT), and anthropogenic heat flux also makes the report potentially valuable for users interested in urban planning and environmental analysis.

### Areas for improvement

**1. Temperature definition and interpretation**

In my evaluation, a report for Downtown Los Angeles displayed a temperature of 34.08°C (93.36°F) for January 20, 2022, at 00:00.

The report also included an Open-Meteo reanalysis comparison for the same date, with a mean of 56.4°F, a maximum of 72.6°F, and a minimum of 44.8°F.

The difference was substantial. As a new user, I could not immediately determine whether the FortyGuard temperature represented ambient air temperature, land surface temperature, or another temperature metric.

I recommend making the temperature definition, data source, and measurement or modeling methodology more explicit.

**2. Distinguishing measured data from estimates**

The report contains several environmental and urban indicators that appear to involve estimation or modeling.

It would be helpful to distinguish clearly between:
- Directly measured or sourced observations.
- Model-generated estimates.
- Derived indicators.
- Reference or calibration values.

This would help users understand how much confidence to place in each result.

**3. Reference periods and assumptions**

Some indicators appear to involve different reference periods or hypothetical and calibration baselines.

Providing clearer explanations of these assumptions would make the report easier to interpret and reduce the risk of users comparing values that are not directly comparable.

### Dashboard assessment

The Dashboard has strong potential as an urban heat intelligence product. Its breadth of analysis is valuable, but greater transparency around temperature definitions, data provenance, and estimation methods would improve user confidence.

---

## 3. Temperature API

### What I liked

The API provides a structured way to retrieve temperature information for geographic areas and different analytical purposes.

I tested three scenarios:

1. Heatmap at 100m granularity.
2. Exceedance analysis at 100m granularity.
3. Heatmap at 20m granularity.

The API returned structured GeoJSON data and statistical summaries, allowing me to perform additional validation using Python.

For the 100m heatmap test, I received 103 cells. All had unique tile IDs, valid geometries, and non-missing temperature fields.

For the 20m heatmap test, I received 2,530 cells, also with unique IDs, valid geometries, and complete temperature fields.

I appreciated that the API supports different analytical types rather than only returning temperature snapshots.

### Areas for improvement

**1. Temperature consistency across spatial resolutions**

One of the most notable findings was the difference between the 20m and 100m heatmap results for the same area and time.

| Metric | 100m | 20m |
|---|---:|---:|
| Number of cells | 103 | 2,530 |
| Mean temperature | 32.38°C | 29.14°C |
| Minimum | 32.03°C | 28.33°C |
| Maximum | 33.31°C | 29.60°C |

The mean temperature differed by approximately 3.24°C.

I understand that the 20m and 100m products may use separate catalogs or methodologies. Therefore, I cannot conclude that either result is incorrect.

However, I would appreciate clearer documentation explaining the differences between these catalogs, their underlying sources, and whether their outputs are intended to be directly comparable.

**2. Temporal interpretation**

In the Exceedance test, I requested a time range from 09:00 to 17:00 local time.

The returned metadata represented the processing window in UTC, from 16:00 to 23:00, with an inclusive end indicator.

The result may be consistent with hourly observations from 09:00 through 16:00 local time, but the relationship between the requested end time and the returned observation window was not immediately obvious.

I recommend documenting how time ranges, hourly observations, end-time inclusivity, and timezone conversions are handled.

**3. Output metadata**

The API returned useful statistical information and GeoJSON features.

Additional metadata about catalog sources, spatial resolution, tile counts, timestamps, and processing methodology would make the results easier to validate and integrate into downstream data pipelines.

### API assessment

The API was technically accessible and returned structured data suitable for programmatic processing.

My main recommendation is to improve documentation around data provenance, spatial-resolution differences, and temporal interpretation. These details are particularly important for customers building analytical pipelines on top of the API.

---

## 4. FortyGuard MCP

### What I liked

The MCP integration was straightforward to configure in OpenAI Codex.

After connecting the remote MCP server, Codex successfully discovered 11 tools, including environmental parameters, heatmaps, reports, satellite and street-view analysis, routing, monitoring, and credit balance.

The ability to interact with FortyGuard through natural-language requests is a useful addition. Instead of manually constructing REST API requests, users can ask an AI agent to select and invoke the appropriate capability.

I tested three workflows.

**Test 1 – Environmental Parameters**

- Successfully retrieved environmental conditions for Phoenix, Arizona.
- Returned 24 hourly timestamps for a single-day request.
- Included apparent temperature, humidity, precipitation, wet-bulb temperature, AQI, and solar irradiance estimates.
- Reported a cost of 2,900 credits.

I particularly appreciated the combination of hourly environmental information and derived metrics.

One important distinction is that the returned parameters represented the first-hour snapshot, while the hourly series covered the entire day. The heat index was also a derived metric rather than a separate direct measurement.

**Test 2 – Asynchronous Heatmap**

- Successfully submitted a heatmap request.
- Retrieved the completed result using the corresponding activity ID.
- The read operation consumed zero additional credits.

The MCP statistics matched the REST API results for the same polygon, date, time, and granularity.

This was a particularly positive finding because it demonstrated consistency between the two interfaces in my test.

**Test 3 – Temperature-aware Routing**

- Successfully submitted and retrieved a routing request.
- Returned a route of 1.865 km with a travel duration of 2.46 minutes.
- Included mean and peak thermal exposure metrics.
- Reported the time spent above a specified temperature threshold.

The workflow completed successfully, although only one distinct route was returned.

### Areas for improvement

**1. Tool catalog documentation**

The MCP documentation describes nine tools, but my Codex client discovered eleven.

The additional tools were:
- `credit_balance`
- `monitoring`

This may reflect additional capabilities available to my account or documentation that has not yet been updated.

It would be helpful to keep the documented tool catalog aligned with the tools actually exposed to clients.

**2. Routing alternatives and selection logic**

The routing response indicated three candidate routes but returned only one distinct route.

As a result, I could not compare alternatives based on travel time and thermal exposure.

The returned metadata also included fields such as `score`, `no_cooling_available`, and `has_balanced`.

More detailed explanations of these fields and the route selection methodology would help users understand why a particular route was selected.

**3. Result detail and metadata**

The MCP heatmap result included minimum, maximum, mean, and standard deviation, but did not include the cell count or additional metadata available in the REST API response.

Providing more detailed output, or making important metadata consistently accessible through the MCP read tools, would improve the experience for users who need to validate results.

**4. AI interpretation and transparency**

Since MCP is designed for AI clients, it is important that the returned information clearly distinguishes:
- Observed environmental values.
- Derived metrics.
- Model-generated estimates.
- Missing or unavailable information.

This would help AI agents explain results more accurately and avoid presenting estimates as direct measurements.

### MCP assessment

The MCP integration worked well in my initial tests. I was able to connect Codex, discover tools, execute direct requests, and complete asynchronous workflows.

The successful consistency check between MCP and REST API was particularly encouraging.

Further improvements to tool documentation, routing alternatives, and output metadata would make the integration more useful for AI-driven workflows.

---

## 5. Recommendations and Priorities

Based on my evaluation, I would suggest the following improvements:

| Priority | Recommendation | Product |
|---|---|---|
| High | Clarify temperature definitions and data provenance | Dashboard |
| High | Explain differences between 20m and 100m catalogs | API |
| High | Clarify timezone and temporal-window semantics | API |
| Medium | Keep documented MCP tools aligned with the actual catalog | MCP |
| Medium | Provide clearer routing alternatives and selection explanations | MCP |
| Medium | Improve metadata availability in MCP results | MCP |
| Medium | Clearly distinguish measured, derived, and modeled values | All products |

---

## 6. Final Thoughts

I found FortyGuard to be an interesting product ecosystem with potential applications in urban planning, environmental analysis, infrastructure, and heat-risk assessment.

The strongest aspect, in my opinion, is the combination of multiple data dimensions and the availability of different interfaces for different users:

- The Dashboard provides accessible, report-oriented analysis.
- The API supports programmatic integration and custom data workflows.
- MCP makes these capabilities accessible through AI assistants and agent-based applications.

My evaluation was conducted using a limited number of locations, dates, and test scenarios. Therefore, the observations above should be considered initial product feedback rather than a comprehensive validation of the underlying datasets or models.

Overall, I see strong potential in the platform. Improving data transparency, documentation, and consistency of information across the three interfaces would make it easier for new customers and technical users to understand, trust, and integrate FortyGuard's capabilities.

Thank you for providing access to the products and the opportunity to explore them. I appreciated the opportunity to evaluate FortyGuard from a new customer's perspective.