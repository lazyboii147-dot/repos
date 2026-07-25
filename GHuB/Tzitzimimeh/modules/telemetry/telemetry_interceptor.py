import json

def intercept_alloy_payload(payload_dict):
    print("[*] Intercepting Adobe Alloy telemetry payload structure...")
    events = payload_dict.get("data", {}).get("__adobe", {}).get("analytics", {}).get("events", "")
    print(f"[+] Detected telemetry events vector: {events}")
    return events

if __name__ == "__main__":
    sample = {"data": {"__adobe": {"analytics": {"events": "event341,event344=1000"}}}}
    intercept_alloy_payload(sample)
