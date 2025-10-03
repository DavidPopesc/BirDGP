const minusBtn = document.querySelector('.minus');
const plusBtn = document.querySelector('.plus');

minusBtn.addEventListener('click', (e) => {
    let el = document.getElementById("TR").value;
    el += 1;
    document.getElementById("TR").textContent = el;
    //e.preventDefault();
  });