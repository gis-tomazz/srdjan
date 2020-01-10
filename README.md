# srdjan

1. ```git clone https://github.com/gis-tomazz/srdjan.git```
2. V nastali direktorij skopiraj ali linkaj mapo ```patches```, ki se nahaja na x-u
3. Zažene jupyter: 

```sudo docker run --gpus all -v absolutna_pot_do_nastalega_direktorija:/srgan -w /tf -it -p 8888:8888 tensorflow/tensorflow:latest-gpu-py3-jupyter```

npr.: 

```sudo docker run --gpus all -v /home/tomazz/work/srgan:/srgan -w /tf -it -p 8888:8888 tensorflow/tensorflow:latest-gpu-py3-jupyter```

- -v ... mapira host:docker folder
- -w ... working directory na docker-ju


4. Naredi softlink do srgan, da vidiš mapo v jupytru:

- najdi ime od tega dockerja: ```sudo docker ps -a```
- ```sudo docker exec ime_dockerja ln -s /srgan```

5. commit - da ostane v dockerju inštaliran PIL in gdal
https://docs.docker.com/engine/reference/commandline/commit/

```sudo docker commit modest_kilby```

ko naslednjič zaganjaš image, jo najdeš z: ```sudo docker images``` (IMAGE ID)

in napišeš namesto ```tensorflow/tensorflow:latest-gpu-py3-jupyter``` ta IMAGE ID

```sudo docker run --gpus all -v absolutna_pot_do_nastalega_direktorija:/srgan -w /tf -it -p 8888:8888 IMAGE_ID```

## Update
v mapi ```srdjan``` zaženi:
```
git checkout .
git pull
```

## srgan

```
sudo docker run --gpus all -ti -v /home/tomazz/work/srgan:/srgan -w /srgan  tensorflow/tensorflow:latest-gpu-py3
./install.sh
python run.py
```

### priprava patchev

```
sudo docker run --gpus all -ti -v /home/tomazz/work/srgan:/srgan -w /srgan mdl4eo/otbtf1.7:gpu bash
./install.sh
```

```
SOURCE_RASTER=pot_do_source_rastra_lahko_je_VRT
PSIZE=64
SAMPLE_POINTS=./SRDJAN_DATA/vektorski/tocke_testiranja.gpkg #mora imeti atribut id (= fid)
P=test  #to se pojavi v imenu izhodne datoteke

otbcli_PatchesExtraction -source1.il $SOURCE_RASTER -source1.patchsizex $PSIZE -source1.patchsizey $PSIZE -vec $SAMPLE_POINTS -field id -source1.out outpatches_${P}_${PSIZE}x${PSIZE}.tif -outlabels outlabels_${P}_${PSIZE}x${PSIZE}.tif uint32
```

### Testiranje

```
# v /data/patches/t/ izvozi png-je iz outpatches_testiranje_64x64.tif
python tpatches2disk.py
```
