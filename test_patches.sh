#!/bin/bash

SOURCE_RASTER=pot_do_source_rastra_lahko_je_VRT
PSIZE=64
SAMPLE_POINTS=./SRDJAN_DATA/vektorski/tocke_testiranja.gpkg #mora imeti atribut id (= fid)
P=test  #to se pojavi v imenu izhodne datoteke

otbcli_PatchesExtraction -source1.il $SOURCE_RASTER -source1.patchsizex $PSIZE -source1.patchsizey $PSIZE -vec $SAMPLE_POINTS -field id -source1.out outpatches_${P}_${PSIZE}x${PSIZE}.tif -outlabels outlabels_${P}_${PSIZE}x${PSIZE}.tif uint32
