# Aries Subsystem & Component Mapper: P0 Supply-Chain Exposure Analysis

## 1. Scope of Exposure
- **Complete Search Subsystem Disclosure:** Publicly accessible Webpack module maps expose the entire internal dependency tree for core search components, including horizontal search forms, autocomplete handlers, and property code lookup logic.
- **Geolocation & Mapping Integration:** Full exposure of GoogleApiWrapper, geocoding parameters, latitude/longitude parsing routines, and map marker stylings.
- **Internal Constants and Feature Toggles:** Comprehensive disclosure of internal viewports, event bindings, navigation speeds, and routing feature flags.

## 2. Attack Surface & Exploitation Risks
- **Search Engine Reverse Engineering:** Complete visibility into internal file paths and module structures allows attackers to map exact execution flows and construct precise malicious autocomplete or geocoding payloads.
- **State and Storage Manipulation:** Exposure of internal storage handlers (localStorageFallback, RecentSearchApi) and eventing architecture (PubSub, subscribeDOMEvents) enables deep analysis of client-side state persistence.
