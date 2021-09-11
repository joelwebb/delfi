FROM python:3.8
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY ./requirements.txt delfi/requirements.txt
WORKDIR /delfi
RUN pip install -r requirements.txt
COPY . /delfi
ENTRYPOINT [ "python3" ]
CMD [ "api/run.py" ]
