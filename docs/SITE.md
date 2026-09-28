# BiliardoOS — sito pubblico

Redesign del 28 settembre 2026: un'identità da circolo, con smeraldo scuro, ottone, avorio, fotografia editoriale e tipografia serif. Il sito resta statico e compatibile con GitHub Pages, senza framework, processo di compilazione o dipendenze JavaScript.

## File

- `index.html`: contenuti, navigazione, galleria, installazione, FAQ e metadati.
- `styles.css`: layout responsive, palette, animazioni, stampa e movimento ridotto.
- `app.js`: menu mobile, galleria accessibile, ingrandimento, informazioni sulla release e copia del collegamento.
- `assets/club.webp`: fotografia editoriale generata con GPT Image per il redesign, ottimizzata in WebP (circa 25 KB). Non è una fotografia di un cliente o di un evento dichiarato reale.
- `assets/precision.svg`: illustrazione vettoriale originale del castello a cinque birilli.
- `assets/mark.svg`: icona coordinata alla nuova testata.
- `screenshots/`: schermate reali del programma già presenti nel repository. Il redesign le usa senza modificarle.

I font sono di sistema: nessun download da servizi esterni. Non sono stati aggiunti tracker o analytics. La pagina interroga l'API pubblica di GitHub per conoscere l'ultima release stabile.

## Download

I pulsanti funzionano anche senza JavaScript e portano a `/releases/latest`. Quando l'API risponde, puntano direttamente all'installer `.exe` della release stabile. Sono accettati solo download HTTPS dal repository Plagemes/biliardoos-releases su github.com.

Non parte un download inatteso aprendo la pagina. `?noauto` rimane supportato. Il collegamento esplicito `?download=1` avvia il download soltanto su Windows; `noauto` ha sempre la precedenza. Da altri dispositivi si può copiare il collegamento e aprirlo sul PC Windows.

Release, installer, manifest di aggiornamento e programma desktop non vengono modificati dal sito.

## Anteprima locale

Dalla radice del repository:

```sh
python -m http.server 8000 --directory docs
```

Aprire `http://localhost:8000/?noauto`.

## Verifiche

Controllati layout da 320 a 1920 pixel, sette schermate e relativi testi, tasti freccia/Home/End nella galleria, dialogo con Escape e ripristino del focus, menu mobile, FAQ native e collegamento SmartScreen, modalità senza JavaScript e movimento ridotto. Testati i fallback con API non disponibile, risposta non valida, rate limit, installer mancante e URL esterno non attendibile. Le prove browser usano i file di produzione e risposte API controllate; non eseguono l'installer.

## Manutenzione

Per aggiornare la galleria, modificare l'array `screens` in `app.js` e le schede corrispondenti in `index.html`. Aggiornare i contenuti quando cambiano requisiti, licenza o funzioni distribuite. Versione e dimensione dell'installer non sono fissate nel codice.

Il branch `backup/site-before-redesign-20260928` conserva il sito precedente, incluse le schermate aggiornate prima della pubblicazione. La cronologia Git rimane intatta.
