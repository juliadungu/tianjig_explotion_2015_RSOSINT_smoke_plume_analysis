from pathlib import Path
from PIL import Image
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
EVENT = (610, 135, 670, 195)
EXCLUSION = (550, 75, 730, 255)
ROI_SIZE = 60

h1 = np.array(Image.open(ROOT / "images/himawari/selected/H1_himawari_2015-08-12_1530Z.jpg").convert("RGB"))
h2 = np.array(Image.open(ROOT / "images/himawari/selected/H2_himawari_2015-08-12_1540Z.jpg").convert("RGB"))

def metrics(arr, box):
    x1, y1, x2, y2 = box
    gray = arr[y1:y2, x1:x2].mean(axis=2)
    return float(gray.mean()), float(gray.std())

event_mean_h1, event_std_h1 = metrics(h1, EVENT)
_, event_std_h2 = metrics(h2, EVENT)

rows = []
cid = 1
for y in range(20, 241, 30):
    for x in range(50, 901, 30):
        box = (x, y, x + ROI_SIZE, y + ROI_SIZE)
        ex = EXCLUSION
        overlaps = not (box[2] <= ex[0] or box[0] >= ex[2] or box[3] <= ex[1] or box[1] >= ex[3])
        if overlaps:
            continue

        mean1, std1 = metrics(h1, box)
        mean2, std2 = metrics(h2, box)

        if abs(mean1 - event_mean_h1) <= 10 and std1 <= 15:
            rows.append({
                "control_id": f"C{cid:02d}",
                "x1": x, "y1": y, "x2": x + ROI_SIZE, "y2": y + ROI_SIZE,
                "h1_mean": mean1, "h1_std": std1,
                "h2_mean": mean2, "h2_std": std2,
                "delta_std_h2_minus_h1": std2 - std1,
            })
            cid += 1

pd.DataFrame(rows).to_csv(ROOT / "data/matched_control_rois.csv", index=False)
