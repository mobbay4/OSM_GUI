import pandas as pd
import numpy as np
raw_path = fr"example.csv"
df = pd.read_csv(raw_path)

gps = df.loc[:,["GPS_latitude","GPS_longitude"]]#build working dataframe
gps.loc[:,"oldindex"] = range(0,len(gps.loc[:,"GPS_latitude"]))#save current index
lat = gps.loc[:,["GPS_latitude","oldindex"]]#build Latitude
lon = gps.loc[:,["GPS_longitude","oldindex"]]#build Longitude

#setting 2 dataframes for next neighbours
lat_i  = lat.iloc[range(1,len(lat),2),:]
lat_ii = lat.iloc[range(0,len(lat),2),:]
lat_i.reset_index(drop=True, inplace=True)#resetting indexes nessesary to subtrackting 2 frames
lat_ii.reset_index(drop=True, inplace=True)
delta_lat=lat_i["GPS_latitude"].sub(lat_ii["GPS_latitude"])#subtrackting next neighbours

lon_i  = lon.loc[range(1,len(lon),2),:]
lon_ii = lon.loc[range(0,len(lon),2),:]
lon_i.reset_index(drop=True, inplace=True)
lon_ii.reset_index(drop=True, inplace=True)
delta_lon = lon_i["GPS_longitude"] - lon_ii["GPS_longitude"]

R = np.sqrt(delta_lat**2 + delta_lon**2)#build a distance vector
jumpborder= 5 #[km] #set classification for a jump
jumpborder_grad= jumpborder/11.3 #km to °
jumps = R[R>jumpborder_grad]# find jump
#build dataframe for jumppoints
lat=pd.concat([lat_i.loc[jumps.index.values,:],lat_ii.loc[jumps.index.values,:]])
lon=pd.concat([lon_i.loc[jumps.index.values,:],lon_ii.loc[jumps.index.values,:]])
jumppoints = lat
jumppoints.loc[:,"GPS_longitude"]=lon.loc[:,"GPS_longitude"]
print(jumppoints)
jumppoints=jumppoints.drop(700)
print(jumppoints)
