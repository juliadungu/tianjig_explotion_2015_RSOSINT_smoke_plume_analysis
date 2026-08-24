from pathlib import Path
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
ROI = (610, 135, 670, 195)

records = []
for idx in range(3, 28):
    src = ROOT / "images" / "himawari" / "extracted" / f"frame_{idx:02d}.jpg"
    him = np.array(Image.open(src).convert("RGB"))[:320]
    x1, y1, x2, y2 = ROI
    roi = him[y1:y2, x1:x2]
    gray = roi.mean(axis=2)

    minutes = (idx - 3) * 10
    hh = 15 + minutes // 60
    mm = minutes % 60
    timestamp = f"2015-08-12T{hh:02d}:{mm:02d}:00Z"

    records.append({
        "gif_frame_index": idx,
        "timestamp_utc": timestamp,
        "roi_mean_rendered_intensity": float(gray.mean()),
        "roi_std_rendered_intensity": float(gray.std()),
        "roi_p05_rendered_intensity": float(np.percentile(gray, 5)),
        "roi_p95_rendered_intensity": float(np.percentile(gray, 95)),
        "roi_extreme_pixel_count": int(((gray < 60) | (gray > 180)).sum()),
        "roi_pixel_count": int(gray.size),
    })

df = pd.DataFrame(records)
df.to_csv(ROOT / "data" / "himawari_roi_timeseries.csv", index=False)

fig, ax = plt.subplots(figsize=(10, 4.8))
ax.plot(df["timestamp_utc"], df["roi_std_rendered_intensity"], marker="o")
ax.set_ylabel("ROI standard deviation (rendered 8-bit intensity)")
ax.set_title("Rendered local contrast in fixed Himawari event-site ROI")
ax.tick_params(axis="x", rotation=60)
fig.tight_layout()
fig.savefig(ROOT / "figures" / "figure_himawari_roi_contrast_timeseries.png", dpi=200)
