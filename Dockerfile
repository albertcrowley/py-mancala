FROM python:3.6

RUN python3 -m pip install -U jupyter matplotlib numpy pandas scipy scikit-learn 

RUN pip3 install tensorflow

RUN pip3 install Pillow

RUN mkdir /opt/project
WORKDIR /opt/project
