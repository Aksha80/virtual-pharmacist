async function sendMessage() {
    const userMessage = document.getElementById("userMessage").value;
    const responseElement = document.getElementById("response");

    if (!userMessage.trim()) {
        responseElement.textContent = "Please enter a message.";
        return;
    }

    try {
        const response = await fetch("http://localhost:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: userMessage })
        });

        const data = await response.json();
        responseElement.textContent = "Response: " + data.response;
    } catch (error) {
        responseElement.textContent = "Error connecting to the chatbot.";
        console.error("Error:", error);
    }
}
