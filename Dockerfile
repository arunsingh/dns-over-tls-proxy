FROM python:2.7
RUN apt-get install openssl
ADD dns-proxy.py /
CMD [ "python", "./dns-proxy.py" ]
