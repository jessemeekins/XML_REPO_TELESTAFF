const refreshButton = document.getElementById('refresh');
const pageBody = document.getElementById('page-body');
const homeButton = document.getElementById('home');


const backgroundChange = refreshButton.onclick = () => {
    var currentColor = pageBody.style.backgroundColor;    
    pageBody.style.backgroundColor = (currentColor === 'red' ? 'green': 'red');
    refreshButton.innerHTML = currentColor === '' ? 'Refresh': currentColor;
}

refreshButton.addEventListener('click', backgroundChange());

const getCount = document.getElementById('get-count');
let count = 0;


const counter = getCount.onclick = () => {
    count+=1;
    getCount.innerHTML = count;
}


