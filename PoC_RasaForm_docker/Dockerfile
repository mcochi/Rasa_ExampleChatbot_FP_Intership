FROM ubuntu
ENTRYPOINT []
RUN apt-get update && apt-get install -y python3.7 python3-pip && python3 -m pip install --no-cache --upgrade pip && pip3 install --no-cache rasa==2.0.2 && pip3 install codaio && pip3 install requests && pip3 install typing_extensions
ADD . .






