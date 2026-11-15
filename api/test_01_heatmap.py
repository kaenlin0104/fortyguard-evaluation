
import os
import requests
import json
import time
from pathlib import Path
from dotenv import load_dotenv

print("Starting FortyGuard Test 01 - Heatmap...")

# 1. Load API key
load_dotenv()
API_KEY = os.getenv("FORTYGUARD_API_KEY")

if not API_KEY:
    raise ValueError("Missing FORTYGUARD_API_KEY")

# 2. API endpoint
url = "https://api.fortyguard.com/v1/heatmap"

headers = {
    "api-key": API_KEY,
    "Content-Type": "application/json"
}

# 3. Request payload
payload = {
    "polygon_aoi": {
        "type": "Polygon",
        "coordinates": [[
            [-118.2500, 34.0400],
            [-118.2400, 34.0400],
            [-118.2400, 34.0500],
            [-118.2500, 34.0500],
            [-118.2500, 34.0400]
        ]]
    },
    "date_time": {
        "start_date": "2024-07-15",
        "start_time": "14:00",
        "filter_type": 1
    },
    "granularity": 100
}

# 4. Submit request
response = requests.post(
    url,
    headers=headers,
    json=payload,
    timeout=60
)

print("HTTP Status:", response.status_code)
print("Response:", response.text)

response.raise_for_status()

# 5. Extract activity ID
activity_id = response.json()["data"]["activity_id"]
print("Activity ID:", activity_id)

# 6. Check task status
status_url = f"https://api.fortyguard.com/v1/status/{activity_id}"

for attempt in range(120):
    status_response = requests.get(
        status_url,
        headers={"api-key": API_KEY},
        timeout=60
    )

    status_response.raise_for_status()
    status_data = status_response.json()["data"]
    status = status_data["status"].lower()

    print(f"Attempt {attempt + 1}: {status}")

    if status in ("completed", "succeeded"):
        print("Heatmap generation completed!")

        result = status_response.json()

        output_dir = Path("api/responses")
        output_dir.mkdir(parents=True, exist_ok=True)

        output_file = output_dir / "heatmap_100m.json"

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(result, file, indent=4, ensure_ascii=False)

        print(f"Response saved to: {output_file}")
        break

    elif status in ("failed", "error"):
        raise RuntimeError(status_response.text)

    time.sleep(5)

else:
    raise TimeoutError("Task did not complete within 10 minutes.")
