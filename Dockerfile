FROM continuumio/anaconda3:4.4.0
COPY . /usr/flask_api/
EXPOSE 5000
WORKDIR /usr/flask_api/
RUN pip install -r requirements.txt
CMD python flask_api.py
