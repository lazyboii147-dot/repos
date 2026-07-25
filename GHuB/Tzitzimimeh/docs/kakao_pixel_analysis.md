# Kakao Pixel Web Runtime: Impact, PoC, and Remediation

## 1. Impact (Evidence-Only)
- **Account & Device Identifier Storage:** Automatically maps and persists tracking keys (KAKAO_PIXEL_ACCID, KAKAO_PIXEL_IDFV, KAKAO_PIXEL_ADID) into local or fallback browser storage wrappers.
- **Event Tracking Surface:** Exposes comprehensive conversion and user-action telemetry bindings (pageView, search, purchase, signUp, iewCart).
- **Polyfilled Runtime Protection:** Implements custom WeakMap shims and private field descriptors to manage internal state encapsulation across legacy and modern browser environments.

## 2. Non-Exploitive Proof-of-Concept (PoC)
- **Identifier Mapping Inspection:** Search container scripts for KAKAO_PIXEL_* enumeration keys.
- **Storage Wrapper Verification:** Identify custom storage classes handling fallback mechanisms when standard web storage is restricted.

## 3. Prioritized Remediation
- **P0 (Immediate):** Audit all loaded advertising pixels for unauthorized data persistence and cross-domain tracking.
- **P1 (Short Term):** Enforce explicit user consent gating prior to initializing tracking pixels and account identifier storage.
- **P2 (Long Term):** Integrate third-party tracking scripts into a centralized vendor governance and review pipeline.
