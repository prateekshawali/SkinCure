const chatInput = document.querySelector(".chat-input textarea");
const sendChatBtn = document.getElementById("send-btn");
const chatbox = document.querySelector(".chatbox");

const API_URL = "http://127.0.0.1:5000/"; // Flask URL


const createchatLi = (message, className) => {
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat", className);
    let chatContent = className === "outgoing"
        ? `<p>${message}</p>`
        : `<span class="material-symbols-outlined">smart_toy</span><p>${message}</p>`;
    chatLi.innerHTML = chatContent;
    return chatLi;
};

const scrollToBottom = () => {
    chatbox.scrollTo({
        top: chatbox.scrollHeight,
        behavior: 'smooth'
    });
};

const handleChat = async () => {
    const userMessage = chatInput.value.trim();
    if (!userMessage) return;

    chatbox.appendChild(createchatLi(userMessage, "outgoing"));
    chatInput.value = "";
    scrollToBottom();

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: userMessage })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();

        // ✅ Append the bot response using 'data.response'
        chatbox.appendChild(createchatLi(data.response, "incoming"));
    } catch (error) {
        console.error("Error:", error);
        chatbox.appendChild(createchatLi("Oops! Something went wrong. Please try again.", "incoming"));
    } finally {
        scrollToBottom();
    }
};

sendChatBtn.addEventListener("click", handleChat);
