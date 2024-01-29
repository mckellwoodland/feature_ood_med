"""
This script creates a JSON file that describes a directory with images and labels.

This file assumes that, when sorted, the filenames in the image directory correspond to the images in the label directory.

Modified from the generate_dataset_json function within https://github.com/BAAI-DCAI/SegVol/blob/main/data_process/train_data_process.py.
"""

# Imports.
import argparse
import json
import os

# Arguments
parser = argparse.ArgumentParser()
parser._action_groups.pop()
required = parser.add_argument_group('Required Arguments')
required.add_argument('-i', '--img_dir', required=True, type=str, help="Path to the image directory.")
required.add_argument('-l', '--label_dir', required=True, type=str, help="Path to the label directory.")
required.add_argument('-o', '--output_file', required=True, type=str, help="Path to the JSON file to be outputed.")
args = parser.parse_args()
img_dir = args.img_dir
label_dir = args.label_dir
out_f = args.output_file
        
# Main code.
img_paths = sorted([os.path.join(img_dir, f) for f in sorted(os.listdir(img_dir))])
label_paths = sorted([os.path.join(label_dir, f) for f in sorted(os.listdir(label_dir))])
data = list(zip(img_paths, label_paths))
dataset = {'testing': [{'image': ct_path, 
                        'label': gt_path} for ct_path, gt_path in data]}
with open(out_f, 'w') as f:
    print(f'{out_f} dump')
    json.dump(dataset, f, indent=2)
        