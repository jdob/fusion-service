FROM python:3

EXPOSE 8000

RUN mkdir /code
WORKDIR /code

ADD fusion /code/fusion
ADD requirements.txt /code/
ADD manage.py /code/
ADD setup.py /code/

RUN pip install -r requirements.txt
RUN pip install -e .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
