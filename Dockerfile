FROM debian:bookworm-20221219-slim

RUN apt-get -y update
RUN apt-get -y install certbot python3-certbot-dns-standalone
RUN apt-get clean

EXPOSE 80 443 53

ENTRYPOINT [ "certbot" ]

VOLUME /etc/letsencrypt /var/lib/letsencrypt

WORKDIR /opt/certbot
