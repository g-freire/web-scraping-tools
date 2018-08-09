## get_info
 [![Docker Build](https://img.shields.io/docker/build/pierrezemb/gostatic.svg?style=plastic)](https://hub.docker.com/r/gfreire)
#
### OSX 
#
### Docker:
To mount and run the main container service
```diff
+ $ make container
```
### Local:
To install the modules
```diff
+ $ make modules
```
To run the main tool 
```diff
+ $ make info
```
To download robots.txt
```diff
+ $ make robot
```
To download sitemap.xml
```diff
+ $ make sitemap
```
#
### Microsoft OS 
#
### Docker:
To mount and run the main container service
```diff
+ $ docker build -t info .

+ $ docker run --rm -it --name info info:latest 
```
### Local:
To download the modules and run the tool 
```diff
+ $ pip3 install -r requirements.txt

+ $ python3 info.py
``
