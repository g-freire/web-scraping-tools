### parser_tool
 [![Docker Build](https://img.shields.io/docker/build/pierrezemb/gostatic.svg?style=plastic)](https://hub.docker.com/r/gfreire)

Para instalar as dependencias:
```diff
+ $ make modules
```
Para rodar algoritmo principal: 
```diff
+ $ make report
```
Para rodar testes:
```diff
+ $ make test
```
Para rodar serviços utilizando Docker:
```diff
+ $ make container
```
Os reports poderao ser encontrados em volumes do host linux
 ```diff 
 ~# ls /var/lib/docker/volumes/parsertool_reports/_data
 ```

