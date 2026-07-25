# Qualtrics Target Display Engine & Utility Layer Analysis

## 1. Scope of Exposure
- **Display & Suppression Control:** Full exposure of client-side suppression logic (shouldPreventRepeatedDisplay, QSI_<id>_intercept), governing how survey frequency capping and expiration cookies operate.
- **Impression & Click Telemetry:** Comprehensive tracking of user interactions via sendStat, logging brand identifiers, directory IDs, and distribution tokens directly to remote servers.
- **Dynamic JavaScript & Action Execution:** Exposure of unJavaScriptAction and evalJS routines, enabling custom script evaluation and client-side cookie manipulation upon intercept triggering.

## 2. Attack Surface & Exploitation Risks
- **Intercept Spoofing & Manipulation:** Visibility into DOM measurement, positioning, and localStorage history (Q_INTER) allows attackers to force, suppress, or spoof survey renders.
- **Arbitrary Execution Vector:** Exposing the creative action engine introduces high-risk client-side execution surfaces where malicious modifications can alter UI components or inject tracking telemetry.
