(function () {
  const STORAGE_KEY = 'mc-tutorial-theme';

  function getStored() {
    try { return localStorage.getItem(STORAGE_KEY) || 'auto'; }
    catch { return 'auto'; }
  }

  function setStored(value) {
    try { localStorage.setItem(STORAGE_KEY, value); }
    catch {}
  }

  function applyTheme(value) {
    if (value === 'auto') {
      document.documentElement.removeAttribute('data-theme');
    } else {
      document.documentElement.setAttribute('data-theme', value);
    }
  }

  function updateButtons(value) {
    document.querySelectorAll('.book-theme-toggle button[data-theme-value]').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.themeValue === value);
    });
  }

  function setTheme(value) {
    applyTheme(value);
    setStored(value);
    updateButtons(value);
  }

  document.addEventListener('DOMContentLoaded', () => {
    const stored = getStored();
    setTheme(stored);

    document.querySelectorAll('.book-theme-toggle button[data-theme-value]').forEach(btn => {
      btn.addEventListener('click', () => setTheme(btn.dataset.themeValue));
    });
  });
})();
