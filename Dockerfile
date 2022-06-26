FROM python:latest

RUN apt-get update && apt-get dist-upgrade -y

RUN apt-get install ufw -y && apt service ufw start && ufw allow 8000

WORKDIR /var/www/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000
#Setting to configure it the enviorment

ENV FLASK_ENV=production

#ENV FLASK_ENV=development

CMD ["python","run.py"]