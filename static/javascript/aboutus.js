var thumbnail = document.getElementsByClassName("thumbnail");
var aboutPic = document.getElementById("about-us-pic");
var backgroundImg = new Array(
    "/static/images/car-pic-1-large.jpg",
    "/static/images/car-pic-2-large.jpg",
    "/static/images/car-pic-3-large.jpg",
    "/static/images/car-pic-4-large.jpg",
    "/static/images/car-pic-5-large.jpg",
);

let i = 0;
function forward(){
    if(i<4){
    aboutPic.style.backgroundImage = 'url("'+backgroundImg[i+1]+'")';
    thumbnail[i+1].classList.add("active");
    thumbnail[i].classList.remove("active");
    i++;
}
else{
    i = -1;
    aboutPic.style.backgroundImage = 'url("'+backgroundImg[i+1]+'")';
    thumbnail[i+1].classList.add("active");
    thumbnail[4].classList.remove("active");
    i++;
}
}
document.getElementById("next").addEventListener("click", forward);


function backward(){
    if(i>0){
    aboutPic.style.backgroundImage = 'url("'+backgroundImg[i-1]+'")';
    thumbnail[i-1].classList.add("active");
    thumbnail[i].classList.remove("active");
    i--;
}
else{
    i = 5;
    aboutPic.style.backgroundImage = 'url("'+backgroundImg[i-1]+'")';
    thumbnail[i-1].classList.add("active");
    thumbnail[0].classList.remove("active");
    i--;
}
}
document.getElementById("prev").addEventListener("click", backward);


var typedWords = new Typed(".hello-auto", {
    strings: ["Hello!", "Bonjour!", "Hola!", "Konnichiwa!","Selamat"],
    typeSpeed : 100,
    backSpeed : 100,
    loop: true
})

var typedWordsHello = new Typed(".auto-type", {
    strings: ["Developers", "Coders", "Students"],
    typeSpeed : 90,
    backSpeed : 90,
    loop: true
})
