import argparse
import os
from utils import *
from pathlib import Path

conversion_mappings = {
    ".png": png_to_webm,
    '.gif': gif_to_webm
}

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', default=['peepo_emotes'], nargs='+', help='fpath to a directory containing src/ and mappings.json')
    return parser.parse_args()

def convert_to_webm(dir: str):
    files = os.listdir(os.path.join(dir, 'src'))
    for file in files:
        fpath = Path(os.path.join(dir, 'src', file))
        ext = fpath.suffix
        if ext in conversion_mappings.keys():
            print(f"Converting {file} to .webm format...")
            conversion_mappings[ext](fpath)
            os.remove(fpath)
            
def main():
    args = parse_arguments()
    for dir in args.dir:
        convert_to_webm(dir)

if __name__ == '__main__':
    main()