// script.js
document.addEventListener('DOMContentLoaded', function() {
    const body = document.querySelector('body');
    const container = document.querySelector('.container');
    
    // Toggle dark mode
    function toggleDarkMode() {
        body.classList.toggle('dark-mode');
        container.classList.toggle('dark-mode');
    }

    // Add event listener to the button
    const darkModeBtn = document.createElement('button');
    darkModeBtn.textContent = 'Toggle Dark Mode';
    darkModeBtn.addEventListener('click', toggleDarkMode);
    document.body.appendChild(darkModeBtn);
});
