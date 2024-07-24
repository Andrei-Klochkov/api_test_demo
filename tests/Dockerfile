FROM alpine

SHELL ["/bin/sh", "-c"]

WORKDIR /usr/tests

COPY tests/ tests/
COPY settings.env .
COPY data/ data/

RUN apk update && \
    apk add --update --no-cache python3 && \
    apk add --update --no-cache py3-pip && \
    python -m venv .venv && \
    source .venv/bin/activate && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r tests/requirements.txt && \
    sed -i 's!^TEST_HOST = .*$!TEST_HOST = simple_api_app!' settings.env

CMD source .venv/bin/activate; \
    pytest -s -v tests/; \
    /bin/sh