FROM python:3.6

COPY . /src
WORKDIR /src

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt
EXPOSE 5000

CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:5000", "run:app", "dev_tools/config.yml"]