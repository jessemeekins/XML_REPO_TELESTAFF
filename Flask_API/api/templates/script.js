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


localStorage.setItem('name', 'Jesse' );
localStorage.setItem('phone', '901-343-7736' );
localStorage.setItem('address', '592 South Cox');


const tableName = document.getElementById('table-name');
const tableAddress = document.getElementById('table-address');
const tablePhone = document.getElementById('table-phone');
const submitButton = document.getElementById('submit');

tableName.innerHTML = localStorage.getItem('name')
tableAddress.innerHTML = localStorage.getItem('address')
tablePhone.innerHTML = localStorage.getItem('phone')


