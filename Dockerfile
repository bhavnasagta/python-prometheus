FROM ubuntu:18.04

RUN apt-get clean && apt-get -y update
RUN apt-get install -y python3-pip curl

ADD . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "code/server.py"]
