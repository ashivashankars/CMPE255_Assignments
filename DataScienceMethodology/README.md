# Data Science Methodologies — CRISP-DM · SEMMA · KDD

This repository contains **three complete projects**, one per methodology, each with:
- A phase-by-phase notebook flow
- Reproducible `src/` modules
- Reports & model cards
- A minimal deployment demo (FastAPI + Streamlit)
- A **"World‑Renowned Critic"** review loop prompt (Claude/GPT‑5)

> Generated scaffold on 2025-11-01. Fill in the notebooks, run the critic at the end of every phase, then publish the accompanying Medium article and YouTube walkthrough.

## Projects
- `crispdm_homecredit` — Credit risk (Home Credit Default Risk)
- `semma_bankmarketing` — Campaign response (Bank Marketing)
- `kdd_fraud` — Credit card fraud (highly imbalanced)

## Quick start

```bash
conda create -n ds-methods python=3.11 -y
conda activate ds-methods
pip install -r env/requirements.txt
```

### Run local API
```bash
python crispdm_homecredit/src/serve.py  # FastAPI at http://127.0.0.1:8000/docs
```

### Docker
```bash
docker build -t ds-methods:latest -f docker/Dockerfile .
docker run -p 8000:8000 -p 8501:8501 ds-methods:latest
```

## Tools
- See `tools/open_interpreter.md` and `tools/metagpt_plan.md` to automate repetitive tasks.
