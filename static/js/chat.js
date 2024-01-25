const username = JSON.parse(document.getElementById('json-username').textContent)
const message_username = JSON.parse(document.getElementById('json-message-username').textContent)
const chatmessagesubmit = document.getElementById('chatMessageSubmit')

const socket = new WebSocket(
    'ws://'
    +window.location.host
    +'/ws/'
    +username
    +"/"
);
socket.onopen = (e)=> {
        console.log("connection established")
}
socket.onclose = (e)=> {
    console.log(e)
}
socket.onmessage = (e)=> {
    // console.log(JSON.parse(e.data))
    const data = JSON.parse(e.data)
    console.log(data)
    if (data.username == message_username ){ 
        document.querySelector('#messagearea').innerHTML += `
        <div class="flex items-end justify-end mb-4">
                    <div class="bg-green-500 p-3 rounded-lg text-white">
                        <p>${data.message}</p>
                        <p class="text-xs">10:32 AM</p>
                    </div>
        </div>
        `
    }
    else{ 
        document.querySelector('#messagearea').innerHTML += `
        <div class="flex items-start mb-4">
                    <div class="bg-gray-300 p-3 rounded-lg">
                        <p>${data.message}</p>
                        <p class="text-xs text-gray-500">10:30 AM</p>
                    </div>
        </div>
        `
    }
}
chatmessagesubmit.addEventListener('submit',(e)=> {
    e.preventDefault()
    const message_input = document.querySelector('#messageInput')
    const message = message_input.value;
    socket.send(JSON.stringify({ 
        'message':message,
        'username':message_username
    }))
    message_input.value = ''
})