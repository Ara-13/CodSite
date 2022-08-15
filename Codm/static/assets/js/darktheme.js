var css = document.getElementById('colorswitch'); 
const d = new Date();
let hour = d.getHours();
if (hour < 8 && hour > 6){
    css.href = '/assets/css/main.css';
    var moon = document.getElementById('moon');
    moon.src = '/static/assets/img/svg/moon-solid.svg';
    var img = document.getElementById('logo');
    img.src = 'http://127.0.0.1:8000/static/assets/img/logo.jpg'
} else {
    var moon = document.getElementById('moon');
    moon.src = '/static/assets/img/svg/sun-solid.svg';
    var img = document.getElementById('logo');
    img.src = 'http://127.0.0.1:8000/static/assets/img/logo-dark.jpg';
    css.href = '/static/assets/css/main-dark.css';
}