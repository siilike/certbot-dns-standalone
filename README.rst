Standalone DNS Authenticator plugin for Certbot
===============================================

This is a plugin that uses an integrated DNS server to respond to the
``_acme-challenge`` records. Simultaneous challenges are supported.

A subdomain needs to be created that defines certbot as its nameserver,
e.g. for ``acme.example.com``:

::

    acme     IN  NS  ns-acme.example.com.
    ns-acme  IN  A   1.2.3.4

where 1.2.3.4 is the IP of the server where certbot will be run. This
configuration directs any requests to ``*.acme.example.com`` to 1.2.3.4
where the plugin will respond with the relevant challenge.

Any server can be used as long as port 53 is available which means that
a DNS server cannot be run at that particular IP at the same time.

The plugin binds to all available interfaces. The validation usually
takes less than a second.

Next, ``_acme-challenge`` for the domain that the certificate is
requested for must be configured as a CNAME record to
``domain.acme.example.com``, e.g. for ``example.net``:

::

    _acme-challenge  IN  CNAME  example.net.acme.example.com.

This means that any requests to ``_acme-challenge.example.net`` should
be performed to ``example.net.acme.example.com`` instead which is where
our certbot runs. No further changes to the DNS of ``example.net`` are
necessary.

Installation
============

::

    # pip3 install certbot certbot-dns-standalone

Usage
=====

Just run ``certbot certonly`` and use the
``certbot-dns-standalone:dns-standalone`` plugin:

::

    # certbot certonly
    Saving debug log to /var/log/letsencrypt/letsencrypt.log

    How would you like to authenticate with the ACME CA?
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    1: Obtain certificates using an integrated DNS server
    (certbot-dns-standalone:dns-standalone)
    2: Spin up a temporary webserver (standalone)
    3: Place files in webroot directory (webroot)
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Select the appropriate number [1-3] then [enter] (press 'c' to cancel): 1
    Plugins selected: Authenticator certbot-dns-standalone:dns-standalone, Installer None
    Please enter in your domain name(s) (comma and/or space separated)  (Enter 'c' to cancel): *.example.net

Non-interactive usage:

::

    certbot --non-interactive --agree-tos --email certmaster@example.com certonly \
      --preferred-challenges dns --authenticator certbot-dns-standalone:dns-standalone \
      --certbot-dns-standalone:dns-standalone-address=0.0.0.0 \
      --certbot-dns-standalone:dns-standalone-ipv6-address=:: \
      --certbot-dns-standalone:dns-standalone-port=53 \
      -d example.com

To renew the certificates add ``certbot renew`` to ``crontab``.

Parameters supported
--------------------

Parameters can be specified as ``--certbot-dns-standalone:dns-standalone-PARAMETER=VALUE``.

Supported parameters are:

  * ``address`` -- IPv4 address to bind to, defaults to ``0.0.0.0``
  * ``ipv6-address`` -- IPv6 address to bind to, defaults to ``::``
  * ``port`` -- port to use, defaults to 53
