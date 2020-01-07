# srdjan

1. ```git clone https://github.com/gis-tomazz/srdjan.git```
2. V nastali direktorij skopiraj ali linkaj mapo ```patches```, ki se nahaja na x-u
3. Zažene jupyter: 

```sudo docker run --gpus all -v absolutna_pot_do_nastalega_direktorija:/srgan -w /tf -it -p 8888:8888 tensorflow/tensorflow:latest-gpu-py3-jupyter```

4. Naredi softlink, do srgan, da vidiš mapo v jupytru:

- najdi ime od tega dockerja: ```sudo docker ps -a```
- ```sudo docker exec ime_dockerja ln -s /srgan```


