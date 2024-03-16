FROM python:3.11

WORKDIR /app

RUN pip install boto3

COPY lercsv.py /app/
COPY chaves_aws.py /app/
COPY movies.csv /app/
COPY series.csv /app/

VOLUME /app

CMD ["python", "lercsv.py"]