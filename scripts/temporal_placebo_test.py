from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "himawari_roi_timeseries.csv")

df["delta_std_from_prev"] = df["roi_std_rendered_intensity"].diff()
df["abs_delta_std_from_prev"] = df["delta_std_from_prev"].abs()

rows = []
for i in range(1, len(df)):
    rows.append({
        "interval_start_utc": df.loc[i-1, "timestamp_utc"],
        "interval_end_utc": df.loc[i, "timestamp_utc"],
        "delta_std": float(df.loc[i, "delta_std_from_prev"]),
        "abs_delta_std": float(df.loc[i, "abs_delta_std_from_prev"]),
        "is_explosion_interval": (
            df.loc[i-1, "timestamp_utc"].endswith("15:30:00Z")
            and df.loc[i, "timestamp_utc"].endswith("15:40:00Z")
        ),
    })

out = pd.DataFrame(rows)
out["rank_signed_increase_desc"] = out["delta_std"].rank(method="min", ascending=False).astype(int)
out["rank_abs_change_desc"] = out["abs_delta_std"].rank(method="min", ascending=False).astype(int)
out.to_csv(ROOT / "data" / "himawari_temporal_placebo_intervals.csv", index=False)
