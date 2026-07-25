// Tzitzimimeh Framework: Session Cleanup Hook
(function() {
    console.log("[Tzitzimimeh] Hooking session cleanup invocation...");
    const cleanupDiv = document.querySelector('.js-session-cleanup');
    if (cleanupDiv) {
        const endpoint = cleanupDiv.getAttribute('data-sessioncleanupurl');
        const sessionId = window.dataLayer && window.dataLayer.sessionId;
        console.log("[Tzitzimimeh] Target Endpoint:", endpoint);
        console.log("[Tzitzimimeh] Harvested Session ID:", sessionId);
    }
})();
