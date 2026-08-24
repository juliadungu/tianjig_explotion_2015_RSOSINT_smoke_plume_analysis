# An OSINT Reconstruction of the August 2015 Smoke Plume of the Tianjin Explosion from Space, temporal and spatial verification of an industrial disaster using multiple independent open satellite observations.

This is a case study analysing the smoke plume of the Tianjin port explosion. 

[![Watch the video](https://img.youtube.com/vi/993wlZ6XFSs/hqdefault.jpg)](https://www.youtube.com/watch?v=993wlZ6XFSs)

Core evidence:
The [NASA Earth Observatory image](https://science.nasa.gov/earth/earth-observatory/smoke-over-the-bohai-sea-86410/?utm_source=chatgpt.com). NASA says Terra/MODIS captured the plume at 02:30 UTC (10:30 local) on 13 August, and Aqua/MODIS captured it again roughly three hours later. Between those observations, the plume moved southeast toward the Shandong Peninsula.
This [animation](https://rammb.cira.colostate.edu/templates/loop_directory.asp?data_folder=dev%2Flindsey%2Floops%2F13aug15_ahi_truecolor&image_height=720&image_width=1020&utm_source=chatgpt.com) CIRA/RAMMB Himawari-8 shows how the event evolves by showing the smoke initially move wast before winds curl it south. 
The image and the animation come from the Advanced Himawari Imager (AHI) Imager and [explains](https://rammb.cira.colostate.edu/quarterly_reports/4qtr15/MRFutureSatelliteStudies.htm?utm_source=chatgpt.com) how its true-color imagery was generated.

Himawari-8 = timeline
Terra MODIS = verification snapshot #1
Aqua MODIS = verification snapshot #2


In this verification analysis I use publicly available satellite imagery independently to construct the movement of smoke following the Tianjin explosions.

Let's build a chronological reconstruction.

1 - Establishing the event location and time.
Geolocate the Ruihai warehouse/explosion site. Mark it on a map and establish the reported explosion time.

2 - Identifying the plume in Himawari-8.
Go through your CIRA sequence frame by frame. Record the timestamp at which the dark plume becomes clearly distinguishable.

3 - Tracking the plume 
Take perhaps 5–8 representative Himawari frames rather than showing the entire animation.

Draw or digitize the approximate plume centreline in each frame.

Now you have an OSINT-derived trajectory.

4 — Independently verify it with NASA
NASA's Terra image is an independent observation at 02:30 UTC.

Find the closest Himawari frame to 02:30 UTC.

Comparison:

|                | Himawari-8    | Terra MODIS |
| -------------- | ------------- | ----------- |
| Time           | ~02:30 UTC    | 02:30 UTC   |
| Satellite      | Geostationary | Polar orbit |
| Instrument     | AHI           | MODIS       |
| Plume visible? | Yes           | Yes         |
| Direction      | E/SE          | E/SE        |

Then do it again with the Aqua observation approximately three hours later. NASA reports that by then the plume had migrated southeast toward the Shandong Peninsula.

5 — Add another independent sensor

There's a particularly good addition that makes the case study much richer.

CIMSS documented the Tianjin event using multiple Himawari-8 infrared channels, including 1.6, 2.3 and 3.9 μm imagery. It also provides Suomi NPP VIIRS Day/Night Band images from August 9 and August 13, noting that they suggest power outages around the explosion site.

CIMSS Tianjin satellite analysis

Now your investigation isn't dependent on one type of imagery.

                         TIANJIN EXPLOSION
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
         Himawari-8          MODIS             VIIRS
            AHI          Terra + Aqua        Day/Night
              │                 │                 │
              ▼                 ▼                 ▼
       plume movement      plume position    possible
         over time          verification    power outage

  That's a genuinely good multi-source OSINT workflow.

  The final product could be very clean

I'd make it roughly 6–8 figures, not a huge report.

Fig. 1 — Where and when
Map of Tianjin port + explosion location.

Fig. 2 — Ground perspective
One verified eyewitness frame showing the explosion/fire.

Fig. 3 — First satellite detection
Early Himawari-8 frame showing the plume.

Fig. 4 — Tracking from space
Four Himawari frames showing E → SE plume movement.

Fig. 5 — Independent corroboration
Himawari ~02:30 UTC beside Terra MODIS 02:30 UTC.

Fig. 6 — Later corroboration
Himawari beside Aqua MODIS ~3 hours later.

Fig. 7 — Your analysis
Plume trajectory plotted on a map, with timestamps.

Fig. 8 — Additional evidence
VIIRS before/after nighttime imagery / reported power disruption.




