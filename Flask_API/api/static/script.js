const refreshButton = document.getElementById('refresh');
const pageBody = document.getElementById('page-body');
const homeButton = document.getElementById('home');



const addAlsButton = document.getElementById('add-als-count');
const rmAlsButton = document.getElementById('rm-als-count');
let alsCount = document.getElementById('als-count').innerHTML;


const alsCounter = addAlsButton.onclick = () => {
    alsCount++;
    
    alsCount.innerHTML = alsCount;
    console.log(alsCount)
}

const buttonCount = document.getElementById('count');
const getCount = document.getElementById('counter');
let count = 0;

const counter = buttonCount.onclick = () => {
    count+=1;
    getCount.innerHTML = count;
    console.log(count)
}
















function startTime() {
    const today = new Date();
    let h = today.getHours();
    let m = today.getMinutes();
    let s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('nav-clock').innerHTML =  today;

    setTimeout(startTime, 1000);
  }
  
function checkTime(i) {
if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
return i;
}