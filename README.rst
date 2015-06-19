GNU social - Open, distributed microblogging
============================================

`GNU social`_ (formerly StatusNet) provides microblogging functionality
similar to Twitter. It uses an open, distributed design that allows
enterprises and individuals to install and control their own services
and data while integrating with other StatusNet instances, SMS, Twitter,
Facebook and XMPP IM clients.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- GNU social configurations:
   
   - Installed from upstream source code to /var/www/gnusocial

- SSL support out of the box.
- `Adminer`_ administration frontend for MySQL (listening on port
  12322 - uses SSL).
- Postfix MTA (bound to localhost) to allow sending of email from web
  applications (e.g., password recovery)
- Webmin modules for configuring Apache2, PHP, MySQL and Postfix.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL, phpMyAdmin: username **root**


.. _GNU social: https://gnu.io/social/
.. _TurnKey Core: http://www.turnkeylinux.org/core
.. _Adminer: http://www.adminer.org/
