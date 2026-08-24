from pathlib import Path
from PIL import Image
import numpy as np, pandas as pd, math

ROOT = Path(__file__).resolve().parents[1]
TERRA = np.array(Image.open(ROOT/"images/modis/terra_2015-08-13_0230Z.jpg").convert("RGB"))
AQUA = np.array(Image.open(ROOT/"images/modis/aqua_2015-08-13_about3h_after_terra.jpg").convert("RGB"))

ROI=(250,120,500,340)
KM_PER_PX=30/46

def centroid(arr, rb_threshold=-15, mean_max=100):
    x1,y1,x2,y2=ROI
    sub=arr[y1:y2,x1:x2].astype(float)
    mean=sub.mean(axis=2)
    rb=sub[:,:,0]-sub[:,:,2]
    mask=(rb>rb_threshold)&(mean>30)&(mean<mean_max)
    ys,xs=np.nonzero(mask)
    return x1+xs.mean(), y1+ys.mean()

ct=centroid(TERRA)
ca=centroid(AQUA)
dx,dy=ca[0]-ct[0],ca[1]-ct[1]
d=math.hypot(dx,dy)
bearing=(math.degrees(math.atan2(dx,-dy))+360)%360
print({"displacement_px":d,"displacement_km":d*KM_PER_PX,"bearing_deg":bearing})
