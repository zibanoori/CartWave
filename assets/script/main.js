document.addEventListener('DOMContentLoaded', () => {
  const themeToggleBtn = document.querySelector('.js-theme-toggle');
  const htmlElement = document.documentElement;
  const icon = themeToggleBtn?.querySelector('i');
  const savedTheme = localStorage.getItem('them') || 'light'
  htmlElement.setAttribute('data-theme', savedTheme);
  updateTcon(savedTheme);
});