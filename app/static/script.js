const questionInput = document.getElementById("question");
const askButton = document.getElementById("askButton");
const chat = document.getElementById("chat");


function addMessage(text, type) {

    const message = document.createElement("div");

    message.className = `message ${type}`;

    const bubble = document.createElement("div");

    bubble.className = "bubble";
    bubble.textContent = text;

    message.appendChild(bubble);
    chat.appendChild(message);

    chat.scrollTop = chat.scrollHeight;

    return message;
}


function showThinking() {

    const message = document.createElement("div");

    message.className = "message assistant";
    message.id = "thinking";

    message.innerHTML = `
        <div class="bubble">
            Thinking...
        </div>
    `;

    chat.appendChild(message);

    chat.scrollTop = chat.scrollHeight;
}


function removeThinking() {

    const thinking = document.getElementById("thinking");

    if (thinking) {
        thinking.remove();
    }
}


async function askQuestion() {

    const question = questionInput.value.trim();

    if (!question) {
        return;
    }

    // Add user's message
    addMessage(question, "user");

    // Clear input
    questionInput.value = "";

    // Disable button while waiting
    askButton.disabled = true;

    // Show loading state
    showThinking();

    try {

        const response = await fetch("/ask", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });


        if (!response.ok) {
            throw new Error("Server error");
        }


        const data = await response.json();

        removeThinking();

        addMessage(data.answer, "assistant");


    } catch (error) {

        removeThinking();

        addMessage(
            "Something went wrong. Please try again.",
            "assistant"
        );

        console.error(error);

    } finally {

        askButton.disabled = false;

        questionInput.focus();

    }
}


/* Ask button */

askButton.addEventListener("click", askQuestion);


/* Enter key */

questionInput.addEventListener("keydown", (event) => {

    if (event.key === "Enter") {
        askQuestion();
    }

});