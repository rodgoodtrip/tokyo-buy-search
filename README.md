# Tokyo / Yokohama Buy Search

Public single-page app for the owner-occupy searches. Each search is its own view. Stars and strikes stay in this browser (`localStorage`), separate per search.

## Live site

https://rodgoodtrip.github.io/tokyo-buy-search/

| View | URL |
| --- | --- |
| August snapshot (original prices, Rod’s shortlist) | https://rodgoodtrip.github.io/tokyo-buy-search/#august |
| Tokyo / Yokohama, Nov 2026 | https://rodgoodtrip.github.io/tokyo-buy-search/#nov |
| Shinjuku ≤ $600k | https://rodgoodtrip.github.io/tokyo-buy-search/#shinjuku |
| Ueno / Taito ≤ $600k | https://rodgoodtrip.github.io/tokyo-buy-search/#ueno |
| Osaka / Kansai | https://rodgoodtrip.github.io/tokyo-buy-search/#osaka |
| Tokyo 23 wards under $600k | https://rodgoodtrip.github.io/tokyo-buy-search/#wards |

Opening the site with no hash stays on the August snapshot. Force-load Rod’s shortlist on that view: https://rodgoodtrip.github.io/tokyo-buy-search/?seed=1

## Share a shortlist (no account)

On a listing view, **Export shortlist** downloads `{search}-shortlist-YYYY-MM-DD.json` (for example `august-shortlist-2026-11-17.json`) with:

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

The page loads each search from `data/*.json`, so open it through a local server (a `file://` tab cannot fetch those files):

```bash
python3 -m http.server 8765
```

Then open http://127.0.0.1:8765/

## Data

- `data/august.json` — August snapshot (same 187 listings as `listings.json`)
- `data/nov.json`, `data/shinjuku.json`, `data/ueno.json`, `data/osaka.json` — Nov 2026 searches
- `data/wards.json` — 23-ward medians and sample listings
- `listings.json` / `listings.csv` — August snapshot, camelCase fields
- `seed-state.json` — August shortlist snapshot
