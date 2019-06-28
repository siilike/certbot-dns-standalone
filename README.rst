Standalone DNS Authenticator plugin for Certbot
===============================================

This is a plugin that uses an integrated DNS server to respond to the
``_acme-challenge`` records. Simultaneous challenges are supported.

A subdomain with the relevant NS and A records needs to be set up, e.g.
for ``acme.example.com``:

::

    acme     IN  NS  ns.acme.example.com.
    ns.acme  IN  A   1.2.3.4

where 1.2.3.4 is the IP of the server where certbot will be run. Port
53 needs to be available for use, so a DNS server cannot be run there.

Next, ``_acme-challenge`` for the domain that the certificate is
requested for must be configured as a CNAME record to
``domain.acme.example.com``, e.g. for ``example.net``:

::

    _acme-challenge  IN  CNAME  example.net.acme.example.com.

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
    Please enter in your domain name(s) (comma and/or space separated)  (Enter 'c' to cancel): ...

Certbot currently needs to be run as root as it needs to bind to port 53.
