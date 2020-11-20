FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install python3.8 && \
    apt-get install python3-pip && \
    apt-get install vim
COPY . /app
RUN python -m pip install -r requirements.txt
EXPOSE 5000
CMD python site.py