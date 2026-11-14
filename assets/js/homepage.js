/* Progressive enhancement: every paper remains visible when JavaScript is unavailable. */
(() => {
  const filters = document.querySelector('.publication-filters');
  const papers = [...document.querySelectorAll('.publication')];
  const count = document.querySelector('.publication-count');
  if (filters && count && papers.length) {
    filters.hidden = false;
    count.hidden = false;
    const update = (filter) => {
      let visible = 0;
      papers.forEach((paper) => {
        paper.hidden = filter !== 'all' && paper.dataset.role !== filter;
        if (!paper.hidden) visible++;
      });
      filters.querySelectorAll('button').forEach((button) => {
        button.setAttribute('aria-pressed', String(button.dataset.filter === filter));
      });
      count.textContent = `Showing ${visible} of ${papers.length} selected publications`;
    };
    filters.addEventListener('click', (event) => {
      const button = event.target.closest('button[data-filter]');
      if (button) update(button.dataset.filter);
    });
    update('all');
  }
})();
