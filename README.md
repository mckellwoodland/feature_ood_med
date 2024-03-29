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

This repository contains a fork of the official SegVol repository as a submodule. To use our code, move to the `feature_ood_med` branch of the submodule.

### Docker
```
docker build -t seg_vol SegVol/.
```
```
docker run -it --rm -v $(pwd):/workspace seg_vol
```

### Inference

If your system does not have internet access, download [OpenAI's CLIP model from HuggingFace](https://huggingface.co/openai/clip-vit-base-patch32) and place the files in `SegVol/model/CLIP`. If your system does have internet access, you can delete the `clip_ckpt` argument from the `SegVol/script/inference_demo.sh` script.

To run the demo case, download the files from [HuggingFace](https://huggingface.co/BAAI/SegVol). Place the NIfTI files in `SegVol/data/`. Place the model in `SegVol/model/`. The results will be placed in `SegVol/logs/demo`.
```
bash SegVol/script/inference_demo.sh
```

To test on your own data
1. Generate the JSON file using `utils/create_json.py`. The images and corresponding labels should be in separate folders. When the file contents of the two directories are sorted, the image file should correspond to the label file.
```
usage: create_json.py [-h] -i IMG_DIR -l LABEL_DIR -o OUTPUT_FILE

Required Arguments:
  -i IMG_DIR, --img_dir IMG_DIR
                        Path to the image directory.
  -l LABEL_DIR, --label_dir LABEL_DIR
                        Path to the label directory.
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Path to the JSON file to be outputed.
```
2. Update the `SegVol/script/inference.sh` file with where to put your logs and your config file.
## CLIP-Driven Universal Model

## Multi-Talent

## UniSeg

## STU-Net

# Acknowledgments

Research reported in this publication was supported in part by the Tumor Measurement Initiative through the MD Anderson Strategic Initiative Development Program (STRIDE), the Helen Black Image Guided Fund, the Image Guided Cancer Therapy Research Program at The University of Texas MD Anderson Cancer Center, a generous gift from the Apache Corporation, and the National Cancer Institute of the National Institutes of Health under award numbers R01CA221971, P30CA016672, and R01CA235564.

# Citation

# References

<!--1. A. L. Simpson *et al.* A large annotated medical image dataset for the development and evaluation of segmentation algorithms. 2019, arXiv:1902.09063.-->
