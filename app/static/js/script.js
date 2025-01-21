document.addEventListener('DOMContentLoaded', (event) => {
    const toggleModeButton = document.getElementById('toggle-mode');
    const body = document.getElementById('body');
    const html = document.getElementById('html');
    const footer = document.querySelector('.footer');

    const darkMode = localStorage.getItem('darkMode');
    if (darkMode === 'enabled') {
        enableDarkMode();
    } else {
        disableDarkMode();
    }

    toggleModeButton.addEventListener('click', () => {
        darkMode = localStorage.getItem('darkMode');
        if (darkMode !== 'enabled') {
            enableDarkMode();
        } else {
            disableDarkMode();
        }
    });

    function enableDarkMode() {
        body.classList.add('dark-mode');
        body.classList.remove('light-mode');
        footer.classList.add('dark-mode');
        footer.classList.remove('light-mode');
        localStorage.setItem('darkMode', 'enabled');
    }

    function disableDarkMode() {
        body.classList.add('light-mode');
        body.classList.remove('dark-mode');
        footer.classList.add('light-mode');
        footer.classList.remove('dark-mode');
        localStorage.setItem('darkMode', 'disabled');
    }
});