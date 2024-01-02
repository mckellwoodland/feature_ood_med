# Feature-based Out-of-Distribution Detection for Medical Imaging Segmentation - Official Repository

**Feature-based Out-of-Distribution Detection for Medical Imaging Segmentation**
McKell Woodland, Ankit B. Patel, & Kristy K. Brock

Abstract: *The ability to detect when medical imaging segmentation models have performed poorly is crucial for their deployment in clinical settings. While methods such as MC dropout and ensembling perform well, they require modifications to the training scheme and are expensive at inference. The current work predicts inadequate performance using the segmentation model’s features, requiring no training scheme modifications, and incurring minimal cost. Mahalanobis distance, Gram matrices, and spectral analysis were applied to dimensionality-reduced features extracted from all encoding layers of 3 segmentation architectures (nnU-net, Swin Transformer, 3D U-net) trained on 10 segmentation datasets (MSD).*

# Docker

```
docker build -t feature_ood_med .
```

# Data

Download the data from the Medical Segmentation Decathlon<sup>1</sup>. Put all the tar files in one folder.

Build the docker container.
```
docker build -t feature_ood_med .
```

Unzip the tar files.
```
docker run -it --rm -v "$PWD":/workspace feature_ood_med python utils/preprocess_msd.py \
  --in_dir {IN_DIR} \
  --out_dir {OUT_DIR}
```
# Acknowledgments

# Citation

# References
