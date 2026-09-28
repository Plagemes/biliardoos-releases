/* BiliardoOS — progressively enhanced static site. No dependencies or tracking. */
(() => {
  'use strict';
  document.documentElement.classList.replace('no-js', 'js');
  const isEnglish = document.documentElement.lang.toLowerCase().startsWith('en');
  const t = (it, en) => isEnglish ? en : it;
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const siteUrl = isEnglish ? 'https://plagemes.github.io/biliardoos-releases/en/?noauto' : 'https://plagemes.github.io/biliardoos-releases/?noauto';
  const status = document.getElementById('download-status');
  const announce = (message) => { if (status) status.textContent = message; };
  document.getElementById('year').textContent = String(new Date().getFullYear());

  // The mobile navigation remains a normal, keyboard-accessible collection of links.
  const menu = document.querySelector('.menu-toggle');
  const mobileNav = document.getElementById('mobile-nav');
  const setMenu = (open) => {
    menu.setAttribute('aria-expanded', String(open));
    menu.setAttribute('aria-label', open ? t('Chiudi il menu', 'Close menu') : t('Apri il menu', 'Open menu'));
    mobileNav.hidden = !open;
  };
  menu.addEventListener('click', () => setMenu(menu.getAttribute('aria-expanded') !== 'true'));
  mobileNav.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => setMenu(false)));
  document.addEventListener('click', (event) => {
    if (!event.target.closest('.site-header')) setMenu(false);
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') {
      setMenu(false); menu.focus();
    }
  });
  window.matchMedia('(max-width: 800px)').addEventListener('change', (event) => {
    if (!event.matches) setMenu(false);
  });

  // Product screenshots follow the active language. English views are dedicated assets,
  // not overlaid translations, so the site stays visually coherent in both editions.
  const screens = isEnglish ? [
    { file: '02-tournament-overview-en.webp', title: 'Your championship', alt: 'BiliardoOS: English championship overview with phases, winner and closeout tools', text: 'From setup to closeout: every championship phase, the next step and the tools you need, all in one view.' },
    { file: '03-draw-report-en.webp', title: 'The draw, documented', alt: 'BiliardoOS: English draw report with summary, applied rules and PDF export', text: 'Heats built around the rules you set. The report records the draw and its random seed, so the result can be reproduced instead of reconstructed from memory.' },
    { file: '04-callups-4-per-a4-en.webp', title: 'Call-ups, ready to go', alt: 'BiliardoOS: English call-up slips laid out four per A4 page', text: 'Single slips for sending, or four per A4 page for printing. Call times, venues and tournament details are already in place.' },
    { file: '07-heat-results-en.webp', title: 'Match night, point by point', alt: 'BiliardoOS: English heat results with match scores and qualifiers', text: 'Enter scores, follow qualifications and prepare the final phase. From roll call to the last match, the championship stays under control.' },
    { file: '09-standings-en.webp', title: 'Every result has weight', alt: 'BiliardoOS: English championship standings with players, clubs and points', text: 'Individual and club standings, seasons, statistics and hall of fame. Match night ends, but every result remains easy to find.' },
    { file: '11-whatsapp-inbox-en.webp', title: 'The club stays connected', alt: 'BiliardoOS: English WhatsApp inbox with conversations and an AI-assisted reply', text: 'WhatsApp and email in the same workflow. Follow conversations, call-ups and scheduled sends without losing the championship context.' },
    { file: '12-ai-assistant-en.webp', title: 'Help, right where you need it', alt: 'BiliardoOS: English local AI assistant beside the championship screen', text: 'A question about the app or your championship data? The assistant stays beside your work and runs locally on your PC.' }
  ] : [
    { file: '02-tournament-overview.png', title: 'Il tuo campionato', alt: 'BiliardoOS: panoramica del campionato con fasi, vincitore e strumenti di chiusura', text: 'Dall’impostazione alla chiusura: le fasi del campionato, il prossimo passo e gli strumenti che ti servono, in un’unica vista.' },
    { file: '03-verbale-sorteggio.png', title: 'Il sorteggio, nero su bianco', alt: 'BiliardoOS: verbale di sorteggio con riepilogo, regole applicate e documento esportabile', text: 'Batterie costruite secondo le regole che imposti. Il verbale registra il sorteggio e il seed permette di riprodurlo, senza ricostruire tutto a memoria.' },
    { file: '04-convocazioni-4-per-a4.png', title: 'Le convocazioni', alt: 'BiliardoOS: tagliandi di convocazione impaginati quattro per foglio A4', text: 'Tagliandi singoli per l’invio o quattro per foglio A4 per la stampa. Orari di chiamata, sedi e informazioni del torneo, già al loro posto.' },
    { file: '07-risultati-batterie.png', title: 'La serata, punto per punto', alt: 'BiliardoOS: risultati delle batterie con punteggi delle partite e qualificazioni', text: 'Inserisci i punteggi, segui le qualificazioni e prepara la fase finale. Dall’appello all’ultima partita, il campionato resta sotto controllo.' },
    { file: '09-classifiche.png', title: 'Il valore di ogni risultato', alt: 'BiliardoOS: classifiche del campionato con posizioni, giocatori, gruppi sportivi e punti', text: 'Classifiche individuali e per gruppo, stagioni, statistiche e albo d’oro. La serata finisce, ma i risultati restano facili da ritrovare.' },
    { file: '11-whatsapp-inbox.png', title: 'Il circolo, in contatto', alt: 'BiliardoOS: casella dei messaggi WhatsApp con elenco delle conversazioni e risposta al giocatore', text: 'WhatsApp ed email nello stesso flusso di lavoro. Segui conversazioni, convocazioni e invii programmati, senza perdere il contesto del campionato.' },
    { file: '12-assistente-ai.png', title: 'Un aiuto, proprio lì', alt: 'BiliardoOS: assistente AI locale aperto accanto alla pagina del campionato', text: 'Una domanda sull’app o sui dati del campionato? L’assistente è accanto alla tua schermata e lavora sul tuo PC, con un motore AI locale.' }
  ];
  const screenDir = isEnglish ? '../screenshots-en' : 'screenshots';
  const tabs = Array.from(document.querySelectorAll('[data-screen]'));
  const panel = document.getElementById('screen-panel');
  const image = document.getElementById('product-screen');
  const screenLink = document.getElementById('screen-link');
  const dialog = document.getElementById('lightbox');
  let activeScreen = 0;
  function selectScreen(index, focus = false) {
    activeScreen = (index + screens.length) % screens.length;
    const screen = screens[activeScreen];
    tabs.forEach((tab, i) => {
      tab.setAttribute('aria-selected', String(i === activeScreen));
      tab.tabIndex = i === activeScreen ? 0 : -1;
    });
    panel.setAttribute('aria-labelledby', tabs[activeScreen].id);
    image.src = `${screenDir}/${screen.file}`;
    image.alt = screen.alt;
    screenLink.href = image.src;
    screenLink.setAttribute('aria-label', `${t('Ingrandisci la schermata', 'Enlarge screen')}: ${screen.title}`);
    document.getElementById('screen-label').textContent = screen.title;
    document.getElementById('screen-description').textContent = screen.text;
    const counter = document.getElementById('screen-count');
    counter.replaceChildren(document.createTextNode(String(activeScreen + 1).padStart(2, '0') + ' '));
    const total = document.createElement('i'); total.textContent = '/ 07'; counter.append(total);
    if (focus) tabs[activeScreen].focus({ preventScroll: true });
    tabs[activeScreen].scrollIntoView({ behavior: reducedMotion ? 'instant' : 'smooth', block: 'nearest', inline: 'nearest' });
  }
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => selectScreen(index));
    tab.addEventListener('keydown', (event) => {
      let next;
      if (event.key === 'ArrowRight') next = activeScreen + 1;
      if (event.key === 'ArrowLeft') next = activeScreen - 1;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = screens.length - 1;
      if (next !== undefined) { event.preventDefault(); selectScreen(next, true); }
    });
  });
  screenLink.addEventListener('click', (event) => {
    // Preserve modifier-click and a native image link when dialog is not supported.
    if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || !dialog.showModal) return;
    event.preventDefault();
    const fullImage = document.getElementById('lightbox-image');
    fullImage.src = image.src; fullImage.alt = image.alt;
    document.getElementById('lightbox-title').textContent = screens[activeScreen].title;
    dialog.showModal();
  });
  document.getElementById('lightbox-close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', (event) => {
    if (event.target !== dialog) return;
    const rect = dialog.getBoundingClientRect();
    if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) dialog.close();
  });
  dialog.addEventListener('close', () => screenLink.focus({ preventScroll: true }));

  // FAQ deep links work both from the installation notice and directly from a URL.
  function openFaq(id) {
    const item = document.getElementById(id);
    if (item && item.tagName === 'DETAILS') item.open = true;
  }
  document.querySelectorAll('[data-open-faq]').forEach((link) => link.addEventListener('click', () => openFaq(link.dataset.openFaq)));
  window.addEventListener('hashchange', () => openFaq(location.hash.slice(1)));
  openFaq(location.hash.slice(1));

  // Always keep a working release-page fallback; never inject API HTML into the page.
  const platform = navigator.userAgentData ? navigator.userAgentData.platform : navigator.platform;
  const isWindows = /Win/i.test(platform || navigator.userAgent);
  if (!isWindows) document.getElementById('device-note').hidden = false;
  const downloadLinks = Array.from(document.querySelectorAll('[data-download]'));
  downloadLinks.forEach((link) => link.addEventListener('click', () => {
    announce(/\.exe(?:$|\?)/i.test(link.href) ? t('Download richiesto. Se non parte, usa il collegamento “Tutte le versioni”.', 'Download requested. If it does not start, use the “All releases” link.') : t('Si apre la pagina della versione più recente su GitHub.', 'Opening the latest release page on GitHub.'));
  }));
  function allowedDownload(url) {
    try {
      const parsed = new URL(url);
      return parsed.protocol === 'https:' && parsed.hostname === 'github.com' && /^\/Plagemes\/biliardoos-releases\/releases\/download\//i.test(parsed.pathname) && /\.exe$/i.test(parsed.pathname);
    } catch { return false; }
  }
  async function loadRelease() {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 8000);
    try {
      const response = await fetch('https://api.github.com/repos/Plagemes/biliardoos-releases/releases/latest', {
        signal: controller.signal, credentials: 'omit', headers: { Accept: 'application/vnd.github+json' }
      });
      if (!response.ok) throw new Error(`GitHub ${response.status}`);
      const release = await response.json();
      if (release.draft || release.prerelease || !Array.isArray(release.assets)) return;
      const installer = release.assets.find((asset) => /\.exe$/i.test(asset.name || '') && allowedDownload(asset.browser_download_url));
      if (!installer) return;
      downloadLinks.forEach((link) => { link.href = installer.browser_download_url; });
      const version = String(release.tag_name || '').replace(/^v/i, '').slice(0, 32);
      if (version) document.querySelectorAll('[data-version]').forEach((node) => { node.textContent = `${t('Versione', 'Version')} ${version}`; });
      const size = Number(installer.size);
      if (Number.isFinite(size) && size > 0) document.querySelectorAll('[data-size]').forEach((node) => { node.textContent = `· ${Math.round(size / 1048576)} MB`; });
      // No surprise downloads on a marketing page. ?noauto remains supported.
      // Explicit ?download=1 is available for intentional direct-download links, on Windows only.
      const params = new URLSearchParams(location.search);
      if (isWindows && params.get('download') === '1' && !params.has('noauto')) {
        announce(t('Download richiesto dal collegamento. L’installer si apre ora.', 'Download requested by this link. The installer is opening now.'));
        window.location.assign(installer.browser_download_url);
      }
    } catch {
      // Offline, rate-limited or API unavailable: all buttons still lead to /releases/latest.
    } finally { clearTimeout(timeout); }
  }
  loadRelease();

  document.getElementById('copy-link').addEventListener('click', async () => {
    try {
      if (navigator.clipboard && window.isSecureContext) {
        await navigator.clipboard.writeText(siteUrl);
      } else {
        const field = document.createElement('textarea');
        field.value = siteUrl; field.setAttribute('readonly', '');
        field.style.cssText = 'position:fixed;left:-9999px;top:0';
        document.body.append(field); field.select();
        const copied = document.execCommand('copy'); field.remove();
        if (!copied) throw new Error('Clipboard unavailable');
      }
      announce(t('Link copiato. Inoltralo al tuo PC Windows.', 'Link copied. Send it to your Windows PC.'));
    } catch { announce(`${t('Copia questo indirizzo', 'Copy this address')}: ${siteUrl}`); }
  });

  // Content is visible without JS; animation is only added after observation is available.
  if ('IntersectionObserver' in window && !reducedMotion) {
    const observer = new IntersectionObserver((entries, instance) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) { entry.target.classList.add('is-visible'); instance.unobserve(entry.target); }
      });
    }, { threshold: 0.08 });
    document.querySelectorAll('[data-reveal]').forEach((element) => {
      element.classList.add('will-reveal'); observer.observe(element);
    });
  }
})();
