import streamlit as st, pandas as pd, joblib, pathlib, numpy as np
st.title("Credit Card Fraud — Anomaly Scoring (Demo)")
PTH = pathlib.Path(__file__).resolve().parents[1] / "data" / "processed" / "iforest_stub.pkl"
if not PTH.exists():
    st.warning("Run the Data Mining notebook to generate iforest_stub.pkl (threshold stub).")
else:
    cfg = joblib.load(PTH)
    st.info(f"Using saved threshold: {cfg.get('threshold')} (demo only)")
    uploaded = st.file_uploader("Upload CSV with features (V1..V28, Time, Amount)", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
        # For demo, use a simple z-score on Amount as proxy score (since model object not saved here)
        score = (df['Amount'] - df['Amount'].mean())/ (df['Amount'].std()+1e-6)
        df_out = df.copy()
        df_out['anomaly_score_demo'] = np.abs(score)
        df_out['flag'] = (df_out['anomaly_score_demo'] > 3).astype(int)
        st.dataframe(df_out.head(20))
        st.download_button("Download with flags", df_out.to_csv(index=False).encode('utf-8'), "scored_flags.csv")
