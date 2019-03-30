Standalone DNS Authenticator plugin for Certbot
===============================================

This is a plugin that uses an integrated DNS server to respond to the
``_acme-challenge`` records. Simultaneous challenges are supported.

A subdomain with the relevant NS and A records needs to be set up, e.g.
for ``acme.example.com``:

::

    acme     IN  NS  ns.acme.example.com.
    ns.acme  IN  A   1.2.3.4

and then ``_acme-challenge`` for the domain that the certificate is
requested for configured as a CNAME record to
``domain.acme.example.com``.

::

    _acme-challenge  IN  CNAME  example.net.acme.example.com.

Installation
============

::

    # pip3 install certbot certbot-dns-standalone

Usage
=====

Just run ``certbot certonly`` and use the
``certbot-dns-standalone:dns-standalone`` plugin.

Certbot needs to be run as root as it needs to bind to port 53.
