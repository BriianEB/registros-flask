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





const boton_color = document.getElementById('boton_color');
const color_container = document.getElementById('color_container');
const colores = ['#C23F61', '#C23F9E', '#9C3FC2', '#7D3FC2', '#3F4BC2', '#40C7D7', '#3FC296', '#3FC245', '#CED740', '#D7A040'];

if (boton_color) {
    boton_color.addEventListener('click', function () {
        var random_num = Math.floor(Math.random() * colores.length);
        color_container.style.backgroundColor = colores[random_num];
    });
}
