FROM certbot/certbot

EXPOSE 53

COPY . /opt/certbot/src/standalone-dns

RUN python tools/pip_install.py --no-cache-dir --editable /opt/certbot/src/standalone-dns
