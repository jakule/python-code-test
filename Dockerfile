FROM alpine:3.6

RUN apk add --update py3-pip python3 postgresql postgresql-dev zlib-dev libjpeg-turbo-dev gcc python3-dev musl-dev make \
 && pip3 install --upgrade pip pipenv
RUN if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi

WORKDIR /srv/python-code-test
ADD Pipfile /srv/python-code-test/
ADD Pipfile.lock /srv/python-code-test/
RUN pipenv install --deploy --system