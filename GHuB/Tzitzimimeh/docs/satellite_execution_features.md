# Advanced _satellite Execution Engine & Feature Matrix

## 1. Core _satellite Runtime Architecture
The tag manager execution layer relies on the global window._satellite object to coordinate container lifecycles, data element lookups, script injections, and cookie/storage interactions.

## 2. Key Execution & Feature Capabilities
- **Dynamic Script Registration (__registerScript):** Programmatically registers and injects external or inline JavaScript assets into the runtime DOM outside standard application build pipelines.
- **Data Element Binding (getVar / setVar):** Evaluates, retrieves, and mutates dynamic data elements mapped from global scopes, cookies, data layers, or custom code functions.
- **Diagnostic Logging (_satellite.logger):** Intercepts execution states, consent flags, and cookie storage objects, emitting telemetry directly to browser developer consoles.
- **Cookie & Storage Interfacing (_satellite.cookie):** Direct abstraction layer for reading, writing, and evaluating consent-sensitive storage elements (e.g., OptanonConsent).

## 3. Supply-Chain & Execution Risks
- **Opaque Runtime Modification:** Methods like __registerScript execute third-party payloads without Subresource Integrity (SRI) or content security policy restrictions.
- **State Pollution:** Dynamic variable assignment via setVar can overwrite context boundaries, altering downstream telemetry and third-party event forwarding payloads.
