# Reconstructing the Tianjin Explosion from Space

### A Remote-Sensing OSINT Event Reconstruction

On 12 August 2015, two major explosions struck the Ruihai hazardous-goods warehouse in Tianjin. The official investigation records the first explosion at **23:34:06 local time (15:34:06 UTC)** and the second at **23:34:37 local time (15:34:37 UTC)**.

[![BBC News eyewitness footage of the Tianjin explosion](https://img.youtube.com/vi/993wlZ6XFSs/hqdefault.jpg)](https://www.youtube.com/watch?v=993wlZ6XFSs)

*Ground-level context: eyewitness footage published by BBC News.*

The same event was observed from space. CIMSS published a shortwave-infrared animation combining **Himawari-8 (3.9 µm), MTSAT-2 (3.75 µm), and COMS-1 (3.75 µm)**. CIMSS states that all three satellites viewed the explosion and that it generated a strong shortwave-infrared thermal signature. The animation also records the atmospheric evolution after the event.

The following morning, NASA's **Terra/MODIS** instrument observed a dark smoke plume over the Bohai Sea at **02:30 UTC on 13 August**. NASA reports that **Aqua/MODIS** observed the plume again **about three hours later**, after it had moved southeast.

Two simple checks are added to this chronology:

- the change around Tianjin is compared with **31 similar-sized areas elsewhere in the Himawari image** to see whether the same kind of change appears across the scene;
- the later movement of the visible smoke plume is estimated from NASA's Terra and Aqua images.

The Tianjin analysis area changes more than any of the 31 comparison areas. The NASA images indicate that the visible plume core later shifted roughly **40–60 km toward the south-southeast**.

This investigation asks:

> **Can open satellite records independently reconstruct the Tianjin event, distinguish the immediate event-site signal from ordinary nearby variation, and quantify the later displacement of the visible smoke plume?**

This repository deliberately separates two evidence phases rather than pretending that they form a continuous homogeneous time series:

1. **Immediate event record — 12 August:** CIMSS shortwave-infrared satellite sequence.
2. **Later atmospheric aftermath — 13 August:** NASA Terra and Aqua MODIS imagery.

The analysis is a **remote-sensing OSINT event reconstruction**: it reconstructs the observable event chronology and later atmospheric aftermath, without claiming a continuous plume trajectory across the night.

---

## Evidence set

| ID | Time (UTC) | Source | What it establishes |
|---|---:|---|---|
| **H1** | 12 Aug 15:30 | Himawari-8 / 3.9 µm SWIR | Immediate pre-explosion comparison, four minutes before the recorded explosions |
| **H2** | 12 Aug 15:40 | Himawari-8 / 3.9 µm SWIR | First selected Himawari frame after both recorded explosions |
| **H3** | 12 Aug 17:50 | Himawari-8 / 3.9 µm SWIR | Later state in the same Himawari sequence |
| **N1** | 13 Aug 02:30 | Terra / MODIS imagery | Dark smoke plume over the Bohai Sea |
| **N2** | 13 Aug, about three hours after 02:30 UTC | Aqua / MODIS imagery | Later plume; proxy-centroid displacement is ~40–60 km south-southeast from N1 |

**For H1–H3, the primary chronology uses only the top Himawari-8 panel. The full three-panel composites are retained because MTSAT-2 and COMS-1 have different timestamps and must not be treated as simultaneous with Himawari.**

The source animation is preserved in [`images/himawari/`](images/himawari/), and the selected frames are extracted reproducibly with [`scripts/extract_cimss_gif.py`](scripts/extract_cimss_gif.py).

## Key findings

- Himawari-8 shows a clear change around Tianjin across the selected observations.
- The change is larger than those measured in the 31 comparison areas.
- NASA Terra and Aqua imagery shows the later plume moving south-southeast.
- The rendered NASA imagery suggests the visible plume core shifted roughly 40–60 km.
---

# 1. Establishing the event time

The English-language *Process Safety Progress* investigation summary places the Ruihai dangerous-goods warehouse at **39°02′22.98″ N, 117°44′11.64″ E**. In **“Accident Details and Its Impacts”**, it states that the fire began at 10:51 PM local time and was followed by two violent explosions. In **“First Response”**, it gives the exact local explosion times as **11:34:06 PM** and **11:34:37 PM**, describing the second as more violent.

A later open-access *Remote Sensing* study independently reproduces the chronology in 24-hour notation: **23:34:06 local time (UTC+8)** for the first explosion and **23:34:37** for the second, 31 seconds later.

Converted from China Standard Time (UTC+8), the two major explosions occurred at:

- first explosion: **15:34:06 UTC**;
- second, larger explosion: **15:34:37 UTC**.

Sources:

- AIChE / *Process Safety Progress*: https://aiche.onlinelibrary.wiley.com/doi/10.1002/prs.11830
- *Remote Sensing* (2024): https://www.mdpi.com/2072-4292/16/22/4241

The UTC values are **derived conversions in this repository**: eight hours are subtracted from the cited local times. Because the event times come from sources independent of the satellite imagery, they provide the temporal anchor for the H1 → H2 comparison.

---

# 2. Immediate satellite record

CIMSS published a three-panel animation covering the event with:

- **Himawari-8 — 3.9 µm** (top panel);
- **MTSAT-2 — 3.75 µm** (middle panel);
- **COMS-1 — 3.75 µm** (bottom panel).

Original animation:  
https://cimss.ssec.wisc.edu/satellite-blog/wp-content/uploads/sites/5/2015/08/HIMAWARI3PAN_NOMAP_12AUGUST2015_1500_1900anim.gif

CIMSS article:  
https://cimss.ssec.wisc.edu/satellite-blog/archives/19209

CIMSS describes a strong thermal signature in the shortwave-infrared bands and notes that the resulting smoke could be traced as it spread in multiple directions.

## H1 — pre-event comparison

![H1 Himawari-8 3.9 µm at 15:30 UTC](images/himawari/selected/H1_himawari_2015-08-12_1530Z.jpg)

**Himawari-8 time: 15:30 UTC.** This observation precedes the official explosion times by approximately four minutes.

This frame is used only as the immediate pre-event comparison. It is not presented as proof that no fire was already present; the official report states that the site had been burning before the explosions.

## H2 — first selected Himawari frame after the explosions

![H2 Himawari-8 3.9 µm at 15:40 UTC](images/himawari/selected/H2_himawari_2015-08-12_1540Z.jpg)

**Himawari-8 time: 15:40 UTC.** This is the first selected Himawari observation after both explosions recorded at 15:34 UTC.

The comparison **H1 → H2** is therefore temporally bracketed by an independent official event record.

Because the three panels are not always acquired at identical times, the timestamp printed inside each panel is retained in the source image and is not replaced by a single synthetic composite time.

For example, the H2 source composite contains Himawari-8 at **15:40 UTC**, MTSAT-2 at **15:32 UTC**, and COMS-1 at **15:30 UTC**. Only the Himawari panel is post-explosion in that composite.

## H3 — later shortwave-infrared evolution

![H3 Himawari-8 3.9 µm at 17:50 UTC](images/himawari/selected/H3_himawari_2015-08-12_1750Z.jpg)

**Himawari-8 time: 17:50 UTC.** This frame is a **representative later observation**, selected to show the subsequent state within the same CIMSS sequence; it was not chosen by an optimization rule.

It demonstrates continued atmospheric/thermal evolution after the event. It is **not** treated as a georeferenced measurement of plume distance, bearing, or wind speed.

---

# 3. Quantitative and visual comparison of H1 → H2 → H3

The source GIF is a rendered, color-enhanced product rather than calibrated radiance data. Quantitative analysis is therefore restricted to **rendered-image change**, not physical temperature, radiance, energy, or explosive yield.

A fixed **60 × 60 pixel region of interest (ROI)** is drawn around the persistent thermal feature associated with the Tianjin event in the rendered Himawari-8 panel. The ROI was selected from the imagery itself; it was **not independently projected from the warehouse coordinates**. The same pixel coordinates are then held fixed across the selected Himawari observations in the CIMSS sequence.

![H1-H2-H3 with ROI](figures/figure_h1_h2_h3_roi.png)

The corresponding fixed ROI crops are:

![H1-H2-H3 ROI crops](figures/figure_h1_h2_h3_roi_crops.png)

## Rendered local contrast

For each frame, RGB values inside the ROI are reduced to a simple rendered intensity by averaging the three 8-bit channels. The standard deviation of those values is used as a **local contrast metric**.

This metric has no physical temperature unit. Its purpose is only to quantify how visually heterogeneous the same rendered region becomes through time.

| Frame | Time | ROI standard deviation | Extreme rendered pixels* |
|---|---:|---:|---:|
| **H1** | 15:30 | **8.70** | **16** |
| **H2** | 15:40 | **19.78** | **112** |
| **H3** | 17:50 | **13.41** | **54** |

\*Pixels below 60 or above 180 on the derived 0–255 rendered-intensity scale; this threshold is an image-analysis convenience, not a physical classification.

Between H1 and H2, the ROI's rendered-intensity standard deviation rises from **8.70 to 19.78**, an increase of approximately **127%**. The count of extreme rendered pixels rises from **16 to 112**. By H3 at 17:50, the local contrast has fallen to **13.41**, remaining above H1 but below the immediate H2 state.

The broader Himawari sequence gives additional context:

![Himawari ROI contrast time series](figures/figure_himawari_roi_contrast_timeseries.png)

The rendered local contrast differs between the selected H1, H2 and H3 observations. Because this repository does not independently establish a uniform acquisition interval for every frame in the CIMSS animation, it does not use frame spacing as a quantitative temporal test.

This is evidence of a **substantial change in the rendered Himawari SWIR signal inside the fixed analysis ROI**. It is not, by itself, a measurement of explosion energy.

## H2 − H1 difference image

A direct absolute RGB difference between the 15:40 and 15:30 rendered Himawari panels localizes where the displayed product changed most strongly around the site:

![H2 minus H1 rendered difference](figures/figure_h2_minus_h1_difference.png)

Because clouds and atmospheric features also evolve, this difference image is interpreted locally and together with the fixed ROI, not as a general change-detection map.

The complete per-frame measurements are stored in:

```text
data/himawari_roi_timeseries.csv
```

The H1/H2/H3 summary is stored in:

```text
data/H1_H2_H3_metrics.csv
```

Reproduce the metrics and figures with:

```bash
python scripts/analyze_himawari_roi.py
```

---

# 4. Checking the change against the surrounding image

To check whether the H1→H2 change was specific to the Tianjin analysis area, the same image-change measurement was applied to **31 other 60×60-pixel areas** elsewhere in the Himawari image. These comparison areas were selected from the H1 image using the rules recorded in the analysis script, without using their H2 results.

Control candidates must:

- lie on a 30-pixel sampling grid;
- avoid a 180×180 pixel exclusion area around the event ROI;
- fall within the predefined control-search area used by the script and outside the event exclusion zone;
- have an H1 mean rendered intensity within **±10** units of the event ROI;
- have H1 rendered-intensity standard deviation **≤15**.

The comparison areas have broadly similar rendered-image characteristics in H1. The exact search bounds and selection rules are recorded in `scripts/validate_with_controls.py`.

![Comparison-area layout](figures/figure_control_roi_layout.png)

For each comparison area, the same statistic is calculated:

```text
Δcontrast = SD(H2) − SD(H1)
```

The event-site result is:

```text
Event ROI:   +11.08
Control median: +0.00
Control range:  -1.28 to +6.50
Comparison areas: 31
```

The Tianjin analysis area's increase is **larger than all 31 comparison areas** in this test. This is a descriptive comparison, not a formal statistical significance test.

![Tianjin area versus comparison areas](figures/figure_event_vs_controls_distribution.png)

A ranked view shows the same result:

![Ranked event and controls](figures/figure_event_vs_controls_ranked.png)

This supports the narrower claim that the H1→H2 change in the Tianjin analysis area was larger than the changes measured in these 31 comparison areas.

It does not transform the rendered GIF into calibrated physical measurements. The result remains a test of **relative rendered-image change**.

The comparison-area table is available at:

```text
data/matched_control_rois.csv
```

The validation summary is available at:

```text
data/control_validation_summary.csv
```

Reproduce the control selection with:

```bash
python scripts/validate_with_controls.py
```

---


# 5. Next-morning visible smoke

The shortwave-infrared sequence ends on 12 August. The next evidence phase comes from NASA MODIS natural-color imagery on 13 August.

NASA Earth Observatory:  
https://science.nasa.gov/earth/earth-observatory/smoke-over-the-bohai-sea-86410/

NASA states that fires associated with the Tianjin explosions sent dark smoke east and southeast.

## N1 — Terra/MODIS at 02:30 UTC

![Terra MODIS, 13 August 2015](images/modis/terra_2015-08-13_0230Z.jpg)

NASA states that Terra/MODIS acquired this observation at **02:30 UTC (10:30 local time)** on 13 August 2015.

The image independently establishes that a dark plume associated with the Tianjin fires was visible over the Bohai Sea the following morning.

## N2 — Aqua/MODIS, about three hours after Terra

![Aqua MODIS, 13 August 2015](images/modis/aqua_2015-08-13_about3h_after_terra.jpg)

NASA reports that Aqua/MODIS acquired a second observation **about three hours after Terra**, after the plume had moved southeast toward the Shandong Peninsula.

---

# 6. Terra → Aqua plume displacement

NASA states that Terra/MODIS observed the dark plume at **02:30 UTC on 13 August 2015** and that Aqua captured a second image **about three hours later**, after the plume had moved southeast toward the Shandong Peninsula.

The two NASA presentation images use the same 720×480 map frame. An ORB/RANSAC registration check on persistent image features returns an identity transform to numerical precision for the tested matches, supporting direct comparison in the shared pixel frame.

![Terra and Aqua centroids](figures/figure_modis_terra_aqua_centroids.png)

## Dark-smoke proxy

A reproducible proxy mask is restricted to the central Bohai Sea (`x=250–500`, `y=120–340`) to avoid most land, labels and the inset map. Pixels are retained when:

```text
R − B > -15
30 < mean(R,G,B) < 100
```

This rule is not a chemical smoke classifier. It is simply a transparent way to isolate the visually dark brown/gray plume core in the two rendered NASA images.

![MODIS proxy masks](figures/figure_modis_plume_masks.png)

The proxy centroid moves from approximately:

```text
Terra: (369.3, 200.5) px
Aqua:  (389.7, 275.7) px
```

The displacement is **77.9 pixels**. Using the rendered **30 km** scale bar, measured at approximately **46 pixels** in the supplied NASA image, gives:

```text
scale ≈ 0.652 km/pixel
nominal centroid displacement ≈ 50.8 km
bearing ≈ 164.8°
```

In image coordinates this corresponds to approximately **13.3 km east** and **49.0 km south**. The derived direction is therefore south-southeast, consistent with NASA's qualitative description that the plume had moved southeast toward the Shandong Peninsula.

![MODIS displacement](figures/figure_modis_plume_displacement.png)

## Sensitivity

Because the mask operates on rendered RGB values, the estimate is tested across 15 reasonable threshold combinations. The resulting centroid displacement ranges from approximately **42.9 to 61.4 km**, with bearings from **154° to 171°**.

![MODIS threshold sensitivity](figures/figure_modis_displacement_sensitivity.png)

The **50.8 km / 164.8°** value is an image-derived estimate from the rendered NASA figures, not a measurement from georeferenced MODIS Level-1 data. The robust conclusion is therefore simply that the visually dark plume core shifted **roughly 40–60 km toward the south-southeast** between the two NASA observations.

This is an **apparent plume-centroid displacement**, not wind speed. The sensitivity test varies the proxy-mask thresholds; it does not quantify every source of uncertainty, such as the manually read scale bar or analysis-window placement.

Data:

```text
data/modis_plume_displacement_summary.csv
data/modis_plume_sensitivity.csv
data/modis_registration_check.csv
```

Reproduce:

```bash
python scripts/analyze_modis_displacement.py
```

---

# 7. What the evidence supports

The investigation supports a conservative two-phase reconstruction.

### Immediate event phase

- The cited local explosion times convert to **15:34:06 and 15:34:37 UTC**.
- Himawari-8 provides a rendered 3.9 µm SWIR observation at **15:30 UTC** and another at **15:40 UTC**, bracketing the explosion interval.
- In a fixed 60×60 pixel analysis ROI, rendered local contrast increases from **8.70 to 19.78** across H1→H2, approximately **+127%**.
- The corresponding H1→H2 change of **+11.08** exceeds the range observed in the **31 comparison areas** (**−1.28 to +6.50**).
- The selected H3 observation at **17:50 UTC** shows a later state in the same Himawari sequence.

### Next-morning atmospheric phase

- Terra/MODIS independently shows a dark plume over the Bohai Sea at **02:30 UTC on 13 August**.
- Aqua/MODIS shows the plume in a later, more southerly position **about three hours after** the 02:30 UTC Terra observation.
- A reproducible rendered-RGB proxy places the nominal plume-core centroid displacement at **50.8 km, bearing 164.8°**.
- Across 15 threshold combinations, the displacement remains in a **42.9–61.4 km** range with bearings of **154–171°**.
- The robust result is therefore **tens of kilometres of apparent south-southeast plume-core displacement**, consistent with NASA's qualitative description of southeastward movement toward the Shandong Peninsula.

Taken together, the sources independently support:

```text
15:30 UTC        15:34 UTC        15:40 UTC             17:50 UTC
H1 Himawari ───► explosions ───► H2 Himawari ───────► H3 Himawari
   SWIR                                  │
                                        │ overnight observational gap
                                        ▼
13 Aug 02:30 UTC                                      about three hours later
N1 Terra/MODIS ───────────────────────────────────────────► N2 Aqua/MODIS
dark plume                                                plume shifted SSE
```

The analysis does **not** fill the overnight observational gap with an inferred trajectory.

---

# 8. What the evidence does **not** support

This repository does **not** claim a continuous satellite-derived trajectory from 15:34 UTC on 12 August to the MODIS observations on 13 August.

The current evidence does not justify deriving:

- a continuous plume trajectory or centroid speed across the overnight observational gap;
- wind speed from the Terra→Aqua apparent centroid displacement;
- physical temperature, radiance, energy, or explosive yield from the rendered SWIR GIF;
- chemical composition or toxicity of the visible plume;
- blast pressure or structural damage from these atmospheric products;
- formal statistical significance from the 31 comparison areas alone;
- an exact Aqua acquisition time: the NASA Earth Observatory source used here states only **“about three hours later.”**

The CIMSS imagery is shortwave infrared; the NASA Earth Observatory images are rendered MODIS observations. They are complementary observations, not interchangeable measurements.

---


# 9. Reproducibility

The original CIMSS GIF is stored unchanged at:

```text
images/himawari/HIMAWARI3PAN_NOMAP_12AUGUST2015_1500_1900anim.gif
```

Extract every GIF frame and regenerate H1–H3 with:

```bash
python scripts/extract_cimss_gif.py
```

Selected frame definitions are stored in:

```text
data/selected_frames.csv
```

The event chronology is stored in:

```text
data/event_timeline.csv
```

Source provenance is stored in:

```text
data/sources.csv
```

Quantitative Himawari outputs are stored in:

```text
data/H1_H2_H3_metrics.csv
data/himawari_roi_timeseries.csv
data/matched_control_rois.csv
data/control_validation_summary.csv
```

MODIS displacement outputs are stored in:

```text
data/modis_registration_check.csv
data/modis_plume_displacement_summary.csv
data/modis_plume_sensitivity.csv
```

Reproduce the two quantitative phases with:

```bash
python scripts/analyze_himawari_roi.py
python scripts/validate_with_controls.py
python scripts/analyze_modis_displacement.py
```

File hashes are stored in:

```text
data/checksums.sha256
```

---


# Sources

**CIMSS Satellite Blog — Explosion in Tianjin, China**  
https://cimss.ssec.wisc.edu/satellite-blog/archives/19209

**CIMSS — original three-satellite SWIR animation**  
https://cimss.ssec.wisc.edu/satellite-blog/wp-content/uploads/sites/5/2015/08/HIMAWARI3PAN_NOMAP_12AUGUST2015_1500_1900anim.gif

**NASA Earth Observatory — Smoke over the Bohai Sea**  
https://science.nasa.gov/earth/earth-observatory/smoke-over-the-bohai-sea-86410/

**AIChE / Process Safety Progress — Tianjin Explosion Investigation Report Summary**  
https://aiche.onlinelibrary.wiley.com/doi/10.1002/prs.11830

**Process Safety Progress — Anatomy of Tianjin Port fire and explosion: Process and causes**  
https://aiche.onlinelibrary.wiley.com/doi/10.1002/prs.11837

**BBC News eyewitness video**  
https://www.youtube.com/watch?v=993wlZ6XFSs