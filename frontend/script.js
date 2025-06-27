document.addEventListener('DOMContentLoaded', () => {
    // --- DOM Elements ---
    const fileInput = document.getElementById('file-input');
    const analyzeButton = document.getElementById('analyze-button');
    const dropZone = document.getElementById('drop-zone');
    const uploadContainer = document.getElementById('upload-container');
    
    // UI States
    const promptState = document.getElementById('prompt-state');
    const filePreviewState = document.getElementById('file-preview-state');
    const fileNameSpan = document.getElementById('file-name');
    const removeFileButton = document.getElementById('remove-file-button');
    
    // Results & Loading
    const skeletonLoader = document.getElementById('skeleton-loader');
    const resultsContainer = document.getElementById('results-container');
    const resultsHeader = document.getElementById('results-header');
    const errorMessageDiv = document.getElementById('error-message');
    const startOverButton = document.getElementById('start-over-button');

    const API_URL = 'http://127.0.0.1:8000/analyze/';
    let selectedFile = null;

    // --- State Management Functions ---

    const resetToInitialState = () => {
        selectedFile = null;
        fileInput.value = '';
        
        uploadContainer.classList.remove('hidden');
        promptState.classList.remove('hidden');
        filePreviewState.classList.add('hidden');
        analyzeButton.disabled = true;

        resultsContainer.innerHTML = '';
        resultsHeader.classList.add('hidden');
        skeletonLoader.classList.add('hidden');
        errorMessageDiv.classList.add('hidden');
    };

    const handleFileSelect = (file) => {
        if (!file) return;

        const fileName = file.name.toLowerCase();
        const isAllowed = fileName.endsWith('.csv') || fileName.endsWith('.xlsx');

        if (!isAllowed) {
            displayError('Invalid file type. Please upload a CSV or XLSX file.');
            resetToInitialState();
            return;
        }
        
        selectedFile = file;
        fileNameSpan.textContent = file.name;
        promptState.classList.add('hidden');
        filePreviewState.classList.remove('hidden');
        analyzeButton.disabled = false;
        errorMessageDiv.classList.add('hidden');
    };

    const displayError = (message) => {
        errorMessageDiv.textContent = message;
        errorMessageDiv.classList.remove('hidden');
    };

    const displayResults = (result) => {
        resultsContainer.innerHTML = '';
        
        if (result.message || !result.charts || result.charts.length === 0) {
            const message = result.message || 'No suitable charts could be generated for this dataset.';
            resultsContainer.innerHTML = `<div class="empty-state"><p>${message}</p></div>`;
            return;
        }

        result.charts.forEach((chart, index) => {
            const chartCard = document.createElement('div');
            chartCard.className = 'chart-card';
            chartCard.style.animationDelay = `${index * 100}ms`;

            const title = document.createElement('h3');
            title.textContent = chart.title;

            const img = document.createElement('img');
            img.src = `data:image/png;base64,${chart.image_base64}`;
            img.alt = chart.title;

            chartCard.appendChild(title);
            chartCard.appendChild(img);
            resultsContainer.appendChild(chartCard);
        });
    };
    
    // --- Event Listeners ---
    
    dropZone.addEventListener('click', () => fileInput.click());
    fileInput.addEventListener('change', (e) => handleFileSelect(e.target.files[0]));

    removeFileButton.addEventListener('click', (e) => {
        e.stopPropagation();
        resetToInitialState();
    });
    
    startOverButton.addEventListener('click', resetToInitialState);

    // Drag & Drop
    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('drag-over');
    });
    dropZone.addEventListener('dragleave', () => dropZone.classList.remove('drag-over'));
    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.classList.remove('drag-over');
        handleFileSelect(e.dataTransfer.files[0]);
    });

    // Main Analysis Logic
    analyzeButton.addEventListener('click', async () => {
        if (!selectedFile) return;

        uploadContainer.classList.add('hidden');
        skeletonLoader.classList.remove('hidden');
        errorMessageDiv.classList.add('hidden');

        const formData = new FormData();
        formData.append('file', selectedFile);

        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                body: formData,
            });

            const result = await response.json();
            if (!response.ok) throw new Error(result.detail || 'An unknown error occurred on the server.');
            
            skeletonLoader.classList.add('hidden');
            resultsHeader.classList.remove('hidden');
            displayResults(result);

        } catch (error) {
            console.error('Analysis failed:', error);
            skeletonLoader.classList.add('hidden');
            uploadContainer.classList.remove('hidden');
            displayError(error.message);
        }
    });

    resetToInitialState();
});