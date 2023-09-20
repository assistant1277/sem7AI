// Get references to the menu button and side panel
const menuButton = document.getElementById('menu-button');
const sidePanel = document.getElementById('side-panel');

// Add an event listener to the menu button to toggle the side panel
menuButton.addEventListener('click', () => {
    if (sidePanel.style.left === '0px') {
        sidePanel.style.left = '-250px'; // Hide the side panel
    } else {
        sidePanel.style.left = '0px'; // Show the side panel
    }
});