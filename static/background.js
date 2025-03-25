chrome.runtime.onInstalled.addListener(() => {
    console.log("Extension installed and background script running.");
});

// Listen for messages from popup or content scripts
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "fetch_text") {
        fetch("http://localhost:5000/get_text")
            .then(response => response.text())
            .then(text => sendResponse({ text: text }))
            .catch(error => sendResponse({ error: "Failed to fetch text from server." }));
        return true; // Keep the message channel open for async response
    }
});
