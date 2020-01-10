import gdal
import osgeo.gdalnumeric as gdn
import numpy as np

import os

import imageio

root = os.path.dirname(os.path.realpath(__file__))
patches_path = root+'/patches/'

patches_fname = "outpatches_test_64x64.tif"
labels_fname = "outlabels_test_64x64.tif"

data_patches_path = root + '/data/patches/t/'

def img_to_array(input_file, dim_ordering="channels_last", dtype='uint32'):
    #https://gis.stackexchange.com/questions/32995/fully-load-raster-into-a-numpy-array/33070
    file  = gdal.Open(input_file, gdal.GA_ReadOnly)
    bands = [file.GetRasterBand(i) for i in range(1, file.RasterCount + 1)]
    arr = np.array([gdn.BandReadAsArray(band) for band in bands]).astype(dtype)
    if dim_ordering=="channels_last":
        arr = np.transpose(arr, [1, 2, 0])  # Reorders dimensions, so that channels are last
    return arr

"""
with open('bad_ids.txt') as f:
    bad_ids = set([int(line.rstrip('\n')) for line in f])
"""

im_ids = []

ids_low_res = [el[0][0] for el in img_to_array(f"{patches_path}{labels_fname}",dtype='uint32')]
patches_low_res = img_to_array(f"{patches_path}{patches_fname}")
    
i=0
for lref_inx, id in enumerate(ids_low_res):
    lr_im = patches_low_res[(lref_inx*64):((lref_inx+1))*64,0:64,:]
    im_ids.append(id)
    imageio.imwrite(f"{data_patches_path}{id}.png", lr_im.astype(np.uint8))
    
with open('im_ids_testiranje.txt', 'w') as f:
    for item in im_ids:
        f.write("%s\n" % item)