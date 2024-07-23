FROM alpine

SHELL ["/bin/sh", "-c"]

WORKDIR /usr/test_app

COPY app/ .
COPY settings.env .
COPY data/check_username/result_messages.py data/check_username/

RUN apk update && \
    apk add --update --no-cache python3 && \
    apk add --update --no-cache py3-pip && \
    python -m venv .venv && \
    source .venv/bin/activate && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD source .venv/bin/activate; \
    python src/main.py

EXPOSE 5000:5000