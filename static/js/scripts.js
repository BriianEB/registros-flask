var header = document.querySelector('.header');
var nav = document.querySelector('.nav');
var nav_toggler = document.querySelector('.nav-toggler');
var nav_shown = false;

nav.addEventListener('transitionend', function () {
    nav.classList.remove('collapsing');

    if (!nav_shown) {
        nav.classList.remove('h-0');
        nav.classList.add('d-none');
    }

    nav.style.height = null;
    nav_toggler.disabled = false;
});

nav_toggler.addEventListener('click', function () {
    nav_toggler.disabled = true;

    if (!nav_shown) {
        nav.classList.remove('d-none');
        var nav_height = nav.offsetHeight + 'px';
        nav.classList.add('collapsing');

        setTimeout(function () {
            nav.style.height = nav_height;
            header.classList.add('show');
        }, 0);
    } else {
        nav.style.height = nav.offsetHeight + 'px';
        nav.classList.add('collapsing');

        setTimeout(function () {
            nav.classList.add('h-0');
            header.classList.remove('show');
        }, 0);
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
