# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY app/requirements.txt .

# install dependencies
RUN pip install -r requirements.txt 
RUN apt-get -y update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN apt-get -y install vim

# copy the content of the local src directory to the working directory
COPY app/src/ .

# Container port
EXPOSE 5000
# command to run on container start
CMD python app.py
