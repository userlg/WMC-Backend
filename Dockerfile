FROM python:latest

WORKDIR /var/www/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python","run.py"]