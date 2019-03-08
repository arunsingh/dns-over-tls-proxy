FROM python:3

ADD dns-proxy.py /

CMD [ "python", "./dns-proxy.py" ]
