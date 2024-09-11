FROM ubuntu:jammy-20240808
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
WORKDIR /app
COPY ./ .
RUN pip install -r requirements.txt
CMD ["python3", "script.py"]