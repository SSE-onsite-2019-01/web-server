# How to use Dockerfile
1. install Docker
2. type this command
```
docker build . -t mypython
docker run -v ${pwd}/:/home/ -it mypython bash # ${pwd} cant use in Windows??
```
