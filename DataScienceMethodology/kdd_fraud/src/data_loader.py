import os, subprocess, pandas as pd, pathlib, zipfile

RAW_DIR = pathlib.Path(__file__).resolve().parents[1] / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

def kaggle_download():
    """Download the 'creditcardfraud' dataset from Kaggle (mlg-ulb/creditcardfraud)."""
    try:
        subprocess.check_call(["python","-m","pip","-q","install","kaggle"])
        subprocess.check_call(["kaggle","datasets","download","-d","mlg-ulb/creditcardfraud","-p", str(RAW_DIR)])
        for z in RAW_DIR.glob("*.zip"):
            with zipfile.ZipFile(z, 'r') as zip_ref:
                zip_ref.extractall(RAW_DIR)
        return True
    except Exception as e:
        print("Kaggle download failed or not configured:", e)
        print("Place creditcard.csv into", RAW_DIR)
        return False

def load_creditcard():
    p = RAW_DIR / "creditcard.csv"
    if not p.exists():
        print("creditcard.csv not found. Attempting Kaggle download...")
        kaggle_download()
    if not p.exists():
        raise FileNotFoundError(f"Missing {p}. Use Kaggle API or copy the file locally.")
    return pd.read_csv(p)
