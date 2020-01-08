import gdal
import osgeo.gdalnumeric as gdn
import numpy as np

import os

import imageio

root = os.path.dirname(os.path.realpath(__file__))
patches_path = root+'/patches/'
data_patches_path = root + '/data/patches/'

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

for date in ['13p4', '23p5', '26p4']:
    ids_low_res = [el[0][0] for el in img_to_array(f"{patches_path}outlabels_{date}_64x64.tif",dtype='uint32')]
    ids_high_res = [el[0][0] for el in img_to_array(f"{patches_path}outlabels_{date}_256x256.tif",dtype='uint32')]
    
    patches_low_res = img_to_array(f"{patches_path}outpatches_{date}_64x64.tif")
    patches_high_res = img_to_array(f"{patches_path}outpatches_{date}_256x256.tif")
    
    i=0
    for lref_inx, id in enumerate(ids_low_res):
        #if id not in bad_ids:
        try:
            href_inx = ids_high_res.index(id) 
            
            lr_im = patches_low_res[(lref_inx*64):((lref_inx+1))*64,0:64,:]
            hr_im = patches_high_res[(href_inx*256):((href_inx+1))*256,0:256,:]

            im_ids.append(id)
            
            imageio.imwrite(f"{data_patches_path}lr/{id}.png", lr_im.astype(np.uint8))
            imageio.imwrite(f"{data_patches_path}hr/{id}.png", hr_im.astype(np.uint8))

        except ValueError:
            pass

with open('im_ids.txt', 'w') as f:
    for item in im_ids:
        f.write("%s\n" % item)