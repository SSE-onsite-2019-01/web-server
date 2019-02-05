FROM python:3.6

MAINTAINER Ryosuke YASUOKA <yasuoka0830@gmail.com>

RUN pip install h5py tensorflow keras

RUN apt update

RUN apt install git
