### Critique Prompt — CRISP-DM → Modeling
Goal: Choose, train, and tune algorithms; compare against baseline.

Prompt Example:

🤖 Run the “Modeling” phase of CRISP-DM. Start with a baseline (DummyRegressor or DummyClassifier), then train and tune several candidate models (Ridge, Lasso, RandomForest, GradientBoosting, etc.) with small grids using cross-validation. Report MAE, RMSE, R² (or appropriate metrics). Plot residuals, feature importances, and learning curves. Identify the champion model and justify why.

Deliverables expected:

Baseline + champion model

Model comparison table

Metrics summary (train, CV, test)

Diagnostic plots (residuals, predicted vs actual)

Serialized model artifact
