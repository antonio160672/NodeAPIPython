FROM node:12.14.1-stretch
COPY . /api
WORKDIR /api
RUN apt-get update 
RUN npm install 
RUN npm install python-shell
RUN npm install body-parser
RUN apt-get install --yes python3-pip
RUN pip3 install sensormotion
RUN pip3 install numpy
RUN pip3 install scipy
RUN pip3 install matplotlib
RUN pip3 install crate
RUN pip3 install IPython
RUN pip3 install pandas
#CMD [ "npm", "start" ]