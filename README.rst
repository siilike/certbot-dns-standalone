Standalone DNS Authenticator plugin for Certbot
===============================================

This is a plugin that uses an integrated DNS server to respond to the
``_acme-challenge`` records, so the domain's records do not have to be
modified.

Installation
============

pip
---

::

    # pip3 install certbot certbot-dns-standalone

snap
----

::

    # snap install certbot certbot-dns-standalone
    # snap set certbot trust-plugin-with-root=ok
    # snap connect certbot:plugin certbot-dns-standalone
    # snap connect certbot-dns-standalone:certbot-metadata certbot:certbot-metadata

Debian
------

::

    # apt-get install certbot python3-certbot-dns-standalone

Usage
=====

First, you need to pick a central address for certbot, e.g.
``acme.example.com``.

Next, the ``_acme-challenge`` records need to be pointed to
``$domain.acme.example.com`` using CNAME records, e.g. for ``example.net``:

::

    _acme-challenge  IN  CNAME  example.net.acme.example.com.

Finally, you need to point ``*.acme.example.com`` to certbot. There are two
options for that.

Firstly, if you have an IP address with port ``53`` available, you could
configure it as the nameserver for ``acme.example.com``:

::

    acme     IN  NS  ns.acme.example.com.
    ns.acme  IN  A   1.2.3.4

where ``1.2.3.4`` is the IP of the server where certbot will be run. This
configuration directs any requests to ``*.acme.example.com`` to ``1.2.3.4``
where the plugin will respond with the relevant challenge.

Any server can be used as long as port ``53`` is available which means that
a DNS server cannot be run at that particular IP at the same time.

You can then run certbot as follows:

::

    certbot --non-interactive --agree-tos --email certmaster@example.com certonly \
      --preferred-challenges dns --authenticator dns-standalone \
      --dns-standalone-address=1.2.3.4 \
      -d example.net -d '*.example.net'

Secondly, if you already run a DNS server you could configure it to forward
all requests to ``*.acme.example.com`` to another IP/port instead where you
would run certbot.

With Knot DNS you can use ``mod-dnsproxy``:

::

    remote:
      - id: certbot
        address: 127.0.0.1@5555

    mod-dnsproxy:
      - id: certbot
        remote: certbot
        fallback: off

    zone:
      - domain: acme.example.com
        module: mod-dnsproxy/certbot

Using this configuration all requests to ``*.acme.example.com`` are directed
to ``127.0.0.1`` port ``5555``.

You can then run certbot as follows:

::

    certbot --non-interactive --agree-tos --email certmaster@example.com certonly \
      --preferred-challenges dns --authenticator dns-standalone \
      --dns-standalone-address=127.0.0.1 \
      --dns-standalone-port=5555 \
      -d example.net -d '*.example.net'

By default the plugin binds to all available interfaces. The validation usually
takes less than a second.

To renew the certificates add ``certbot renew`` to ``crontab``.

Usage with Docker
=================

First, build the certbot image:

::

    docker build -t certbot /path/to/certbot-dns-standalone/

Next, the certificate:

::

    docker run -it --rm --name certbot \
      -v "/etc/letsencrypt:/etc/letsencrypt" \
      -v "/var/lib/letsencrypt:/var/lib/letsencrypt" \
      -p 8080:80 -p 1.2.3.4:53:53/tcp -p 1.2.3.4:53:53/udp \
      certbot certonly

where ``1.2.3.4`` is the IP address to use for responding the challenges. HTTP
challenges should be directed to port ``8080``.

``/etc/letsencrypt`` and ``/var/lib/letsencrypt`` need to be mapped to
permanent storage.

Supported parameters
====================

Parameters can be specified as ``--dns-standalone-PARAMETER=VALUE``. For older
certbot versions it should be
``--certbot-dns-standalone:dns-standalone-PARAMETER=VALUE``.

Supported parameters are:

* ``address`` -- IPv4 address to bind to, defaults to ``0.0.0.0``
* ``ipv6-address`` -- IPv6 address to bind to, defaults to ``::``
* ``port`` -- port to use, defaults to ``53``

The relevant parameters in ``/etc/letsencrypt/renewal/*.conf`` are
``dns_standalone_address``, ``dns_standalone_port`` and
``dns_standalone_ipv6_address``.

Third party projects
====================

Third party projects integrating certbot-dns-standalone:

* `CertCache <https://github.com/93million/certcache>`_
