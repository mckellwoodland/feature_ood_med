# Feature-based Out-of-Distribution Detection for Medical Imaging Segmentation - Official Repository

**Feature-based Out-of-Distribution Detection for Medical Imaging Segmentation**
McKell Woodland, Ankit B. Patel, & Kristy K. Brock

Abstract: *The ability to detect when medical imaging segmentation models have performed poorly is crucial for their deployment in clinical settings. While methods such as MC dropout and ensembling perform well, they require modifications to the training scheme and are expensive at inference. The current work predicts inadequate performance using the segmentation model’s features, requiring no training scheme modifications, and incurring minimal cost. Mahalanobis distance, Gram matrices, and spectral analysis were applied to dimensionality-reduced features extracted from all encoding layers of 3 segmentation architectures (nnU-net, Swin Transformer, 3D U-net) trained on 10 segmentation datasets (MSD).*

# Docker

```
docker build -t feature_ood_med .
```

# Data

Download the data from the [Medical Segmentation Decathlon](http://medicaldecathlon.com/)<sup>1</sup>. Put all the tar files in one folder.

Unzip the tar files.
```
docker run -it --rm -v "$PWD":/workspace feature_ood_med python utils/preprocess_msd.py --in_dir {IN_DIR} --out_dir {OUT_DIR}
```

```
usage: preprocess_msd.py [-h] --in_dir IN_DIR --out_dir OUT_DIR

Required Arguments:
  --in_dir IN_DIR    Path to directory with tar files.
  --out_dir OUT_DIR  Path to directory to put unzipped files into.
```

# Segmentation Models
## CLIP-Driven Universal Model

## Swin UNETR

## DiNTS

## nnU-net

## Model Genesis

# Acknowledgments

Research reported in this publication was supported in part by the Tumor Measurement Initiative through the MD Anderson Strategic Initiative Development Program (STRIDE), the Helen Black Image Guided Fund, the Image Guided Cancer Therapy Research Program at The University of Texas MD Anderson Cancer Center, a generous gift from the Apache Corporation, and the National Cancer Institute of the National Institutes of Health under award numbers R01CA221971, P30CA016672, and R01CA235564.

# Citation

# References

1. A. L. Simpson *et al.* A large annotated medical image dataset for the development and evaluation of segmentation algorithms. 2019, arXiv:1902.09063.
