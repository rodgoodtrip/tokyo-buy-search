# Tokyo / Yokohama Buy Search

Public single-page app mirroring the Cursor canvas: sortable table, track/type/line filters, view modes, star/strike (saved per browser via `localStorage`).

## Live site

https://rodgoodtrip.github.io/tokyo-buy-search/

Force-load Rod’s exported shortlist: https://rodgoodtrip.github.io/tokyo-buy-search/?seed=1

## Share a shortlist (no account)

On the live page, **Export shortlist** downloads `tokyo-shortlist-proposal-YYYY-MM-DD.json` with:

- `seed` — drop-in `seed-state.json` contents
- `changes` — added/removed starred & struck vs Rod’s baked-in seed

Send that file to Rod. To accept:

```bash
python3 apply-proposal.py ~/Downloads/tokyo-shortlist-proposal-YYYY-MM-DD.json
git diff seed-state.json   # review, then commit if good
```

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
