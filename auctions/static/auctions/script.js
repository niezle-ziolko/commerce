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

document.addEventListener('DOMContentLoaded', () => {
    const button = document.querySelector('#emoji-button');
    if (!button) return;
    
    import('https://cdn.jsdelivr.net/npm/@joeattardi/emoji-button@latest/dist/index.min.js')
        .then(({ EmojiButton }) => {
            const button = document.querySelector('#emoji-button');
            const textarea = document.querySelector('#id_comment');
            const picker = new EmojiButton({
                theme: 'dark',
                position: 'bottom-start',
            });

            button.addEventListener('click', (event) => {
                event.preventDefault();
                picker.togglePicker(button);
            });

            picker.on('emoji', (emoji) => {
                textarea.value += emoji.emoji;
            });
        })
        .catch((error) => {
            console.error('Nie udało się załadować EmojiButton:', error);
        });
});