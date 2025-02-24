FROM certbot/certbot

ENTRYPOINT [ "certbot" ]
EXPOSE 80 443
VOLUME /etc/letsencrypt /var/lib/letsencrypt
WORKDIR /opt/certbot

COPY . /opt/certbot/src/plugin
RUN python tools/pip_install.py --no-cache-dir --editable /opt/certbot/src/plugin
