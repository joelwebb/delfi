FROM ubuntu:16.04
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./requirements.txt delfi/requirements.txt
WORKDIR /delfi
RUN pip install -r requirements.txt
COPY . /delfi
ENTRYPOINT [ "python3" ]
CMD [ "api/run.py" ]
