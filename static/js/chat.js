const username = JSON.parse(document.getElementById('json-username').textContent)
const message_username = JSON.parse(document.getElementById('json-message-username').textContent)

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
    console.log(e)
}