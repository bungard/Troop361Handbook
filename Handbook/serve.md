# Serving the Handbook Locally

The handbook uses `fetch()` to load markdown files, which requires a local web server
(browsers block file loading when you open `index.html` directly as a `file://` URL).

## Option 1 — Python (no install needed)

Open a terminal in this `Handbook/` folder and run:

```
python -m http.server 8080
```

Then open: **http://localhost:8080**

## Option 2 — VS Code Live Server extension

1. Install the **Live Server** extension in VS Code
2. Open this folder in VS Code
3. Right-click `index.html` → **Open with Live Server**
   (or click "Go Live" in the bottom status bar)

## Option 3 — Node.js

```
npx serve .
```

---

Once served, any changes you make to a `.md` file will appear immediately on the next browser refresh — no rebuild needed.
