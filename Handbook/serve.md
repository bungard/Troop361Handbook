# Working with the Handbook

There are two ways to view the handbook locally.

---

## Option A — Compiled (no server needed)

Run the build script once after editing any `.md` file:

```
python build.py
```

Then open `index.html` directly in any browser — no server required.
This is also what GitHub Actions runs before deploying to GitHub Pages,
so what you see locally will match what's live.

---

## Option B — Live server (instant refresh while editing)

Good when you're actively writing content and want to see changes on every save
without re-running the build script.

**Python (no install needed):**
```
python -m http.server 8080
```
Then open: **http://localhost:8080**

**VS Code Live Server extension:**
Right-click `index.html` → **Open with Live Server**
(or click "Go Live" in the VS Code status bar)

---

## Adding a new section

1. Create the `.md` file in the appropriate `Section*/` folder.
2. Add an entry to the `SECTIONS` array in **both** `index.html` and `build.py`.
3. Run `python build.py` to compile.
