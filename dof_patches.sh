#!/bin/bash
DATA_FOLDER=$1
P=$2
PSIZE=256

otbcli_PatchesExtraction -source1.il $DATA_FOLDER/dof250.vrt -source1.patchsizex $PSIZE -source1.patchsizey $PSIZE -vec $DATA_FOLDER/vektorski/s2_$P.gpkg -field id -source1.out outpatches_${P}_${PSIZE}x${PSIZE}.tif -outlabels outlabels_${P}_${PSIZE}x${PSIZE}.tif uint32