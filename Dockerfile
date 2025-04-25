FROM debian:latest
LABEL authors="30team"

WORKDIR /app
COPY app/main.py ./
ENTRYPOINT ["top", "-b"]

CMD ["python", "./main.py"]