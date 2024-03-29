FROM python:3

WORKDIR /app

COPY requirements.txt .

COPY . ./

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "flaskapi.py"]