# syntax=docker/dockerfile:1

FROM python:3.10-alpine
WORKDIR /flask
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pwd
RUN ls -a
EXPOSE 5000
COPY . . 
RUN python -m flask --app board init-db
CMD ["python", "-m", "flask", "--app", "board", "run", "--host=0.0.0.0", "--debug"]