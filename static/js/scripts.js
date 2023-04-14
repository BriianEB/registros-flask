var header = document.querySelector('.header');
var nav_toggler = document.querySelector('.nav-toggler');

nav_toggler.addEventListener('click', function (event) {
    header.classList.toggle('show');
});
