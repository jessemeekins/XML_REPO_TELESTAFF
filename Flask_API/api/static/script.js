const refreshButton = document.getElementById('refresh');
const pageBody = document.getElementById('page-body');
const homeButton = document.getElementById('home');


const addAlsButton = document.getElementById('add-als-count');
const rmAlsButton = document.getElementById('rm-als-count');
let alsCount = document.getElementById('als-count').innerText;
let newCount = document.getElementById('als-count');

const alsAdd = addAlsButton.onclick = () => {
    alsCount ++;
    newCount.innerHTML = alsCount
}
const alsRm = rmAlsButton.onclick = () => {
    alsCount --;
    newCount.innerHTML = alsCount
}


const addBlsButton = document.getElementById('add-bls-count');
const rmBlsButton = document.getElementById('rm-bls-count');
let blsCount = document.getElementById('bls-count').innerText;
let newBlsCount = document.getElementById('bls-count');

const blsAdd = addBlsButton.onclick = () => {
    blsCount ++;
    newBlsCount.innerHTML = blsCount;
}
const blsRm = rmBlsButton.onclick = () => {
    blsCount --;
    newBlsCount.innerHTML = blsCount;
}


const addBtnCount = document.getElementById('add-counter-count');
const rmBtnCount = document.getElementById('rm-counter-count');
const getCount = document.getElementById('counter');
let count = 0;

const addCounter = addBtnCount.onclick = () => {
    count++;
    getCount.innerHTML = count;
    console.log(count)
}
const rmCounter = rmBtnCount.onclick = () => {
    count--;
    getCount.innerHTML = count;
    console.log(count)
}

const addPeopleButton= document.getElementById('add-people-count');
const rmPeopleButton = document.getElementById('rm-people-count');
let peopleCount = document.getElementById('num-people').innerText;
let newPeopleCount = document.getElementById('num-people');


const addPeople = addPeopleButton.onclick = () => {
    peopleCount++;
    newPeopleCount.innerHTML = peopleCount;
    console.log(count)
}
const rmPeople = rmPeopleButton.onclick = () => {
    peopleCount--;
    newPeopleCount.innerHTML = peopleCount;
    console.log(count)
}


const addMedicButton= document.getElementById('add-medic-count');
const rmMedicButton = document.getElementById('rm-medic-count');
let medicCount = document.getElementById('num-medics').innerText;
let newMedicCount = document.getElementById('num-medics');


const addMedic = addMedicButton.onclick = () => {
    medicCount++;
    newMedicCount.innerHTML = medicCount;
    console.log(count)
}
const rmMedic = rmMedicButton.onclick = () => {
    medicCount--;
    newMedicCount.innerHTML = medicCount;
    console.log(count)
}

const freshButton = document.getElementById('refresher');

const refresher = freshButton.onclick = () => {
    window.location.reload();
} 

filterSelection("alsCount")
function filterSelection(c) {
  var x, i;
  x = document.getElementsByClassName("filterDiv");
  if (c == "alsCount") c = "";
  // Add the "show" class (display:block) to the filtered elements, and remove the "show" class from the elements that are not selected
  for (i = 0; i < x.length; i++) {
    w3RemoveClass(x[i], "show");
    if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
  }
}

// Show filtered elements
function w3AddClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) == -1) {
      element.className += " " + arr2[i];
    }
  }
}

// Hide elements that are not selected
function w3RemoveClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      arr1.splice(arr1.indexOf(arr2[i]), 1);
    }
  }
  element.className = arr1.join(" ");
}

// Add active class to the current control button (highlight it)
//var btnContainer = document.getElementById("myBtnContainer");
var btns = btnContainer.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
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