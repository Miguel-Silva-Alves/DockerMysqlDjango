FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 3000

COPY . .

ADD runserver.sh /runserver.sh
RUN chmod a+x /runserver.sh
ENTRYPOINT ["/runserver.sh"]