FROM python:3
WORKDIR /code
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/