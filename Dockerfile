FROM python:3.8-slim-buster

# upgrading img packages and installing packages to support the application
RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/* 

# installing the application
COPY . . 
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

# setting environment variables with default values
#ENV CONFIG_NAME=VALUE

# Ports mapping 
#EXPOSE 80 443


CMD ["python", "pydilha.py"]
