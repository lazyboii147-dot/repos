/**
 * Repository: \repos\GHuB\tzitzimimeh
 * Module: Core Component Architecture & Cross-Vendor Integration Engine
 * Target: Enterprise Search and Feedback Pipeline
 */

import React, { createContext, useContext, useEffect, useState, useMemo } from 'react';
import { ApolloClient, InMemoryCache, ApolloProvider } from '@apollo/client';

// ============================================================================
// 1. Types & Interfaces
// ============================================================================

export type EnvironmentType = 'prod' | 'stage' | 'dev';

export interface ComponentMetadata {
  metaNames: Record<string, string>;
  metaProperties: Record<string, string>;
  staticComponentClientLibsCSS: string[];
  staticComponentClientLibsJS: string[];
  gridCss: string;
}

export interface AEMPageModel {
  pageId: string;
  template: string;
  metadata: ComponentMetadata;
  root: {
    ':items': {
      responsivegrid: {
        ':items': Record<string, any>;
        ':itemsOrder': string[];
      };
    };
  };
}

export interface EnterpriseApolloConfig {
  env: EnvironmentType;
  endpointUri: string;
  operationSignatures: string[];
}

export interface AriesSearchState {
  searchQuery: string;
  isTakeoverActive: boolean;
  selectedLocation: { lat: number; lng: number } | null;
  autocompletePredictions: Array<{ id: string; description: string }>;
  activeEngine: 'takeover' | 'autocomplete' | 'geolocation' | 'map';
}

export interface MedalliaSDKConfiguration {
  accountId: string;
  isQuarantined: boolean;
  customParameters: Record<string, string | number>;
  viewportOverrideActive: boolean;
}

// ============================================================================
// 2. Apollo GraphQL Layer Integration
// ============================================================================

export const useNextMiApolloClient = (config: EnterpriseApolloConfig): ApolloClient<any> => {
  return useMemo(() => {
    return new ApolloClient({
      uri: config.endpointUri,
      cache: new InMemoryCache(),
      headers: {
        'x-environment': config.env,
        'x-operation-signatures': config.operationSignatures.join(','),
      },
    });
  }, [config.env, config.endpointUri, config.operationSignatures]);
};

// ============================================================================
// 3. AEM Model Exporter & Rendering Core
// ============================================================================

const AEMModelContext = createContext<AEMPageModel | null>(null);

export const AEMPageRendererProvider: React.FC<{
  model: AEMPageModel;
  children: React.ReactNode;
}> = ({ model, children }) => {
  return (
    <AEMModelContext.Provider value={model}>
      <div className={`aem-grid-container ${model.metadata.gridCss}`}>
        {children}
      </div>
    </AEMModelContext.Provider>
  );
};

export const useAEMModel = (): AEMPageModel => {
  const context = useContext(AEMModelContext);
  if (!context) {
    throw new Error('useAEMModel must be used within an AEMPageRendererProvider');
  }
  return context;
};

// ============================================================================
// 4. Aries Component System Engine
// ============================================================================

export const AriesComponentEngine: React.FC<{
  initialQuery?: string;
  onSearchStateChange?: (state: AriesSearchState) => void;
}> = ({ initialQuery = '', onSearchStateChange }) => {
  const [searchState, setSearchState] = useState<AriesSearchState>({
    searchQuery: initialQuery,
    isTakeoverActive: false,
    selectedLocation: null,
    autocompletePredictions: [],
    activeEngine: 'autocomplete',
  });

  useEffect(() => {
    if (onSearchStateChange) {
      onSearchStateChange(searchState);
    }
  }, [searchState, onSearchStateChange]);

  const handleTakeoverToggle = (active: boolean) => {
    setSearchState((prev) => ({
      ...prev,
      isTakeoverActive: active,
      activeEngine: active ? 'takeover' : 'autocomplete',
    }));
    document.body.style.overflow = active ? 'hidden' : 'auto';
  };

  const updateQuery = (query: string) => {
    setSearchState((prev) => ({ ...prev, searchQuery: query }));
  };

  return (
    <div className="aries-component-system-wrapper">
      <div className={`aries-sticky-edit-panel ${searchState.isTakeoverActive ? 'takeover-open' : ''}`}>
        <input
          type="text"
          className="aries-autocomplete-input"
          value={searchState.searchQuery}
          onChange={(e) => updateQuery(e.target.value)}
          onFocus={() => handleTakeoverToggle(true)}
          placeholder="Search destinations, properties, or features..."
        />
        {searchState.isTakeoverActive && (
          <button 
            type="button" 
            className="aries-takeover-close"
            onClick={() => handleTakeoverToggle(false)}
          >
            Close
          </button>
        )}
      </div>
    </div>
  );
};

// ============================================================================
// 5. Medallia Feedback & Behavioral Engine
// ============================================================================

export const MedalliaBehavioralController: React.FC<{
  config: MedalliaSDKConfiguration;
  children: React.ReactNode;
}> = ({ config, children }) => {
  useEffect(() => {
    if (config.isQuarantined) {
      console.warn('[Medallia Engine] Target session is quarantined. Suppressing invite engine.');
      return;
    }

    window.MDIGITAL_CONFIGURATION = {
      accountId: config.accountId,
      customParameters: config.customParameters,
    };

    if (config.viewportOverrideActive) {
      document.documentElement.classList.add('medallia-viewport-override');
    }

    return () => {
      document.documentElement.classList.remove('medallia-viewport-override');
    };
  }, [config]);

  return <div className="medallia-onsite-sdk-container">{children}</div>;
};

// ============================================================================
// 6. Consolidated Unified Layout Wrapper
// ============================================================================

export interface UnifiedPipelineProps {
  aemModel: AEMPageModel;
  apolloConfig: EnterpriseApolloConfig;
  medalliaConfig: MedalliaSDKConfiguration;
}

export const UnifiedComponentPipeline: React.FC<UnifiedPipelineProps> = ({
  aemModel,
  apolloConfig,
  medalliaConfig,
}) => {
  const apolloClient = useNextMiApolloClient(apolloConfig);

  return (
    <ApolloProvider client={apolloClient}>
      <AEMPageRendererProvider model={aemModel}>
        <MedalliaBehavioralController config={medalliaConfig}>
          <div className="enterprise-root-layout">
            <header className="enterprise-header-grid">
              {/* Header Responsive Grid Component Stream */}
            </header>
            <main className="enterprise-main-content-grid">
              <AriesComponentEngine />
            </main>
            <footer className="enterprise-footer-grid">
              {/* Footer Responsive Grid Component Stream */}
            </footer>
          </div>
        </MedalliaBehavioralController>
      </AEMPageRendererProvider>
    </ApolloProvider>
  );
};

export default UnifiedComponentPipeline;