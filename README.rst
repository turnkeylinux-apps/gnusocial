GNU social - Open, distributed microblogging
============================================

`GNU social`_ (formerly StatusNet) provides microblogging functionality
similar to Twitter. It uses an open, distributed design that allows
enterprises and individuals to install and control their own services
and data while integrating with other GNU Social instances, SMS, Twitter,
Facebook and XMPP IM clients.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- GNU social configurations:
   
   - Installed from upstream source code to /var/www/gnusocial

     **Security note**: Updates to GNU social may require supervision so
     they **ARE NOT** configured to install automatically. See `GNU social
     documentation`_ for upgrading.

- SSL support out of the box.
- `Adminer`_ administration frontend for MySQL (listening on port
  12322 - uses SSL).
- Postfix MTA (bound to localhost) to allow sending of email from web
  applications (e.g., password recovery)
- Webmin modules for configuring Apache2, PHP, MySQL and Postfix.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL: username **root**
-  Adminer: username **adminer**


.. _GNU social: https://gnusocial.rocks/
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _GNU social documentation: ~~https://git.gnu.io/gnu/gnu-social/blob/master/UPGRADE~~ *(find new location)*
.. _Adminer: https://www.adminer.org/
