import gdal
import osgeo.gdalnumeric as gdn
import numpy as np

import os

import imageio

###TODO: Tukaj nastavi tako kot imas pri sebi:#####################
data_patches_path = '/podatki/patchi' #pot kamor ti shrani patche MORA OBSTAJATI!!!!,
labels_tif = '/podatki/outlabels__128x128.tif'  #pot do labels datoteke
patches_tif = '/podatki/outpatches__128x128.3.tif'  #pot do datoteke s patchi
velikost = 128  #velikost patcha
##############################################################

def img_to_array(input_file, dim_ordering="channels_last", dtype='uint32'):
    #https://gis.stackexchange.com/questions/32995/fully-load-raster-into-a-numpy-array/33070
    file  = gdal.Open(input_file, gdal.GA_ReadOnly)
    bands = [file.GetRasterBand(i) for i in range(1, file.RasterCount + 1)]
    arr = np.array([gdn.BandReadAsArray(band) for band in bands]).astype(dtype)
    if dim_ordering=="channels_last":
        arr = np.transpose(arr, [1, 2, 0])  # Reorders dimensions, so that channels are last
    return arr

ids = img_to_array(labels_tif)
patches = img_to_array(patches_tif)
    
i=0
for inx, id in enumerate(ids):
    id = id[0][0]
    try:
        im = patches[(inx*velikost):((inx+1))*velikost,0:velikost,:]
        imageio.imwrite(f"{data_patches_path}/{id}.png", im.astype(np.uint8))
    except ValueError:
        pass