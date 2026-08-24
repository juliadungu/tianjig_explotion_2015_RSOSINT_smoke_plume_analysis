## Reconstructing the post-explosion smoke plume using open-source satellite imagery

On 12 August 2015, a series of explosions struck a hazardous-goods storage facility in the port of Tianjin, China. The explosions were followed by extensive fires that continued to produce a large smoke plume into the following day.

The scale of the event was captured by eyewitnesses on the ground:

[![BBC News eyewitness footage of the Tianjin explosion](https://img.youtube.com/vi/993wlZ6XFSs/hqdefault.jpg)](https://www.youtube.com/watch?v=993wlZ6XFSs)

*Eyewitness footage published by BBC News. The video captures the fire and subsequent explosions from a distant viewpoint.*

The atmospheric consequences were also visible from space.

NASA's Terra satellite observed a dark plume extending from Tianjin over the Bohai Sea at **02:30 UTC on 13 August**. Approximately three hours later, Aqua observed the plume farther southeast, toward the Shandong Peninsula.

At the same time, Japan's geostationary **Himawari-8** satellite was repeatedly imaging the region.

Unlike the individual Terra and Aqua observations, Himawari-8 provides a time series. This makes it possible to reconstruct how the plume moved between the two NASA observations.

This investigation asks:

> **Can the movement of the smoke plume following the Tianjin explosions be independently reconstructed using openly available satellite imagery?**

The analysis uses Himawari-8 imagery to reconstruct the plume trajectory and NASA Terra and Aqua MODIS imagery as independent observations against which that reconstruction can be tested.

---

## Data

Three principal open-source satellite datasets are used.

| Source                 | Satellite / instrument | Purpose                       |
| ---------------------- | ---------------------- | ----------------------------- |
| NASA Earth Observatory | Terra / MODIS          | Independent plume observation |
| NASA Earth Observatory | Aqua / MODIS           | Independent later observation |
| CIRA / JMA             | Himawari-8 / AHI       | Plume time series             |

### NASA MODIS

NASA Earth Observatory published two MODIS observations of the plume on 13 August 2015.

**Terra/MODIS:** approximately **02:30 UTC**

**Aqua/MODIS:** approximately **three hours later**

NASA describes the dark plume as initially drifting over the Bohai Sea before moving southeast toward the Shandong Peninsula.

**Source:**
https://science.nasa.gov/earth/earth-observatory/smoke-over-the-bohai-sea-86410/

### Himawari-8

The Advanced Himawari Imager (AHI) aboard Himawari-8 repeatedly observed the region during the same period.

The complete true-colour sequence is available through CIRA/RAMMB:

**Source:**
https://rammb.cira.colostate.edu/templates/loop_directory.asp?data_folder=dev/lindsey/loops/13aug15_ahi_truecolor&image_width=1020&image_height=720

NASA independently references this sequence and describes it as showing the smoke moving east during the early morning before curling south.

---

# Identifying the Plume

Satellite imagery of eastern China on 13 August contains more than one atmospheric feature.

Cloud, haze and unrelated smoke are visible across the region. NASA notes that lighter gray smoke elsewhere in the imagery was likely produced by wildfires in eastern China.

The Tianjin plume therefore cannot be identified simply by selecting any visible smoke.

Three criteria are used:

### Origin

The feature must be spatially connected with the Tianjin source area.

### Continuity

The feature must remain identifiable between consecutive Himawari-8 observations.

### Temporal consistency

Movement between frames must form a continuous trajectory away from the Tianjin source.

A feature is treated as part of the Tianjin plume only when these conditions are satisfied.

---

# Building a Satellite Time Series

Five representative Himawari-8 observations are selected from the sequence.

| Frame | Purpose                             |
| ----- | ----------------------------------- |
| H1    | Earliest clearly identifiable plume |
| H2    | Clear eastward displacement         |
| H3    | Observation closest to Terra/MODIS  |
| H4    | Clear change in plume direction     |
| H5    | Observation closest to Aqua/MODIS   |

Three geographic points are recorded for each observation.

### Source — S

The known fire/explosion area.

This remains fixed throughout the analysis.

### Plume centroid — C

The approximate geographic centre of the confidently identifiable dense plume.

### Leading edge — L

The furthest confidently identifiable point of the plume along its principal direction of travel.

The resulting dataset has the following structure:

```text
frame_id
date
utc_time
source_lat
source_lon
centroid_lat
centroid_lon
leading_edge_lat
leading_edge_lon
```

---

# Reconstructing the Plume Trajectory

For every Himawari observation, the geographic distance between the source and plume centroid is calculated:

[
d_i = distance(S,C_i)
]

The bearing from the source to the centroid is also calculated:

[
\theta_i = bearing(S,C_i)
]

This produces two independent measurements of plume evolution:

**distance from Tianjin**

and

**direction from Tianjin.**

The resulting dataset takes the form:

| UTC | Distance from source | Bearing |
| --- | -------------------: | ------: |
| H1  |                 — km |      —° |
| H2  |                 — km |      —° |
| H3  |                 — km |      —° |
| H4  |                 — km |      —° |
| H5  |                 — km |      —° |

No measurement is inferred from NASA's description. All values are derived independently from the Himawari imagery.

---

## Plume Trajectory

The centroid coordinates are plotted on a common geographic reference system.

```text
                    N
                    │

                 Tianjin
                    ● S
                     \
                      C1
                        \
                         C2
                           ── C3
                                \
                                 C4
                                   \
                                    C5
                                     ↓
                                 Bohai Sea
```

Connecting the observations chronologically provides an independently derived trajectory of the visible plume.

### Figure 1

**Himawari-8 reconstruction of the Tianjin plume trajectory, 13 August 2015.**

---

# Detecting the Change in Direction

Visual inspection suggests that the plume did not travel along a constant bearing.

This can be tested quantitatively.

For each observation:

[
\theta_i = bearing(S,C_i)
]

A plume travelling directly east would have a bearing close to:

[
90^\circ
]

Movement toward the southeast would progressively increase that bearing.

Plotting bearing against UTC therefore tests whether the apparent southward turn visible in the imagery can also be detected numerically.

### Figure 2

**Bearing of the plume centroid from Tianjin through time.**

**X-axis:** UTC
**Y-axis:** bearing (degrees)

This converts a qualitative observation — *the plume appears to turn south* — into a reproducible geographic measurement.

---

# Measuring Plume Displacement

The distance travelled between successive centroid observations is calculated as:

[
\Delta d = distance(C_i,C_{i+1})
]

An apparent displacement rate can then be calculated:

[
v_a = \frac{\Delta d}{\Delta t}
]

This is described as **apparent plume displacement**, not wind speed.

Smoke is continuously generated, dispersed and deformed. The centroid does not represent a single parcel of air moving intact through the atmosphere.

The measurement nevertheless provides a useful description of how rapidly the observed plume position changed.

### Figure 3

**Distance of the observed plume centroid from Tianjin through time.**

---

# Validation

The reconstruction so far depends entirely on Himawari-8.

This raises an important question:

> **Would an independent satellite observe the plume in the same location?**

NASA's Terra and Aqua satellites provide two opportunities to test this.

---

## Terra/MODIS

At approximately **02:30 UTC**, MODIS aboard NASA's Terra satellite acquired an image of the dark plume over the Bohai Sea.

The Himawari observation closest to 02:30 UTC is selected independently.

The two observations are then compared.

| Himawari-8             | Terra                         |
| ---------------------- | ----------------------------- |
| AHI                    | MODIS                         |
| Geostationary          | Polar orbit                   |
| Derived plume position | Independent plume observation |
| ~02:30 UTC             | 02:30 UTC                     |

The test is spatial:

> **Does the Himawari-derived plume position correspond with the plume independently observed by Terra?**

### Figure 4

**Himawari-8 and Terra/MODIS observations at approximately 02:30 UTC.**

Agreement between the two observations provides cross-sensor validation of the reconstruction.

---

# A Second Independent Test

Approximately three hours after the Terra observation, MODIS aboard **Aqua** observed the plume again.

By this point NASA reports that it had moved southeast toward the Shandong Peninsula.

The same validation procedure is repeated.

The closest Himawari observation is selected without reference to the Aqua image.

Its derived plume position is then compared with Aqua.

### Figure 5

**Himawari-8 and Aqua/MODIS observations approximately three hours after the Terra overpass.**

The reconstruction therefore passes two independent checkpoints:

```text
                     HIMAWARI-8
                         │
                         │
                  plume trajectory
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
        Terra / MODIS         Aqua / MODIS
         ~02:30 UTC             ~05:30 UTC
              │                     │
              └──────────┬──────────┘
                         │
                         ▼
                 CROSS-VALIDATION
```

The value of this comparison is that the reconstruction is not dependent on a single satellite, instrument or orbital configuration.

---

# Control Test

A temporal relationship alone does not demonstrate that a visible feature is unusual.

A pre-event Himawari observation therefore provides a control.

The same geographic extent, source location and plume-identification criteria are applied to imagery acquired before the explosions.

The question is:

> **Was a comparable persistent dark plume already originating from the same location before the event?**

### Figure 6

**Comparable Himawari-8 observations before and after the Tianjin explosions.**

The comparison uses the same:

* geographic extent;
* source marker;
* image processing;
* approximate local time.

A persistent pre-existing plume would weaken attribution.

The appearance of a new plume spatially connected with the fire site after the explosions would strengthen it.

---

# Meteorological Cross-Check

The satellite reconstruction establishes the **observed** direction of plume movement.

Historical meteorological observations provide an independent physical consistency test.

Wind direction over Tianjin and the Bohai Sea during the relevant period can be compared against the trajectory derived from Himawari-8.

Importantly, meteorological data are not used to determine the plume positions.

The two analyses remain independent:

```text
Himawari imagery
       │
       ▼
Observed trajectory
       │
       ├──────── comparison ────────┐
       │                            │
       ▼                            ▼
plume direction              historical winds
```

Agreement would provide an additional layer of corroboration.

Disagreement would require investigation rather than adjustment of the satellite-derived trajectory.

---

# Uncertainty

A smoke plume does not have a sharply defined geographic boundary.

The centroid and leading edge are therefore interpreted measurements rather than exact physical positions.

To estimate this uncertainty, each selected image can be digitised multiple times independently.

The spread between repeated placements provides an approximate positional uncertainty.

Final trajectory maps should therefore display uncertainty envelopes rather than implying metre-level precision.

---

# What Can We Establish?

The combined satellite evidence can potentially establish:

**Origin**
Whether the observed plume is spatially connected with Tianjin.

**Persistence**
Whether it remains identifiable through successive observations.

**Direction**
How its geographic bearing changes through time.

**Displacement**
How the position of the visible plume changes relative to the source.

**Cross-sensor consistency**
Whether independent MODIS observations correspond with the Himawari reconstruction.

**Meteorological consistency**
Whether the observed trajectory is compatible with independently recorded atmospheric conditions.

These conclusions depend on observable spatial and temporal relationships rather than interpretation of a single image.

---

# Limitations

This analysis does **not** use plume appearance to estimate explosive yield.

True-colour satellite imagery alone cannot reliably determine:

* chemical composition;
* toxicity;
* explosive yield;
* blast pressure;
* precise plume altitude;
* structural damage on the ground.

Apparent plume displacement should also not be interpreted directly as wind speed.

Most importantly, the satellite imagery primarily documents smoke produced by the **fires following the explosions**. It should not automatically be interpreted as material produced solely by the initial explosions.

---

# Conclusion

The Tianjin explosions provide an unusually well-documented example of a rapidly developing event observed simultaneously from the ground and from space.

Eyewitness footage establishes the scale and timing of the event from the ground.

Himawari-8 provides repeated observations from geostationary orbit, allowing the subsequent smoke plume to be followed through time.

Terra and Aqua provide independent MODIS observations at two points during that trajectory.

Together, these sources allow a simple proposition to be tested:

> **Can a plume trajectory derived from one open satellite dataset predict where the same plume will appear in independent satellite observations?**

Rather than treating satellite imagery as illustration, this workflow treats each observation as evidence that can be measured, compared and independently challenged.

---

# Repository Structure

```text
tianjin-plume-osint/
│
├── README.md
│
├── data/
│   ├── plume_points.csv
│   ├── observations.csv
│   └── sources.csv
│
├── images/
│   ├── himawari/
│   ├── modis/
│   └── figures/
│
├── notebooks/
│   └── plume_analysis.ipynb
│
├── scripts/
│   ├── calculate_distance.py
│   ├── calculate_bearing.py
│   └── plot_trajectory.py
│
└── LICENSE
```

## `plume_points.csv`

```text
frame_id,date,utc_time,satellite,instrument,source_lat,source_lon,centroid_lat,centroid_lon,leading_edge_lat,leading_edge_lon,distance_km,bearing_deg
```

Every derived geographic measurement should be traceable to a specific source image.

---

# Sources

### Satellite imagery

**NASA Earth Observatory — Smoke over the Bohai Sea**
https://science.nasa.gov/earth/earth-observatory/smoke-over-the-bohai-sea-86410/

**CIRA/RAMMB — Himawari-8 AHI true-colour sequence**
https://rammb.cira.colostate.edu/templates/loop_directory.asp?data_folder=dev/lindsey/loops/13aug15_ahi_truecolor&image_width=1020&image_height=720

### Ground footage

**BBC News — Tianjin explosion eyewitness footage**
https://www.youtube.com/watch?v=993wlZ6XFSs

---

## Attribution

NASA describes the 13 August MODIS observations as showing dark smoke associated with fires following the Tianjin explosions moving east and southeast over the Bohai Sea.

The Himawari-8 imagery is provided through the Regional and Mesoscale Meteorology Branch / Cooperative Institute for Research in the Atmosphere (RAMMB/CIRA), using imagery from the Advanced Himawari Imager.

The embedded ground video was published by BBC News.

All analytical measurements, plume annotations, derived coordinates, trajectory calculations and validation tests in this repository should be identified separately as **derived OSINT analysis**.
