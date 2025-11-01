import streamlit as st, pandas as pd, joblib, pathlib
st.title("Bank Marketing — Response Propensity (Demo)")
MODEL_PATH = pathlib.Path(__file__).resolve().parents[1] / "data" / "processed" / "bank_logreg.pkl"
if not MODEL_PATH.exists():
    st.warning("Run the Model notebook to generate bank_logreg.pkl.")
else:
    model = joblib.load(MODEL_PATH)
    st.success("Model loaded. Upload CSV to score or provide a single row.")
    uploaded = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded, sep=None, engine='python')
        proba = model.predict_proba(df)[:,1]
        out = df.copy(); out['response_prob'] = proba
        st.dataframe(out.head(20))
        st.download_button("Download scored CSV", out.to_csv(index=False).encode("utf-8"), "scored.csv")
