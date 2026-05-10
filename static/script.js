async function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();

    if (!message) return;

    const chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += `<div class="message user">${message}</div>`;
    input.value = "";

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        const data = await response.json();

        chatBox.innerHTML += `<div class="message bot">${data.reply}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (error) {
        chatBox.innerHTML += `<div class="message bot">Error connecting</div>`;
    }
}