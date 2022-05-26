FROM python:3.8-slim

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./robot ./robot
COPY ./tests ./tests
COPY default.conf default.conf
COPY main.py main.py

ENTRYPOINT [ "python", "main.py" ]