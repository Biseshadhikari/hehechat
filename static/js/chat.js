const username = JSON.parse(document.getElementById('json-username').textContent);
const message_username = JSON.parse(document.getElementById('json-message-username').textContent);
const chatmessagesubmit = document.getElementById('chatMessageSubmit');
const messageInput = document.querySelector('#messageInput');
const typingIndicator = document.querySelector('#isTypingIndicator'); // Add this line

let typingTimeout=1000;

const socket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + username
    + "/"
);

socket.onopen = (e) => {
    console.log("connection established");
}

socket.onclose = (e) => {
    console.log(e);
}

socket.onmessage = (e) => {
    const data = JSON.parse(e.data);

    if (data.type == "message") {

        if (data.username == message_username) {
            document.querySelector('#messagearea').innerHTML += `
            <div class="flex items-end justify-end mb-4">
                        <div class="bg-green-500 p-3 rounded-lg text-white">
                            <p>${data.message}</p>
                            <p class="text-xs">10:32 AM</p>
                        </div>
            </div>
            `;
        }
        else {
            document.querySelector('#messagearea').innerHTML += `
            <div class="flex items-start mb-4">
                        <div class="bg-gray-300 p-3 rounded-lg">
                            <p>${data.message}</p>
                            <p class="text-xs text-gray-500">10:30 AM</p>
                        </div>
            </div>
            `;
        }
    }

    // Add the following code inside the socket.onmessage event to handle the "typing" messages
    if (data.type == "typing") {
        if (data.message === "") {
            // Empty message indicates no typing, so clear the typing indicator
            typingIndicator.classList.add('hidden')
            typingIndicator.textContent = "";
        } else {
            // Display the typing indicator
            if (data.username != message_username) {
                typingIndicator.classList.remove('hidden')
                typingIndicator.textContent = data.message;
            }
        }
    }
};

chatmessagesubmit.addEventListener('submit', (e) => {
    e.preventDefault();
    const message_input = document.querySelector('#messageInput');
    
    const message = message_input.value;
    if (message == ""){ 
        return
    }
    else{ 
        socket.send(JSON.stringify({
            'type': "message",
            'message': message,
            'username': message_username
        }));
        message_input.value = '';
    }
    
});

messageInput.addEventListener('input', () => {
    // Clear existing timeout if user continues typing
    clearTimeout(typingTimeout);

    // Send "typing" message to the server
    socket.send(JSON.stringify({
        'type': "typing",
        'message': `${message_username} is typing`,
        'username': message_username
    }));

    // Set timeout to clear "is typing" message after 2 seconds of inactivity
    typingTimeout = setTimeout(() => {
        socket.send(JSON.stringify({
            'type': "typing",
            'message': "", // Empty message to indicate no typing
            'username': message_username
        }));
    }, 1000);
});
