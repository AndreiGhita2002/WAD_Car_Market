const Animation = document.getElementById('Animation');

const numberOfBoxes = 400;

for (let loop = 0; loop < numberOfBoxes; loop++) {
    const Box = document.createElement('div');
    Box.classList.add('colorBox');
    Animation.append(Box)
}

