# Dynatrace RUM Bootstrap: Impact, PoC, and Remediation

## 1. Impact (Evidence-Only)
- **High-Sensitivity Telemetry Ingestion:** RUM scripts automatically map internal dataLayer attributes (session identifiers, loyalty levels, authentication states, financial revenues, and search criteria) into monitoring metadata.
- **Native API Instrumentation:** Intercepts native event listeners and overrides performance timing objects (performance.timeOrigin, performance.now()), increasing execution footprint.
- **Client-Side Cookie Mutation:** Dynamically sets and clears tracking cookies (__dTCookie) directly within the browser execution context.

## 2. Non-Exploitive Proof-of-Concept (PoC)
- **Metadata Mapping Inspection:** Search bootstrap bundles for mdcc* = bdataLayer.* declarations.
- **Cookie Logic Verification:** Locate explicit __dTCookie creation and expiration strings.

## 3. Prioritized Remediation
- **P0 (Immediate):** Review monitoring metadata ingestion rules; strip session tokens, loyalty points, and financial metrics from telemetry payloads.
- **P1 (Short Term):** Enforce strict consent gating before initializing RUM bootstrap execution.
- **P2 (Long Term):** Establish a centralized telemetry governance framework to audit all third-party monitoring and analytics vendors for data minimization compliance.
