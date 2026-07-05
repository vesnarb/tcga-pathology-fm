# TCGA Pathology Foundation Model Playground

Predicting clinically meaningful labels from TCGA histopathology using pre-extracted
embeddings from a pathology foundation model (UNI2), with honest classical baselines
for comparison.

## Why this project

Computational pathology has largely moved to foundation models that turn whole-slide
images into compact embeddings. This repo explores how far a lightweight classifier
on top of those embeddings gets on public TCGA data, and measures it against simple
baselines so any added value is demonstrated rather than assumed.

No GPU is required. The heavy image encoding is already done and published as
pre-extracted embeddings, so the work here is loading vectors and training small heads.

## Approach

1. Use the publicly released UNI2-h slide embeddings for TCGA.
2. Join them to public clinical and molecular labels from cBioPortal and GDC.
3. Train and evaluate a light head (logistic regression, then XGBoost) on a chosen target.
4. Report against a naive majority-class baseline and a simple classical baseline, with
   clear metrics and calibration.

   ## First target (draft)

   Headline task: MSI status (binary, clinically relevant for immunotherapy selection).
   Warmup task: pan-cancer tumor-type classification. Final target to be confirmed.

   ## Setup

   Reproducible environment via pixi:

   pixi install
   pixi run lab

   If you later want to run the UNI2 encoder itself rather than use the pre-extracted
   embeddings, pin Python 3.10 and add torch and timm. See DATA.md.

   ## Data and license

   Details in DATA.md. Short version: the UNI2 model and its embeddings are released under
   CC-BY-NC-ND 4.0 for non-commercial research, are gated on Hugging Face, and must not be
   redistributed. This repo therefore contains code and results only. No embeddings or
   weights are committed.

   ## Roadmap

   - [x] Repo scaffold and environment
   - [ ] Request Hugging Face access and download an embedding slice
   - [ ] Inspect the embedding schema and join to labels
   - [ ] Baseline: majority class and a simple classical model
   - [ ] Foundation-model head: logistic regression
   - [ ] Foundation-model head: XGBoost
   - [ ] Evaluation, calibration, and write-up

   ## References

   UNI / UNI2: Chen et al., Towards a General-Purpose Foundation Model for Computational
   Pathology, Nature Medicine, 2024.
   
