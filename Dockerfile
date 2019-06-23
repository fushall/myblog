FROM python

COPY . /myblog/

RUN pip install -r /myblog/requirements.txt

WORKDIR /myblog

ENV FLASK_APP=manage.py

CMD flask run