async function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    document.getElementById("chat-box").innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
    
    const response = await fetch(`/starcoder?question=${encodeURIComponent(userInput)}`);
    const data = await response.json();
    document.getElementById("chat-box").innerHTML += `<p><strong>LaMini:</strong> ${data.result}</p>`;
}
