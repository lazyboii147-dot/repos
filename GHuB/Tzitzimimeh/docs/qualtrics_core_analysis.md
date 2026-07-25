# Qualtrics SiteIntercept CoreModule & Logic Tree Evaluator Analysis

## 1. Scope of Exposure
- **Client-Side Targeting AST Evaluator:** Full exposure of the abstract syntax tree (AST) evaluation engine (evaluateLogicTree, evaluateComparatorNode, evaluateConjunctionNode), revealing how targeting rules, comparators, and logic types execute entirely in the browser.
- **Frustration Signal Monitoring:** Native tracking of user behavioral friction (RAGE_CLICK, MOUSE_THRASH, ERROR_CLICK, DEAD_CLICK) to trigger dynamic intercepts.
- **Cross-Vendor Telemetry Binding:** Deep integration hooks pulling state directly from Adobe Analytics (SiteCatalystValue) and Google Tag Manager data layers.

## 2. Attack Surface & Exploitation Risks
- **Logic Bypass & Manipulation:** Visibility into client-evaluated conditions allows attackers to spoof search parameters, device types, or history states to intentionally trigger or evade feedback intercepts.
- **Behavioral Profiling Exposure:** Comprehensive tracking of page counts, time on site, and frustration metrics creates a high-sensitivity client-side surveillance footprint.
