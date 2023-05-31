const toggleSwitch = document.querySelector('.toggle-link input[type="checkbox"]');
const toggleIcon = document.querySelector('.toggle-link i');

function switchTheme(event) {
  if (event.target.checked) {
    document.documentElement.setAttribute('data-theme', 'dark');
    toggleIcon.classList.remove('fa-moon');
    toggleIcon.classList.add('fa-sun');
  } else {
    document.documentElement.setAttribute('data-theme', 'light');
    toggleIcon.classList.remove('fa-sun');
    toggleIcon.classList.add('fa-moon');
  }
}

toggleSwitch.addEventListener('change', switchTheme, false);
