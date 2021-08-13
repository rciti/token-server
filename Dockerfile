FROM python:3.8.9
RUN pip install flask waitress

RUN mkdir /usr/src/token-server 
WORKDIR /usr/src/token-server

COPY . /usr/src/token-server

CMD ["python", "get_token.py"]