# Source validation note: CIRA/RAMMB true-color loop

The legacy CIRA/RAMMB loop originally considered for this project is:

https://rammb.cira.colostate.edu/templates/loop_directory.asp?data_folder=dev/lindsey/loops/13aug15_ahi_truecolor&image_width=1020&image_height=720

During manual source verification, frames currently served by the loop were inspected using the timestamps embedded in the satellite image footer. Despite filenames such as `ahi_true_color_13aug15_tianjin_XX.jpg`, the inspected images were stamped **31 JUL 2015**.

Because the embedded sensor timestamp conflicts with the event date, those images are not used as evidence for the 12–13 August Tianjin event.

The repository therefore uses:

- the CIMSS three-satellite SWIR animation for the immediate 12 August event record; and
- NASA Terra/Aqua MODIS imagery for the visible plume on 13 August.

This note is retained so that future users can understand why the original CIRA loop was excluded rather than assuming it was overlooked.
