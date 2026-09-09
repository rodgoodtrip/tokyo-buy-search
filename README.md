# Tokyo / Yokohama Buy Search

Public single-page app mirroring the Cursor canvas: sortable table, track/type/line filters, view modes, star/strike (saved per browser via `localStorage`).

## Live site

https://rodgoodtrip.github.io/tokyo-buy-search/

Force-load Rod’s exported shortlist: https://rodgoodtrip.github.io/tokyo-buy-search/?seed=1

## Submit updates for review

On the live page, **Submit for review** opens a GitHub issue with your current stars/strikes (you need a GitHub account).  
A workflow then opens a PR that updates `seed-state.json` for Rod to merge.

Issue titles must start with `[shortlist]` (the button does this for you).

## Shortlist sync

`seed-state.json` is exported from the Cursor canvas (`starredIds` / `struckIds`). The SPA:

- Auto-applies it on **first visit** (empty local storage)
- Has a **Load Rod’s shortlist** button to re-apply (overwrites local marks)
- Supports `?seed=1` to force that seed

Stars/strikes otherwise stay **per visitor browser** — not a shared live sync.

## Local

Open `index.html` in a browser (no build step).

## Data

- `listings.json` / `listings.csv` — 187 listings (camelCase fields)
- `seed-state.json` — canvas shortlist snapshot
