var header = document.querySelector('.header');
var nav = document.querySelector('.nav');
var nav_toggler = document.querySelector('.nav-toggler');
var nav_shown = false;

nav.addEventListener('transitionend', function () {
    if (!nav_shown) {
        nav.classList.add('d-none');
    }
});

nav_toggler.addEventListener('click', function () {
    if (!nav_shown) {
        nav.classList.remove('d-none');
        setTimeout(() => header.classList.add('show'), 0);
    } else {
        header.classList.remove('show');
    }

    nav_shown = !nav_shown;
});
