var login = document.querySelector('.login')
var signup = document.querySelector('.signup')
var logout = document.querySelector('.logout')

var body = document.querySelector('.body')
var modal = document.querySelector('#modal')

function openModal() {
    body.classList.add('none')
    modal.classList.remove('none')
}

function closeModal() {
    body.classList.remove('none')
    modal.classList.add('none')
}

login.addEventListener('click', openModal)
signup.addEventListener('click', openModal)

logout.addEventListener('click', closeModal)
