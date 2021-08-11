FROM python:3.8.9
RUN pip install flask waitress

COPY . /

CMD ["python", "get_token.py"]