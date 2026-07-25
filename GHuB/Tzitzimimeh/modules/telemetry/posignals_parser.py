def parse_posignals_mock():
    print("[*] Parsing POSignals telemetry structure...")
    mock_jwt_payload = {
        "deviceAttributesSerialized": {
            "webGLRenderer": "ANGLE (Intel, Intel(R) Iris(R) Plus Graphics 640)",
            "codecSupport": {"h264": True, "webm": True},
            "mathQuirks": 0.00000011920928955078125
        }
    }
    print("[+] Decoded mock device telemetry attributes successfully.")
    import json
    print(json.dumps(mock_jwt_payload, indent=2))

if __name__ == "__main__":
    parse_posignals_mock()
