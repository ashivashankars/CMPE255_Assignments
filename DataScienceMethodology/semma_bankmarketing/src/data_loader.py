import pandas as pd, pathlib

RAW_DIR = pathlib.Path(__file__).resolve().parents[1] / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

UCI_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00222/bank-additional.zip"

def load_bank_data():
    """Try local CSV first; else fetch from UCI."""
    local = RAW_DIR / "bank-additional" / "bank-additional-full.csv"
    if local.exists():
        return pd.read_csv(local, sep=';')
    # Attempt remote fetch
    try:
        import requests, zipfile, io, os
        r = requests.get(UCI_URL, timeout=60)
        r.raise_for_status()
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(RAW_DIR)
        return pd.read_csv(local, sep=';')
    except Exception as e:
        raise FileNotFoundError(f"Could not load dataset. Place bank-additional-full.csv under {local.parent}. Error: {e}")
