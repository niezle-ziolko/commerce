function setActiveLabel(inputId) {
    const label = document.querySelector(`label[for="${inputId}"]`);
    if (label) {
        label.classList.add('active');
    };
};

function checkInput(inputId) {
    const input = document.getElementById(inputId);
    const label = document.querySelector(`label[for="${inputId}"]`);
    if (input.value.trim() !== '') {
        label.classList.add('active');
    } else {
        label.classList.remove('active');
    };
};