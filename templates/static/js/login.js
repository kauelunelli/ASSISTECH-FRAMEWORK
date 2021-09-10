// Revelar e Ocultar a senha.
let btn = document.querySelector('span');

btn.addEventListener('click', function() {
    let input = document.querySelector('#password');

    if(input.getAttribute('type') == 'password') {
        input.setAttribute('type', 'text');
        btn.className = 'bi bi-eye-slash-fill'
    } else {
        input.setAttribute('type', 'password');
        btn.classList.remove(".bi.bi-eye-slash-fill");
        btn.className = 'bi bi-eye-fill'
    }

});