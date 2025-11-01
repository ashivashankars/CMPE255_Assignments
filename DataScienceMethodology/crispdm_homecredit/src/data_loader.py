import os, subprocess, pandas as pd, zipfile, pathlib

RAW_DIR = pathlib.Path(__file__).resolve().parents[1] / "data" / "raw"
PROC_DIR = pathlib.Path(__file__).resolve().parents[1] / "data" / "processed"
RAW_DIR.mkdir(parents=True, exist_ok=True)
PROC_DIR.mkdir(parents=True, exist_ok=True)

def kaggle_download():
    """Download Home Credit Default Risk using Kaggle CLI if available."""
    try:
        subprocess.check_call(["python","-m","pip","-q","install","kaggle"])
        subprocess.check_call(["kaggle","competitions","download","-c","home-credit-default-risk","-p", str(RAW_DIR)])
        # Unzip all archives
        for z in RAW_DIR.glob("*.zip"):
            with zipfile.ZipFile(z, 'r') as zip_ref:
                zip_ref.extractall(RAW_DIR)
        return True
    except Exception as e:
        print("Kaggle download failed or Kaggle CLI not configured:", e)
        print("Place CSVs (application_train.csv, application_test.csv, bureau.csv, etc.) into", RAW_DIR)
        return False

def load_application_train():
    p = RAW_DIR / "application_train.csv"
    if not p.exists():
        print("application_train.csv not found. Attempting Kaggle download...")
        kaggle_download()
    if not p.exists():
        raise FileNotFoundError(f"Missing {p}. Download via Kaggle or copy it locally.")
    return pd.read_csv(p)

def quick_baseline(df=None, target_col="TARGET"):
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import roc_auc_score
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.compose import ColumnTransformer
    from sklearn.pipeline import Pipeline
    from sklearn.impute import SimpleImputer
    from sklearn.linear_model import LogisticRegression

    if df is None:
        df = load_application_train()
    y = df[target_col].astype(int)
    X = df.drop(columns=[target_col])
    cat_cols = [c for c in X.columns if X[c].dtype == "object"]
    num_cols = [c for c in X.columns if c not in cat_cols]

    pre = ColumnTransformer([
        ("num", SimpleImputer(strategy="median"), num_cols),
        ("cat", Pipeline([("impute", SimpleImputer(strategy="most_frequent")),
                          ("oh", OneHotEncoder(handle_unknown="ignore"))]), cat_cols)
    ])
    clf = Pipeline([("pre", pre),
                    ("model", LogisticRegression(max_iter=200, n_jobs=None if hasattr(LogisticRegression,'n_jobs') else None))])
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    clf.fit(Xtr, ytr)
    proba = clf.predict_proba(Xte)[:,1]
    auc = roc_auc_score(yte, proba)
    return clf, auc
