FROM python:3.7.4-slim-buster

# WORKDIR /app

# RUN useradd -m -r 2kodev && \
#     chown 2kodev /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

ARG GIT_HASH
ENV PORT=8080
ENV GIT_HASH=${GIT_HASH:-dev}

EXPOSE ${PORT}

COPY . .

# USER 2kodev

CMD uvicorn api:app --reload --host 0.0.0.0 --port ${PORT}