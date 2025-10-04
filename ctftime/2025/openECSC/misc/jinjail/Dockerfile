FROM alpine

RUN apk add py3-flask

COPY flag.txt /flag.txt

WORKDIR /app

COPY app.py .

CMD ["python3", "/app/app.py"]
