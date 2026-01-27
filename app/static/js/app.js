/**
 * RealityLens Frontend
 * State-based rendering for robust UI updates
 */

document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const dom = {
        form: document.getElementById('analysis-form'),
        input: document.getElementById('query-input'),
        loading: document.getElementById('loading-indicator'),
        resultsGrid: document.getElementById('results-grid'), // New
        results: {
            logician: document.getElementById('card-logician'),
            historian: document.getElementById('card-historian'),
            profiler: document.getElementById('card-profiler')
        }
    };

    // State Store
    const state = {
        status: 'idle',
        results: {
            logician: null,
            historian: null,
            profiler: null
        }
    };

    // Update Card Helper
    function updateCard(cardElement, content, delay) {
        if (content) {
            cardElement.innerHTML = content;
            cardElement.style.animationDelay = delay;
        }
    }

    // Button Element
    const submitButton = dom.form.querySelector('button');

    // Loading Template Generator
    // Loading Template Generator
    const getLoadingTemplate = (text) => {
        const letters = text.split('').map(char => `<span class="loading-text-words">${char === ' ' ? '&nbsp;' : char}</span>`).join('');
        return `
            <div class="flex flex-col items-center pt-8 w-full">
                <div class="loading-text">
                    ${letters}
                </div>
            </div>
        `;
    };

    // Render Function
    function render() {
        // Always reveal grid if purely not idle (active or loading)
        if (state.status !== 'idle') {
            // We removed the global loader requirement, so we just show the grid
            dom.loading.classList.add('hidden'); // Ensure global loader is OFF
            dom.resultsGrid.classList.add('visible'); // Show grid immediately
        }

        // Update Button Text
        if (state.status === 'loading') {
            submitButton.textContent = 'ANALYZING...';
        } else {
            submitButton.textContent = 'ANALYZE';
        }
    }

    // Actions
    async function startAnalysis(query) {
        if (!query) return;

        // Reset State
        state.status = 'loading';

        // Inject Loading State into Cards
        dom.results.logician.innerHTML = getLoadingTemplate('FINDING LOGIC...');
        dom.results.historian.innerHTML = getLoadingTemplate('SEARCHING HISTORY...');
        dom.results.profiler.innerHTML = getLoadingTemplate('CHECKING PROFILE...');

        render();

        try {
            // Connect SSE
            const eventSource = new EventSource(`/stream?q=${encodeURIComponent(query)}`);

            eventSource.onmessage = (event) => {
                try {
                    const data = JSON.parse(event.data);

                    // Update State based on event
                    if (data.agent_name && state.results.hasOwnProperty(data.agent_name)) {
                        if (state.status === 'loading') {
                            state.status = 'active'; // Switch to active on first real data
                            render();
                        }

                        // Replace content for the specific agent
                        updateCard(dom.results[data.agent_name], data.html_payload, '0s');
                    }
                } catch (e) {
                    console.error("Stream parse error", e);
                }
            };

            eventSource.addEventListener('done', () => {
                eventSource.close();
                state.status = 'idle'; // Reset to idle (or keep active?) 
                // Keeping it active keeps the grid visible. 
                // Let's just reset button text.
                submitButton.textContent = 'ANALYZE';
            });

            eventSource.onerror = () => {
                console.error("SSE Error");
                eventSource.close();

                // Show graceful error in cards
                const errorMsg = "<p class='text-[#C5A059]'>Analysis engine temporarily unavailable.</p>";
                dom.results.logician.innerHTML = errorMsg;
                dom.results.historian.innerHTML = errorMsg;
                dom.results.profiler.innerHTML = errorMsg;

                state.status = 'idle'; // Reset
                submitButton.textContent = 'ANALYZE';
            };
        } catch (err) {
            console.error("Fetch setup error", err);
        }
    }

    // Event Listeners
    dom.form.addEventListener('submit', (e) => {
        e.preventDefault();
        startAnalysis(dom.input.value.trim());
    });
});
