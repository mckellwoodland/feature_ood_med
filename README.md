# Out-of-Distribution Detection for Medical Imaging Segmentation Foundation Models - Official Repository

**Out-of-Distribution Detection for Medical Imaging Segmentation Foundation Models**

McKell Woodland, Ankit B. Patel, & Kristy K. Brock

Abstract: *Foundation models, trained on vast amounts of data and applied to numerous downstream tasks, are achieving state-of-the-art results on a wide variety of medical imaging segmentation tasks. For robust clinical deployment, detecting when segmentation models are presented with scans beyond their scope is critical. However, most foundation segmentation models do not have in-built out-of-distribution (OOD) detection functionality. Furthermore, the post hoc application of OOD detection techniques to foundation segmentation models is challenging because many techniques require training scheme modifications or access to the training dataset. This work performed OOD detection using the features of the foundation segmentation models, requiring neither training scheme modifications nor access to the entire training dataset and incurring minimal cost. The Mahalanobis distance, Gram matrices, and spectral analysis were applied to dimensionality-reduced features extracted from all encoding layers of five foundation models (SegVol, CLIP-Driven Universal Model, Multi-Talent, UniSeg, and STU-Net) evaluated on 20 computed tomography segmentation tasks.*

<!--# Docker

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
  --in_dir IN_DIR    Path to the directory with tar files.
  --out_dir OUT_DIR  Path to the directory to put unzipped files into.
```
-->
# Segmentation Models

## SegVol

This repository contains a fork of the official SegVol repository as a submodule. The branch `feature_ood_med` has all of our changes and instructions for use.

## CLIP-Driven Universal Model

## Multi-Talent

## UniSeg

## STU-Net

# Acknowledgments

Research reported in this publication was supported in part by the Tumor Measurement Initiative through the MD Anderson Strategic Initiative Development Program (STRIDE), the Helen Black Image Guided Fund, the Image Guided Cancer Therapy Research Program at The University of Texas MD Anderson Cancer Center, a generous gift from the Apache Corporation, and the National Cancer Institute of the National Institutes of Health under award numbers R01CA221971, P30CA016672, and R01CA235564.

# Citation

# References

<!--1. A. L. Simpson *et al.* A large annotated medical image dataset for the development and evaluation of segmentation algorithms. 2019, arXiv:1902.09063.-->
