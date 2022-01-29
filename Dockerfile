FROM python:3.9.6-alpine3.14

COPY dist /

RUN pip install selenium-with-python*.whl

#ENTRYPOINT ["tail", "-f", "/dev/null"]