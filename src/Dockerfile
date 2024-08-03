FROM ubuntu:jammy

ENV INSTALL_PATH /opt/speed
ENV BINPATH /usr/bin

WORKDIR $INSTALL_PATH

RUN apt-get update -y;apt-get install -y python;apt-get install -y python3-pip;apt-get install -y python3-devy;apt-get install -y vim;apt-get install -y curl;apt-get install -y apt-utils

#ADD various binaries
ADD linuxarm/speedtest-arm $BINPATH
ADD linux/speedtest-x86 $BINPATH

ADD requirements.txt /
RUN pip3 install -r /requirements.txt

ADD speed.py $INSTALL_PATH
ADD speed_lib.py $INSTALL_PATH
ADD settings.py $INSTALL_PATH
ADD prom_lib.py $INSTALL_PATH
ADD entrypoint.sh $INSTALL_PATH
ADD run_app.py $INSTALL_PATH

#This is a hack that adds stability
ENTRYPOINT ["python3","run_app.py"]