# Image Denoising using Autoencoders

An end-to-end implementation of an **Autoencoder** designed to remove synthetic noise (e.g., Gaussian noise) from corrupted images, restoring the underlying clean representation.

---

## Overview

Image denoising is a core task in computer vision and image processing. Traditional spatial filters (such as Gaussian or median filters) often blur sharp edges while reducing noise. A **Convolutional Autoencoder (CAE)** learns a non-linear mapping from corrupted image inputs to clean image targets:

1. **Encoder**: Compresses the noisy input image into a compact latent feature representation while filtering out high-frequency noise artifacts.
2. **Decoder**: Reconstructs the original, noise-free spatial details from the latent representation.

---

## Project Structure

```text
Image-Denoising/
│
├── Image Denoising.ipynb    # Main notebook containing model training, evaluation, and visualizations
├── .gitignore               # Ignored system and cache files
└── README.md                # Project documentation
