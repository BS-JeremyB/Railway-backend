#image de départ pour django
FROM python:3.11

#définir le répertoire de travail
WORKDIR /app

#installation des dépendances
COPY requirements.txt /app/
RUN pip install -r requirements.txt

#copier le code source
COPY . /app/

#commandes lancées à l'exécutiuon
CMD [ "sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:${PORT}" ]