# Akamai Bot Manager & Clientlib Dispatcher Protection Analysis

## 1. Edge Security & Bot Scoring Mechanics
- **Bot Manager Integration:** The presence of _abck, m_s, and m_sz cookies indicates aggressive client-side behavioral evaluation and bot scoring enforced at the edge CDN layer.
- **Cooldown Penalties:** HTTP 403 responses coupled with extended Retry-After headers (e.g., 28,800 seconds) establish strict rate-limiting and temporary IP/session cooling penalties for automated traversal attempts.
- **Device & Geo Fingerprinting:** EdgeScape geolocation metadata (rowser-akamai-loc-*) and Device Characteristic Cookies (DCC) supply granular environment telemetry to evaluate request legitimacy.

## 2. Front-End Security Posture Inconsistency
- **Asymmetric Exposure:** While tertiary analytics SDKs and search component source maps remain publicly accessible, core AEM clientlib directories (/etc/clientlibs/*) are heavily guarded by dispatcher filter rules and WAF heuristics, revealing an inconsistent security baseline across the client-side architecture.
