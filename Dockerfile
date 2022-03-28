FROM alpine

COPY requirements.txt /home/requirements.txt

RUN apk update && \
    apk add --no-cache python3 py3-pip && \
    apk add build-base && \
    apk add python3-dev && \
    pip install -r /home/requirements.txt && \
    adduser -D -s /bin/ash runner

COPY src /home/trend-tracker/src
COPY run.sh /home/trend-tracker/
#COPY .env /home/trend-tracker/

RUN chown -R runner:runner /home/trend-tracker/

EXPOSE 8000

USER runner

WORKDIR /home/trend-tracker/

ENTRYPOINT ["sh", "run.sh"]