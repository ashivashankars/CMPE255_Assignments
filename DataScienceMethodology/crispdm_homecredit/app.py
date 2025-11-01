import streamlit as st, pandas as pd, joblib, pathlib, json
from sklearn.preprocessing import OneHotEncoder

st.title("Home Credit — Probability of Default (Demo)")

MODEL_PATH = pathlib.Path(__file__).resolve().parents[1] / "data" / "processed" / "baseline_logreg.pkl"
if not MODEL_PATH.exists():
    st.warning("Trained model not found. Run the modeling notebook to create baseline_logreg.pkl.")
else:
    model = joblib.load(MODEL_PATH)
    st.success("Model loaded. Provide a few example fields or upload a CSV.")

    uploaded = st.file_uploader("Upload CSV of application rows (optional)", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
        proba = model.predict_proba(df)[:,1]
        out = df.copy()
        out['prob_default'] = proba
        st.dataframe(out.head(20))
        st.download_button("Download scored CSV", out.to_csv(index=False).encode("utf-8"), "scored.csv")

    st.subheader("Quick single prediction")
    # minimal subset (free-form JSON for flexibility)
    payload = st.text_area("Paste JSON of a single row (keys = feature names)", value='{}', height=150)
    if st.button("Score JSON"):
        try:
            row = json.loads(payload or '{}')
            df = pd.DataFrame([row])
            prob = float(model.predict_proba(df)[:,1][0])
            st.metric("Estimated PD", f"{prob:.3f}")
        except Exception as e:
            st.error(f"Scoring failed: {e}")
