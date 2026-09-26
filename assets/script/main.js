document.addEventListener('DOMContentLoaded', () => {
  const themeToggleBtn = document.querySelector('.js-theme-toggle');
  const htmlElement = document.documentElement;
  const icon = themeToggleBtn?.querySelector('i');

  const savedTheme = localStorage.getItem('them') || 'light'
  htmlElement.setAttribute('data-theme', savedTheme);
  updateIcon(savedTheme);

  themeToggleBtn?.addEventListener('click', () => {
    const currentTheme = htmlElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    htmlElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateIcon(newTheme);
  });
});