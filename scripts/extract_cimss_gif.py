#!/usr/bin/env python3
from pathlib import Path
from PIL import Image
import csv

ROOT = Path(__file__).resolve().parents[1]
GIF = ROOT / 'images/himawari/HIMAWARI3PAN_NOMAP_12AUGUST2015_1500_1900anim.gif'
OUT = ROOT / 'images/himawari/extracted'
SELECTED = ROOT / 'images/himawari/selected'
CSV = ROOT / 'data/selected_frames.csv'

OUT.mkdir(parents=True, exist_ok=True)
SELECTED.mkdir(parents=True, exist_ok=True)

with Image.open(GIF) as im:
    frame_count = im.n_frames
    for i in range(frame_count):
        im.seek(i)
        frame = im.convert('RGB')
        frame.save(OUT / f'frame_{i:02d}.jpg', quality=95)

with open(CSV, newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

with Image.open(GIF) as im:
    for row in rows:
        idx = int(row['gif_frame_index'])
        im.seek(idx)
        frame = im.convert('RGB')
        destination = ROOT / row['output_file']
        destination.parent.mkdir(parents=True, exist_ok=True)
        frame.save(destination, quality=95)

print(f'Extracted {frame_count} source frames and {len(rows)} selected frames.')
