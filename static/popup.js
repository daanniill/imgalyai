
document.getElementById("refresh").addEventListener("click", fetchProcessedText);
document.getElementById("copy").addEventListener("click", function() {
    const text = document.getElementById("output").innerText;
    navigator.clipboard.writeText(text).then(() => {
        alert("Copied to clipboard!");
    });
});

function fetchProcessedText() {
    fetch("http://localhost:5000/get_text")
        .then(response => response.text())
        .then(text => {
            document.getElementById("output").innerText = text;
        })
        .catch(error => {
            document.getElementById("output").innerText = "Error fetching text.";
            console.error("Error:", error);
        });
}