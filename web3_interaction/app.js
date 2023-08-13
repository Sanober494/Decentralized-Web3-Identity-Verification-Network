document.addEventListener("DOMContentLoaded", () => {
    const verificationForm = document.getElementById("verification-form");
    const verificationResult = document.getElementById("verification-result");
    const transactionButton = document.getElementById("transaction-button");
    const interactionResult = document.getElementById("interaction-result");

    verificationForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const formData = new FormData(verificationForm);
        const passport = formData.get("passport");
        const biometric = formData.get("biometric");

        // Simulate sending verification request to the backend
        const response = await fetch("/verify", {
            method: "POST",
            body: JSON.stringify({ passport, biometric }),
            headers: { "Content-Type": "application/json" }
        });

        const data = await response.json();
        verificationResult.textContent = data.message;
    });

    transactionButton.addEventListener("click", async () => {
        // Simulate sending transaction request to the backend
        const response = await fetch("/transaction", { method: "POST" });
        const data = await response.json();
        interactionResult.textContent = data.message;
    });
});
