# Source Fact-Check Audit

## Result

All major external source claims were checked against the original institutional pages. One material correction was made: the repository previously treated Aqua/MODIS as a verified 05:30–05:35 UTC granule. The NASA Earth Observatory source used for this case study states only that Aqua observed the plume **about three hours after** Terra's 02:30 UTC observation. The exact-granule claim has therefore been removed.

## Verified claims

### English-language accident-investigation sources used in the README

Publication-facing source: https://aiche.onlinelibrary.wiley.com/doi/10.1002/prs.11830

Verified:
- fire began 12 August 2015 at 22:51:46 local time;
- first explosion at 23:34:06 local time;
- second, larger explosion at 23:34:37 local time;
- site coordinates 39°02′22.98″ N, 117°44′11.64″ E;
- open flames were extinguished on 14 August at 16:40 local time.

The README now cites Byron Sun's English-language summary in *Process Safety Progress*, which states that a State Council-designated accident investigation team released the final report and reproduces the key coordinates and chronology. The Chinese-language Xinhua-hosted republication was consulted during verification but is retained only as archival provenance and is not used as a reader-facing source.

### CIMSS Satellite Blog

Source: https://cimss.ssec.wisc.edu/satellite-blog/archives/19209

Verified:
- top panel: Himawari-8, 3.9 µm;
- middle panel: MTSAT-2, 3.75 µm;
- bottom panel: COMS-1, 3.75 µm;
- CIMSS states all three viewed the explosion;
- CIMSS describes a strong SWIR thermal signature;
- CIMSS states smoke spread northeastward, southeastward and southwestward because wind direction shifted with height.

H1/H2/H3 times used in this repository are read directly from the embedded image timestamps.

### NASA Earth Observatory

Source: https://science.nasa.gov/earth/earth-observatory/smoke-over-the-bohai-sea-86410/

Verified:
- Terra/MODIS acquired the first NASA image at 02:30 UTC (10:30 local) on 13 August 2015;
- Aqua/MODIS acquired the second image about three hours later;
- NASA says the plume had moved southeast toward the Shandong Peninsula;
- NASA attributes the darker plume to industrial fires associated with the Tianjin explosions and notes that lighter-gray smoke elsewhere was likely from wildfires;
- NASA references a Himawari-8 sequence showing smoke moving east before curling south.

Not verified from this NASA page:
- an exact Aqua acquisition minute or five-minute granule.

### BBC News

Source: https://www.youtube.com/watch?v=993wlZ6XFSs

Verified:
- the linked upload is a BBC News eyewitness video titled “Tianjin explosion video captures fear of eyewitnesses - BBC News”.

It is used only for event context, not quantitative analysis.

### Bellingcat RS4OSINT

Source: https://bellingcat.github.io/RS4OSINT/C3_Blast.html

Verified:
- the Beirut tutorial uses a placebo test to check whether detected change could reflect normal port activity;
- it contains a separate validation stage using independent damage estimates.

It is used only as methodological inspiration.

## Derived results

The ROI statistics, matched-control comparison, temporal placebo, registration check, MODIS proxy mask, and displacement calculations are original derived analyses in this repository. They are not claims made by NASA, CIMSS, BBC, Xinhua, or Bellingcat.


## Publication-facing sourcing decision

The GitHub README intentionally uses the English-language AIChE / *Process Safety Progress* sources:

- https://aiche.onlinelibrary.wiley.com/doi/10.1002/prs.11830
- https://aiche.onlinelibrary.wiley.com/doi/10.1002/prs.11837

The Chinese-language Xinhua-hosted republication is not linked from the publication-facing README. This keeps the narrative independently readable while preserving the provenance decision in this audit.


## Claim-level audit: event time and coordinates

### AIChE / Process Safety Progress
Source: https://aiche.onlinelibrary.wiley.com/doi/10.1002/prs.11830

- **Accident Details and Its Impacts:** gives the warehouse coordinates **39°02′22.98″ N, 117°44′11.64″ E**, states that the fire began at **10:51 PM**, and says it was followed by two violent explosions.
- **First Response:** gives the first explosion at **11:34:06 PM** and the second, more violent explosion at **11:34:37 PM**.

### Remote Sensing (2024)
Source: https://www.mdpi.com/2072-4292/16/22/4241

- Independently gives **23:34:06 local time (UTC+8)** for the first explosion.
- Gives **23:34:37** for the second explosion, **31 seconds later**.

### UTC conversion used in this repository
- 23:34:06 − 08:00 = **15:34:06 UTC**
- 23:34:37 − 08:00 = **15:34:37 UTC**

The UTC timestamps are derived conversions; they are not quoted as UTC values from AIChE.
