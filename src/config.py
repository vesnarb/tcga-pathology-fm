from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
RESULTS_DIR = ROOT / "results"

# Gated Hugging Face dataset of pre-extracted UNI2-h embeddings (see DATA.md).
HF_EMBEDDINGS_REPO = "MahmoodLab/UNI2-h-features"
