FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3-pip
COPY . /microservice_cep
WORKDIR /microservice_cep
RUN pip3 install flask virtualenv Flask-RESTful==0.3.6 gunicorn==19.8.1
RUN virtualenv --python=python3 venv
ENV FLASK_APP=microservice_cep 
ENV PLATAFORMA_SETTINGS=../settings.cfg 
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

CMD ["python3", "run.py"]