const btn2 = document.querySelector(".log")
const email_address = document.getElementById("email")
const password = document.getElementById("pass")
const container = document.querySelector(".app")

function closeWindow() {
    window.close()
}


function send_data() {
    const email = email_address.value
    const pass = password.value
    eel.get_data(email, pass)
    eel.open_app()
    eel.send2(email)
    //window.close()
    container.classList.add("-hidden")
    
}



btn2.addEventListener("click", send_data)