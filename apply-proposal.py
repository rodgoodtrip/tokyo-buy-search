#!/usr/bin/env python3
"""Apply a friend-exported shortlist proposal into seed-state.json and print the diff."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED_PATH = ROOT / "seed-state.json"


def load(path: Path):
    data = json.loads(path.read_text())
    if "seed" in data and isinstance(data["seed"], dict):
        return data["seed"], data.get("changes")
    # raw seed-state.json drop-in
    return data, None


def ids(xs):
    return [str(x) for x in (xs or []) if x is not None]


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <proposal.json|seed-state.json>")
        sys.exit(2)
    proposal_path = Path(sys.argv[1])
    incoming, embedded_changes = load(proposal_path)
    before = json.loads(SEED_PATH.read_text()) if SEED_PATH.exists() else {}

    seed = {
        "starred": ids(incoming.get("starred")),
        "struck": ids(incoming.get("struck")),
        "view": incoming.get("view", "active"),
        "track": incoming.get("track", "all"),
        "kind": incoming.get("kind", "all"),
        "line": incoming.get("line", "all"),
        "sortKey": incoming.get("sortKey", "tokyo"),
        "sortDir": incoming.get("sortDir", "asc"),
    }

    b_star, a_star = set(ids(before.get("starred"))), set(seed["starred"])
    b_struck, a_struck = set(ids(before.get("struck"))), set(seed["struck"])
    changes = embedded_changes or {
        "starredAdded": sorted(a_star - b_star),
        "starredRemoved": sorted(b_star - a_star),
        "struckAdded": sorted(a_struck - b_struck),
        "struckRemoved": sorted(b_struck - a_struck),
    }

    print("Shortlist diff vs current seed-state.json")
    for label, key in [
        ("+ starred", "starredAdded"),
        ("- starred", "starredRemoved"),
        ("+ struck", "struckAdded"),
        ("- struck", "struckRemoved"),
    ]:
        vals = changes.get(key) or []
        print(f"  {label}: {len(vals)}")
        for v in vals:
            print(f"    {v}")

    SEED_PATH.write_text(json.dumps(seed, ensure_ascii=False, indent=2) + "\n")
    print(f"\nWrote {SEED_PATH}")
    print("Review with: git diff seed-state.json")


if __name__ == "__main__":
    main()
