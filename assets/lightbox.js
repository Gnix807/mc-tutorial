(function () {
  const lightbox = document.createElement('div');
  lightbox.className = 'lightbox';
  lightbox.innerHTML = `
    <div class="lightbox-backdrop"></div>
    <div class="lightbox-image-wrap">
      <img class="lightbox-image" src="" alt="" />
      <div class="lightbox-caption"></div>
    </div>
    <button class="lightbox-close" aria-label="关闭">&times;</button>
  `;
  document.body.appendChild(lightbox);

  const backdrop = lightbox.querySelector('.lightbox-backdrop');
  const imgWrap = lightbox.querySelector('.lightbox-image-wrap');
  const imgEl = lightbox.querySelector('.lightbox-image');
  const caption = lightbox.querySelector('.lightbox-caption');
  const closeBtn = lightbox.querySelector('.lightbox-close');

  let isOpen = false;
  let sourceImg = null;

  function open(srcImg) {
    if (isOpen) return;
    isOpen = true;
    sourceImg = srcImg;

    const rect = srcImg.getBoundingClientRect();
    const captionText = srcImg.dataset.lightboxCaption || '';

    imgEl.src = srcImg.src;
    imgEl.alt = srcImg.alt;
    caption.textContent = captionText;

    // Start position
    imgWrap.style.transformOrigin = `${rect.left + rect.width / 2}px ${rect.top + rect.height / 2}px`;
    imgWrap.style.setProperty('--from-x', rect.left + 'px');
    imgWrap.style.setProperty('--from-y', rect.top + 'px');
    imgWrap.style.setProperty('--from-w', rect.width + 'px');
    imgWrap.style.setProperty('--from-h', rect.height + 'px');

    document.body.style.overflow = 'hidden';
    lightbox.classList.add('open');

    requestAnimationFrame(() => {
      imgWrap.classList.add('active');
      backdrop.classList.add('active');
      if (captionText) caption.classList.add('active');
    });
  }

  function close() {
    if (!isOpen) return;
    imgWrap.classList.remove('active');
    backdrop.classList.remove('active');
    caption.classList.remove('active');

    setTimeout(() => {
      lightbox.classList.remove('open');
      document.body.style.overflow = '';
      imgEl.src = '';
      isOpen = false;
      sourceImg = null;
    }, 350);
  }

  document.addEventListener('click', (e) => {
    const img = e.target.closest('img[data-lightbox]');
    if (img) {
      e.preventDefault();
      open(img);
    }
  });

  backdrop.addEventListener('click', close);
  closeBtn.addEventListener('click', close);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && isOpen) close();
  });
})();
