(() => {
  'use strict';
  const data = window.TOOLKIT_DATA;
  if (!data || !Array.isArray(data.cards)) return;
  const cards = data.cards;
  const labels = {'general':'General cards','food-systems':'Food-system prompts','facilitator':'Original facilitator sequence','all':'Complete source deck'};
  const descriptions = {
    general: 'A selection for use across settings: where, when, affect, voice, form, collaborators, pivots, and ways of knowing.',
    'food-systems': 'Ten context-specific Speculation cards from the original workshop edition. Keep their food and agricultural framing when using them.',
    facilitator: 'The original eighteen-card workshop sequence, preserved as a source edition. For the modular two-layer starting point, use the new guide below.',
    all: 'All 122 cards in source order, including general prompts, food-system speculations, and the original facilitator sequence.'
  };
  let collection = 'general';
  let page = 0;
  const pageSize = 24;
  let selected = null;
  let showingBack = false;
  const grid = document.getElementById('card-grid');
  const search = document.getElementById('card-search');
  const category = document.getElementById('category-filter');
  const dialog = document.getElementById('card-dialog');
  const previous = document.getElementById('previous-page');
  const next = document.getElementById('next-page');

  function inCollection(card) { return collection === 'all' || card.collection === collection; }
  function resetCategories() {
    category.replaceChildren(new Option('All layers', 'all'));
    const found = new Map();
    cards.filter(inCollection).forEach(card => found.set(card.category, card.category_label));
    for (const [key, label] of found) category.append(new Option(label, key));
  }
  function filtered() {
    const q = search.value.trim().toLocaleLowerCase();
    return cards.filter(card => inCollection(card) && (category.value === 'all' || card.category === category.value) && (!q || `${card.category_label} ${card.search_text || card.text}`.toLocaleLowerCase().includes(q)));
  }
  function render() {
    const matches = filtered();
    const totalPages = Math.max(1, Math.ceil(matches.length / pageSize));
    page = Math.min(page, totalPages - 1);
    grid.replaceChildren();
    matches.slice(page * pageSize, (page + 1) * pageSize).forEach(card => {
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'browse-card';
      button.setAttribute('aria-label', `Open ${card.category_label} card: ${(card.search_text || card.text).slice(0, 180)}`);
      const img = document.createElement('img');
      img.src = card.front_image;
      img.alt = '';
      img.width = 756;
      img.height = 540;
      img.loading = 'lazy';
      const caption = document.createElement('span');
      caption.className = 'card-meta';
      const name = document.createElement('strong');
      name.textContent = card.category_label;
      const reference = document.createElement('span');
      reference.textContent = `Source p. ${card.front_page} ↗`;
      caption.append(name, reference);
      button.append(img, caption);
      button.addEventListener('click', () => openCard(card));
      grid.append(button);
    });
    if (!matches.length) {
      const empty = document.createElement('div');
      empty.className = 'no-results';
      const title = document.createElement('h3');
      title.textContent = 'No cards match this search.';
      const note = document.createElement('p');
      note.textContent = 'Try another word, or clear the filters.';
      empty.append(title, note);
      grid.append(empty);
    }
    document.getElementById('result-count').textContent = `${matches.length} ${matches.length === 1 ? 'card' : 'cards'}${matches.length > pageSize ? ` · showing ${page * pageSize + 1}–${Math.min((page + 1) * pageSize, matches.length)}` : ''}`;
    document.getElementById('page-label').textContent = `${page + 1} / ${totalPages}`;
    previous.disabled = page === 0;
    next.disabled = page + 1 >= totalPages;
    document.getElementById('pagination').hidden = matches.length <= pageSize;
    document.getElementById('collection-description').textContent = descriptions[collection];
  }
  function showFace() {
    if (!selected) return;
    const img = document.getElementById('dialog-image');
    img.src = showingBack ? selected.back_image : selected.front_image;
    img.alt = `${selected.category_label} card ${showingBack ? 'back' : 'front'}`;
    document.getElementById('dialog-side').textContent = showingBack ? 'Back' : 'Front';
    document.getElementById('flip-card').textContent = showingBack ? 'Show front ↻' : 'Turn over ↻';
  }
  function openCard(card) {
    selected = card;
    showingBack = false;
    document.getElementById('dialog-title').textContent = card.category_label;
    document.getElementById('dialog-collection').textContent = labels[card.collection];
    const text = document.getElementById('dialog-text');
    text.replaceChildren();
    const blocks = card.display_blocks && card.display_blocks.length ? card.display_blocks : [card.display_text || card.source_text];
    blocks.forEach(block => {
      const p = document.createElement('p');
      p.textContent = typeof block === 'string' ? block : JSON.stringify(block);
      text.append(p);
    });
    document.getElementById('dialog-source').textContent = `Original source: front p. ${card.front_page}; back p. ${card.back_page}. Card wording retained. Text extraction has been checked for missing ligature letters.`;
    document.getElementById('dialog-pdf').href = `downloads/Multispecies_Futures_Original_LiveText.pdf#page=${card.front_page}`;
    showFace();
    dialog.showModal();
  }
  document.getElementById('close-dialog').addEventListener('click', () => dialog.close());
  document.getElementById('flip-card').addEventListener('click', () => { showingBack = !showingBack; showFace(); });
  dialog.addEventListener('click', event => { if (event.target === dialog) { const box = dialog.getBoundingClientRect(); if (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom) dialog.close(); } });
  document.querySelectorAll('[data-collection]').forEach(button => {
    button.addEventListener('click', () => {
      collection = button.dataset.collection;
      page = 0;
      document.querySelectorAll('[data-collection]').forEach(item => { const active = item === button; item.classList.toggle('active', active); item.setAttribute('aria-pressed', String(active)); });
      resetCategories();
      render();
    });
  });
  search.addEventListener('input', () => { page = 0; render(); });
  category.addEventListener('change', () => { page = 0; render(); });
  document.getElementById('deck-controls').addEventListener('submit', event => event.preventDefault());
  document.getElementById('deck-controls').addEventListener('reset', () => { setTimeout(() => { page = 0; render(); }, 0); });
  function changePage(delta) { page += delta; render(); document.getElementById('deck-controls').scrollIntoView({behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth', block:'start'}); }
  previous.addEventListener('click', () => changePage(-1));
  next.addEventListener('click', () => changePage(1));
  resetCategories();
  render();
})();
