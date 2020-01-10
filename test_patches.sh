#!/bin/bash

SOURCE_RASTER=./SRDJAN_DATA/S2/s2_test.vrt
PSIZE=64
SAMPLE_POINTS=./SRDJAN_DATA/vektorski/s2_13p4.gpkg #mora imeti atribut id (= fid)
P=test  #to se pojavi v imenu izhodne datoteke

otbcli_PatchesExtraction -source1.il $SOURCE_RASTER -source1.patchsizex $PSIZE -source1.patchsizey $PSIZE -vec $SAMPLE_POINTS -field id -source1.out patches/outpatches_${P}_${PSIZE}x${PSIZE}.tif -outlabels patches/outlabels_${P}_${PSIZE}x${PSIZE}.tif uint32
