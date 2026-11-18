# Catch KYC Advisors — Digital Property

**Pensionizer Express × Club Dividend Detective | The Catch 72 & FUIQ Manifesto**

Canonical repo for the Catch KYC Advisors (AHA TOOLS) static flipbook and related dashboard experiments.

## Flipbook (Vercel)

Root static site: `index.html`, `styles.css`, `app.js`, `vercel.json`.

### Local

```bash
python3 -m http.server 4173 --bind 127.0.0.1
```

Open `http://127.0.0.1:4173`.

### Pages

1. Cover — brand crest & title  
2. Catch 72 — income compounding thesis  
3. FUIQ Manifesto — Find Undervalued Income Quotient  
4. Pensionizer Express — Top 50 / 10 / 5 indexes  
5. Club Dividend Detective — practitioner community  
6. Game of Yield — advisor toolkit  
7. Catch KYC close — CTAs  

### Deploy (CLI)

```bash
npx vercel deploy --yes --prod
# or, when logged out:
npx vercel deploy --temporary --yes
```

### Auto-deploys (Vercel → GitHub Import)

1. Open [vercel.com/new](https://vercel.com/new) and sign in with GitHub.  
2. **Import** `yurikotik/yurikotik-catch-kyc-dashboard`.  
3. Framework Preset: **Other** (static). Root Directory: `.`  
4. Deploy. Production tracks `main`; Preview deploys run on PRs.  
5. Optional: Project → Settings → Domains for a custom host.

Source of the merged flipbook: `yurikotik/Sideshow-Slides-` on `main`.

## Streamlit dashboard (optional)

Under `dashboard/`: `app.py`, `requirements.txt`, `runtime.txt` — a separate Streamlit / Supabase data view. Independent of the Vercel static flipbook (excluded via `.vercelignore`). On Streamlit Community Cloud, set the main file to `dashboard/app.py`.
