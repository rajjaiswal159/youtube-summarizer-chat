const processBtn = document.getElementById("processBtn");
const sendBtn = document.getElementById("sendBtn");
const questionInput = document.getElementById("question");
const result = document.getElementById("result");

function addMessage(text, type) {

    const div = document.createElement("div");

    div.className = `message ${type}`;

    div.innerHTML = text;

    result.appendChild(div);

    result.scrollTop = result.scrollHeight;

    return div;
}

// Process Video
processBtn.addEventListener("click", async () => {

    result.innerHTML = "";

    addMessage("📹 Processing video...", "ai");

    processBtn.disabled = true;

    try {

        const [tab] = await chrome.tabs.query({
            active: true,
            currentWindow: true
        });

        const response = await fetch("http://127.0.0.1:8000/process", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                video_url: tab.url
            })

        });

        const data = await response.json();

        result.innerHTML = "";

        addMessage(data.message, "ai");

        processBtn.disabled = false;

    }

    catch (error) {

        result.innerHTML = "";

        addMessage("❌ Failed to process video.", "ai");

        processBtn.disabled = false;

    }

});


// Chat
sendBtn.addEventListener("click", async () => {

    if (sendBtn.disabled) return;

    const question = questionInput.value.trim();

    if (!question) return;

    addMessage(question, "user");

    questionInput.value = "";

    sendBtn.disabled = true;

    const thinking = addMessage("🤖 Thinking...", "ai");

    try {

        const response = await fetch("http://127.0.0.1:8000/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });

        const data = await response.json();

        if (data.success) {
            thinking.innerHTML = data.answer;
        } else {
            thinking.innerHTML = `❌ ${data.message}`;
        }

        sendBtn.disabled = false;

    }

    catch (error) {

        thinking.innerHTML = "❌ Error occurred.";

        sendBtn.disabled = false;

    }

});

questionInput.addEventListener("keydown", (event) => {

    if (event.key === "Enter" && !event.shiftKey) {

        event.preventDefault();

        sendBtn.click();
    }

});