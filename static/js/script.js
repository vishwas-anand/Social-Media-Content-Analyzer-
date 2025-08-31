document.getElementById("uploadForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const fileInput = document.getElementById("fileInput");
    if (!fileInput.files.length) {
        alert("Please select a file first!");
        return;
    }

    let formData = new FormData();
    formData.append("file", fileInput.files[0]);

    let response = await fetch("/", {
        method: "POST",
        body: formData,
    });

    let result = await response.json();

    document.getElementById("outputText").textContent = result.text || "No text extracted.";
    document.getElementById("analysis").textContent = result.analysis || "";
    document.getElementById("recommendation").textContent = result.recommendation || "";

    document.getElementById("result").style.display = "block";
});
