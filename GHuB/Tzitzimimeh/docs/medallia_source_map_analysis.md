# Medallia / Kampyle Source Map Exposure: P0 Impact Analysis

## 1. Scope of Exposure
- **Complete Module Tree Disclosure:** Public availability of source maps exposes proprietary internal architecture, including constant definitions, targeting engines, screen capture mechanics, and analytics routing.
- **Hard-coded Default Configuration:** Exposes internal account identifiers, website IDs, default regional endpoints, and fallback evaluation rules.
- **Targeting & Decision Logic:** Full disclosure of behavioral and page-level targeting rules, enabling potential bypasses or targeted manipulation of feedback triggers.

## 2. Supply-Chain & Attack Surface Risks
- **Runtime Reverse Engineering:** Attackers can fully map internal SDK mechanics to identify DOM injection points, iframe interaction flaws, and postMessage trust boundaries.
- **Feature Flag Abuse:** Exposure of feature toggles and WCAG/CSP logic allows precise tuning of malicious payloads against client-side defenses.
