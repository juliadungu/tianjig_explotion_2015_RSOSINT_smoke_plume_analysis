# Tracking the Tianjin Explosion from Space

### A reproducible RSOSINT reconstruction using shortwave-infrared and MODIS imagery

On 12 August 2015, two major explosions struck the Ruihai hazardous-goods warehouse in Tianjin. The official investigation records the first explosion at **23:34:06 local time (15:34:06 UTC)** and the second at **23:34:37 local time (15:34:37 UTC)**.

[![BBC News eyewitness footage of the Tianjin explosion](https://img.youtube.com/vi/993wlZ6XFSs/hqdefault.jpg)](https://www.youtube.com/watch?v=993wlZ6XFSs)

*Ground-level context: eyewitness footage published by BBC News.*

The same event was observed from space. CIMSS published a shortwave-infrared animation combining **Himawari-8 (3.9 µm), MTSAT-2 (3.75 µm), and COMS-1 (3.75 µm)**. CIMSS states that all three satellites viewed the explosion and that it generated a strong shortwave-infrared thermal signature. The animation also records the atmospheric evolution after the event.

The following morning, NASA's **Terra/MODIS** instrument observed a dark smoke plume over the Bohai Sea at **02:30 UTC on 13 August**. NASA reports that **Aqua/MODIS** observed the plume again about three hours later after it had moved southeast.

This investigation asks:

> **Can open satellite records independently reconstruct the Tianjin event from the immediate shortwave-infrared signature to the visible smoke plume observed the following morning?**

This repository deliberately separates two evidence phases rather than pretending that they form a continuous homogeneous time series:

1. **Immediate event record — 12 August:** CIMSS shortwave-infrared satellite sequence.
2. **Later atmospheric aftermath — 13 August:** NASA Terra and Aqua MODIS natural-color imagery.

The analysis therefore reconstructs an **event chronology**, not a continuous plume trajectory across the entire night.

---

## Evidence set

| ID | Time (UTC) | Source | What it establishes |
|---|---:|---|---|
| **H1** | 12 Aug 15:30 | Himawari-8 / MTSAT-2 / COMS-1 SWIR composite | Selected pre-event comparison frame, before the recorded 15:34 explosions |
| **H2** | 12 Aug 15:40 | Himawari-8 / MTSAT-2 / COMS-1 SWIR composite | First selected Himawari frame after both recorded explosions |
| **H3** | 12 Aug 17:50 | Himawari-8 / MTSAT-2 / COMS-1 SWIR composite | Later shortwave-infrared atmospheric/thermal evolution |
| **N1** | 13 Aug 02:30 | Terra / MODIS | Dark smoke plume over the Bohai Sea |
| **N2** | ~13 Aug 05:30 | Aqua / MODIS | Later visible plume after southeastward displacement; NASA gives this time only as "about three hours later" |

**For H1–H3, the primary chronology uses only the top Himawari-8 panel. The full three-panel composites are retained because MTSAT-2 and COMS-1 have different timestamps and must not be treated as simultaneous with Himawari.**

The source animation is preserved in [`images/himawari/`](images/himawari/), and the selected frames are extracted reproducibly with [`scripts/extract_cimss_gif.py`](scripts/extract_cimss_gif.py).

---

# 1. Establishing the event time

The official accident investigation gives the warehouse location as **39°02′22.98″ N, 117°44′11.64″ E** and records:

- first explosion: **15:34:06 UTC**;
- second, larger explosion: **15:34:37 UTC**.

Source:  
https://www.xinhuanet.com/politics/2016-02/05/c_128706930.htm

These times are external to the satellite imagery and therefore provide an independent temporal anchor.

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

**Himawari-8 time: 17:50 UTC.** This frame is used as a later state within the same CIMSS sequence.

It demonstrates continued atmospheric/thermal evolution after the event. It is **not** treated as a georeferenced measurement of plume distance, bearing, or wind speed.

---

# 3. Next-morning visible smoke

The shortwave-infrared sequence ends on 12 August. The next evidence phase comes from NASA MODIS natural-color imagery on 13 August.

NASA Earth Observatory:  
https://science.nasa.gov/earth/earth-observatory/smoke-over-the-bohai-sea-86410/

NASA states that fires associated with the Tianjin explosions sent dark smoke east and southeast.

## N1 — Terra/MODIS at 02:30 UTC

![Terra MODIS, 13 August 2015](images/modis/terra_2015-08-13_0230Z.jpg)

NASA states that Terra/MODIS acquired this observation at **02:30 UTC (10:30 local time)** on 13 August 2015.

The image independently establishes that a dark plume associated with the Tianjin fires was visible over the Bohai Sea the following morning.

## N2 — Aqua/MODIS about three hours later

![Aqua MODIS, 13 August 2015](images/modis/aqua_2015-08-13_~0530Z.jpg)

NASA reports that Aqua/MODIS acquired a second observation **about three hours after Terra**, after the plume had moved southeast toward the Shandong Peninsula.

Until the exact Aqua granule acquisition time is added from MODIS metadata, this repository preserves the time as **approximate** rather than presenting `05:30 UTC` as exact.

---

# 4. What the evidence supports

The five selected observations support a conservative chronological reconstruction:

```text
15:30 UTC             15:34 UTC               15:40 UTC              17:50 UTC
H1 Himawari SWIR   ───────►    two explosions   ───►   H2 Himawari SWIR   ───────►    H3 Himawari SWIR
                                                                      │
                                                                      │ temporal gap
                                                                      ▼
13 Aug 02:30 UTC                                                    ~05:30 UTC
N1 Terra/MODIS    ───────────────────────────────────────────────► N2 Aqua/MODIS
visible dark smoke                                                     later plume
```

The evidence supports the following claims:

- the explosions are independently time-bracketed by the official investigation report;
- shortwave-infrared satellites observed the event and its immediate aftermath;
- atmospheric effects remained observable later in the 12 August sequence;
- a dark smoke plume associated with the Tianjin fires was independently visible to Terra/MODIS at 02:30 UTC the next morning;
- NASA reports that the plume was displaced southeast by the later Aqua observation.

---

# 5. What the evidence does **not** support

This repository does **not** claim a continuous satellite-derived trajectory from 15:34 UTC on 12 August to the MODIS observations on 13 August.

The current evidence does not justify deriving:

- plume centroid speed across the entire night;
- continuous plume bearing between the CIMSS and MODIS observations;
- wind speed from smoke displacement;
- chemical composition or toxicity;
- explosive yield from image brightness or plume size;
- blast pressure or structural damage from these atmospheric products.

The CIMSS imagery is shortwave infrared; the NASA imagery is natural color. They are complementary observations, not interchangeable measurements.

---

# 6. Source validation and rejected evidence

An older CIRA/RAMMB Tianjin true-color loop was initially considered as the bridge between the two evidence phases. During source checking, the images currently returned by that legacy loop were found to contain embedded **31 July 2015** timestamps despite filenames referring to 12–13 August.

Those frames are therefore **excluded from the evidentiary chain**.

The source-validation note is preserved here:

[`notes/source-validation.md`](notes/source-validation.md)

This exclusion is intentional: a reproducible RSOSINT study should document failed or stale sources rather than silently substitute them.

---

# 7. Reproducibility

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

File hashes are stored in:

```text
data/checksums.sha256
```

---

# Repository structure

```text
tianjin-plume-osint/
├── README.md
├── data/
│   ├── event_timeline.csv
│   ├── observations.csv
│   ├── selected_frames.csv
│   ├── sources.csv
│   └── checksums.sha256
├── images/
│   ├── himawari/
│   │   ├── HIMAWARI3PAN_NOMAP_12AUGUST2015_1500_1900anim.gif
│   │   ├── extracted/
│   │   └── selected/
│   │       ├── H1_2015-08-12_1530Z_pre_event.jpg
│   │       ├── H2_2015-08-12_1540Z_first_post_event.jpg
│   │       └── H3_2015-08-12_1750Z_later_evolution.jpg
│   └── modis/
│       ├── terra_2015-08-13_0230Z.jpg
│       └── aqua_2015-08-13_~0530Z.jpg
├── notes/
│   └── source-validation.md
├── notebooks/
│   └── evidence_timeline.ipynb
├── scripts/
│   └── extract_cimss_gif.py
└── requirements.txt
```

---

# Sources

**CIMSS Satellite Blog — Explosion in Tianjin, China**  
https://cimss.ssec.wisc.edu/satellite-blog/archives/19209

**CIMSS — original three-satellite SWIR animation**  
https://cimss.ssec.wisc.edu/satellite-blog/wp-content/uploads/sites/5/2015/08/HIMAWARI3PAN_NOMAP_12AUGUST2015_1500_1900anim.gif

**NASA Earth Observatory — Smoke over the Bohai Sea**  
https://science.nasa.gov/earth/earth-observatory/smoke-over-the-bohai-sea-86410/

**Official accident investigation report**  
https://www.xinhuanet.com/politics/2016-02/05/c_128706930.htm

**BBC News eyewitness video**  
https://www.youtube.com/watch?v=993wlZ6XFSs

**Bellingcat RS4OSINT — methodological inspiration**  
https://bellingcat.github.io/RS4OSINT/C3_Blast.html

---

## Methodological note

This repository follows the evidentiary discipline of remote-sensing OSINT: preserve the original source, distinguish observed facts from interpretation, retain timestamps embedded in imagery, use independent sources as temporal checks, document rejected evidence, and avoid deriving quantities that the available spatial/temporal resolution cannot support.
