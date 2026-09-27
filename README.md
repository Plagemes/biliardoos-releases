🇬🇧 English | 🇮🇹 [Italiano](README.it.md)

<div align="center">

<img src="docs/logo.png" alt="BiliardoOS logo" width="120" height="120" />

# BiliardoOS

### Heat-championship billiards tournament manager

[![Latest release](https://img.shields.io/github/v/release/Plagemes/biliardoos-releases?label=latest%20release&color=1f9d5c)](https://github.com/Plagemes/biliardoos-releases/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/Plagemes/biliardoos-releases/total?label=downloads&color=1f9d5c)](https://github.com/Plagemes/biliardoos-releases/releases/latest)
[![Platform](https://img.shields.io/badge/platform-Windows-0078D6)](https://github.com/Plagemes/biliardoos-releases/releases/latest)
[![License](https://img.shields.io/badge/license-Freeware-lightgrey)](./LICENSE)

### ⬇️ [**Download BiliardoOS**](https://github.com/Plagemes/biliardoos-releases/releases/latest)

*Free, for Windows 10/11 - see [Installation](#installation) for the SmartScreen warning*

</div>

---

## What it is

**BiliardoOS** is a desktop app for running a **heat championship**
(*campionato a batterie*) in billiards/pool ("boccette") - the format used
by Italian amateur leagues, where players (or pairs) are split into heats
of 8 or 4, followed by a knockout final phase. It's the tournament format
typical of amateur championships between bars and clubs across Italy.

It is **not an official UISP product** and doesn't use any UISP branding:
it's built for any club or association running an amateur heat
championship, from the draw of the first evening all the way to the final
podium, with convocations, roll call, results, standings, WhatsApp/email
communications, and a local AI assistant that runs entirely on the
organizer's own PC.

**Note:** the app's user interface is currently in Italian, with partial
English support. It was built for the Italian amateur billiards/boccette
scene and its terminology (heats, roll call, convocation tickets...)
reflects that context - the descriptions below use the Italian terms
alongside their English translation where it helps.

All data stays on the organizer's PC: no account to create, no cloud
service to pay for, nothing sent to third parties.

## Features

### 🎲 Smart draw (sorteggio)

Automatic heat draw (*sorteggio*) - 8 or 4 players per heat, singles or
pairs - with configurable rules (no player drawn into their own home bar,
even distribution of sports clubs/groups, seeding by ranking/ELO) and a
quality-scored preview before you confirm. Every draw produces a report
("Anteprima sorteggio" / "Verbale di Sorteggio", i.e. draw preview / draw
record) exportable to PDF, with a reproducible seed.

### 🎫 Convocations and tickets

PDF convocation tickets (*tagliandi di convocazione*), laid out either 4
per A4 sheet for printing at the venue or as single tickets for
emailing/WhatsApp, with call times calculated automatically.

### ✅ Roll call and results

Roll call/check-in (*appello*) with late-arrival handling (grace period,
penalties, exclusion, and walkover where needed) and real-time result
entry, with standings and qualification updated after every match - even
from a phone, via the read-only LAN server ("Results on your phone").

### 🏆 Final phase and standings

Automatic generation of the final-phase bracket from the heat results, all
the way to the podium, plus season standings (individual and by
club/venue), a hall of fame, and advanced statistics.

### 💬 WhatsApp/email communications with anti-ban protection

Built-in WhatsApp (no external app to install) and email via Gmail or
Outlook, with automatic routing to whichever channel is available for each
recipient. The send queue has anti-ban protection (randomized delays,
hourly/daily limits, periodic pauses, quiet hours, an automatic circuit
breaker if anomalies are detected) and a transparency page showing exactly
what the queue is doing right now and why.

### 🤖 Local AI assistant, also on WhatsApp

A **fully local** AI assistant (powered by [Ollama](https://ollama.com)),
with automatic install/update of the engine and a model chosen to fit your
PC's hardware: it answers questions about using the app, with direct links
to the relevant pages. The same assistant can also answer players on
WhatsApp, with organizer approval required for sensitive requests.

### 🔗 Home/laptop link and on-site phone entry

Optional link between a "home" PC and a laptop on the road (via
[Tailscale](https://tailscale.com) or sync through a shared folder such as
Google Drive), plus an "offline evening" mode for a remote venue, with
result entry from a phone via a dedicated PIN.

### 🔒 Privacy and backups

Privacy consent management (GDPR-style), an optional app lock password,
automatic/manual local backups, an optional external backup copy
(OneDrive/USB/NAS), and automatic data-integrity checks with safe repair.

---

## Requirements

- **Windows 10 or 11** (64-bit).
- About **200 MB** of disk space for the app, plus an optional **1-2 GB**
  if you use the local AI assistant (model download).
- No Internet connection required for day-to-day use; it's only needed for
  automatic updates and, if used, for the first WhatsApp/email connection
  and the AI model download.

## Installation

1. Download `BiliardoOS-Setup-<version>.exe` from the
   [releases page](https://github.com/Plagemes/biliardoos-releases/releases/latest).
2. Double-click it to run it.

### Windows SmartScreen warning

BiliardoOS isn't (yet) signed with a code-signing certificate - a paid
service that isn't essential for an app meant for internal/club use. On
first launch you'll see a warning like:

> **"Windows protected your PC"** - *"Windows Defender SmartScreen prevented an unrecognized app from starting..."*

This is expected and harmless: click **"More info"**, then **"Run
anyway"**. The warning appears because the executable isn't digitally
signed, not because it contains anything harmful.

The installer installs **for the current user only**, without requiring
administrator rights (with the option to install it for all users if you
prefer), creates a shortcut on the Desktop and in the Start menu, and its
interface is currently Italian-only.

## Automatic updates

BiliardoOS checks for and installs new versions published here on GitHub
by itself - no account, no configuration needed: the check runs at startup
(silently if nothing is found) and can also be triggered from Settings →
**Updates**. An update is never installed while an open match evening is
in progress, and it's always preceded by an automatic data backup.

## Privacy

**All championship data stays on the organizer's own PC**: players,
tournaments, results and communications are saved locally, never on an
external server. The AI assistant **runs locally** (via Ollama, on the
user's own PC): questions and answers are never sent to any third-party
cloud service. The only outbound traffic is what's strictly needed for
automatic updates and, if enabled by the user, for actually sending
emails/WhatsApp messages.

## FAQ

**Do I have to pay for anything?**
No, BiliardoOS is free.

**Do I need an account or a subscription to some cloud service?**
No. Data stays on your PC. WhatsApp and email are optional and use your
own existing number/account, with no paid third-party services involved.

**Does it work without Internet?**
Yes, for day-to-day use (draw, printed convocations, roll call, results,
standings). Internet is only needed for automatic updates and for features
that require actually sending something (WhatsApp/email) or downloading
the AI model.

**Does the AI assistant send my data to external services?**
No: the assistant runs locally on your PC via Ollama. No player or
tournament data ever leaves the PC for the AI assistant.

**Why does Windows show a warning during installation?**
Because the installer isn't signed with a (paid) code-signing certificate.
See [Installation](#installation) above.

**Can I use it on more than one PC (home and laptop)?**
Yes, via the optional "home/laptop link" feature (Tailscale or a shared
folder) - see the dedicated section above.

**Can I modify or redistribute the program?**
No: BiliardoOS is freeware, provided "as is" - it's not open source. See
[License](#license).

**Where can I find the full manual?**
In-app, under the **Guide** entry in the side menu, or by asking the
built-in AI assistant directly.

## Support & ideas

- Have a question, doubt, or idea? Start a discussion in
  [**Discussions**](https://github.com/Plagemes/biliardoos-releases/discussions).
- Found a problem? Open an
  [**Issue**](https://github.com/Plagemes/biliardoos-releases/issues/new/choose)
  - if possible, attach the "support package" you can generate from
    Settings → "Report a problem" (it collects logs and diagnostic
    information, never players' personal data).

## License

BiliardoOS is **freeware**: free to use, but **all rights are reserved** -
you may not resell, modify, or redistribute the program without
permission, and it's provided "as is", without warranties. See the full
text in [`LICENSE`](./LICENSE).

---

If you find BiliardoOS useful, leave a ⭐ on the project!
