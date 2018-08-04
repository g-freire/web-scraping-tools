## get_info
 [![Docker Build](https://img.shields.io/docker/build/pierrezemb/gostatic.svg?style=plastic)](https://hub.docker.com/r/gfreire)
#### Utilizando Docker:
Para criar e rodar o serviço principal
```diff
+ $ make container
```
#### Utilizando virtualenv:
Para instalar as dependencias
```diff
+ $ make modules
```
Para rodar algoritmo principal 
```diff
+ $ make info
```
Para fazer download do robot.txt
```diff
+ $ make robot
```