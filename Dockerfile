FROM python:3.8

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 1337

USER 1000

CMD [ "python", "./main.py" ]
