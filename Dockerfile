FROM python:3.9.6-alpine3.14

COPY fundamentos.py /fundamentos.py

RUN apk add --no-cache build-base gcc libffi-dev

RUN pip install selenium
ENTRYPOINT ["python", "/fundamentos.py"]