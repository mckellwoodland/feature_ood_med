"""
Unzip the MSD datasets.
"""

# Imports
import argparse
import os
import tarfile
import tqdm

# Arguments
parser = argparse.ArgumentParser()
parser._action_groups.pop()
required = parser.add_argument_group('Required Arguments')
required.add_argument('--in_dir', required=True, type=str, help='Path to the directory with tar files.')
required.add_argument('--out_dir', required=True, type=str, help='Path to the directory to put unzipped files into.')
args = parser.parse_args()
in_dir = args.in_dir
out_dir = args.out_dir
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

# Main Code
for tar_file in tqdm.tqdm(os.listdir(in_dir)):
    with tarfile.open(os.path.join(in_dir, tar_file)) as tar:
        tar.extractall(path=out_dir)
