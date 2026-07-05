# Data and licensing

## Embeddings

Pre-extracted UNI2-h slide embeddings for TCGA (and CPTAC, PANDA) are published on
Hugging Face at MahmoodLab/UNI2-h-features. Access is gated: create a Hugging Face
account, open the dataset page, and accept the terms to enable download.

## Labels

Clinical and molecular labels for TCGA cases (tumor type, MSI status, molecular subtype,
survival) are available from:

- cBioPortal (web API and bulk downloads)
- the GDC data portal

Join labels to embeddings on the TCGA case or slide identifier.

## License and attribution

The UNI and UNI2 models and their pre-extracted embeddings are released under
CC-BY-NC-ND 4.0. In practice this means:

- Non-commercial, academic research use only.
- Attribution required (cite the Nature Medicine paper).
- No derivatives may be redistributed, and the embeddings and weights may not be
  re-published.

  Consequences for this repo:

  - Do not commit embeddings or model weights. They live in data/, which is gitignored.
  - Publish only your own code, results, and figures.
  - Each person who wants the data must register and accept the terms individually.

  TCGA itself is a public NCI and NHGRI resource. Follow GDC data access policies for any
  controlled-access items.
  
