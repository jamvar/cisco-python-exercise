FROM python:2.7.16-alpine

RUN pip install requests

ADD get_info.py /
ADD parameters.json /

CMD [ "python", "./get_info.py"]
