const from = document.getElementById("from")
const to = document.getElementById("to")
const subject = document.getElementById("subject")
const message = document.getElementById("box")
const btn = document.querySelector(".send")

function getdata() {
    result1 = from.value
    result2 = to.value
    result3 = subject.value
    result4 = message.value
    eel.send(result1, result2, result3, result4)
}

eel.expose(notify)
function notify(){
    alert("Email sent successfully!")
}


eel.expose(notify2)
function notify2(){
    alert("Sending email, please wait!")
}

eel.expose(send3)
function send3(email) {
    from.value = email    
}

btn.addEventListener("click", getdata)