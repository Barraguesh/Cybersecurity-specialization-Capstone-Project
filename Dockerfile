FROM python:3.6-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers gcc musl-dev libressl-dev libffi-dev python3-dev rust cargo openssl-dev sqlite
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /notsignal
COPY ./notsignal /notsignal
WORKDIR /notsignal
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/

RUN adduser -D localapp
RUN chown -R localapp:localapp /vol
RUN chmod -R 755 /vol/web
USER localapp

CMD ["entrypoint.sh"]