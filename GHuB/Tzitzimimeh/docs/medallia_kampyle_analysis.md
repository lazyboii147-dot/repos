# Medallia Kampyle Embed Runtime: Impact, PoC, and Remediation

## 1. Impact (Evidence-Only)
- **Dynamic Script Injection:** Automatically provisions and appends external JavaScript resources (JS_SITE_CODE, ONSITE_DATA_PATH) directly into the document body at runtime via window.KAMPYLE_EMBED.kampyleInit().
- **Telemetry & Feedback Endpoints:** Establishes active data-collection connections to external cloud telemetry infrastructures (nalytics-fe.digital-cloud.medallia.com, eedback.digital-cloud.medallia.com).
- **Client-Hint & Environment Profiling:** Harvests detailed browser capabilities, user-agent strings, and client-hints (USER_AGENT_CLIENT_HINTS_LIST) to feed customer experience analytics.

## 2. Non-Exploitive Proof-of-Concept (PoC)
- **Endpoint Enumeration:** Search embed scripts for configuration maps containing DEFAULT_ANALYTICS_SUBMIT_EVENTS_URL and SUBMIT_URL_PREFIX.
- **Loader Verification:** Locate document.createElement("script") execution routines bound to window.load event listeners.

## 3. Prioritized Remediation
- **P0 (Immediate):** Audit all embedded feedback and survey widgets for unauthorized data collection and session interaction tracking.
- **P1 (Short Term):** Enforce strict Content Security Policy (CSP) directives restricting script loading and beacon submissions to approved third-party domains.
- **P2 (Long Term):** Integrate customer feedback and RUM widgets into centralized vendor governance and privacy review workflows.
