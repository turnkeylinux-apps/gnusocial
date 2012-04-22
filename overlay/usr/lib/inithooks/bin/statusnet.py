#!/usr/bin/python
"""Set StatusNet domain, administrator password and email

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively
    --domain=   unless provided, will ask interactively
                DEFAULT=www.example.com

"""

import re
import sys
import getopt
import hashlib

from dialog_wrapper import Dialog
from mysqlconf import MySQL

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

DEFAULT_DOMAIN="www.example.com"

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email=', 'domain='])
    except getopt.GetoptError, e:
        usage(e)

    email = ""
    domain = ""
    password = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val
        elif opt == '--domain':
            domain = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "StatusNet Password",
            "Enter new password for the StatusNet 'administrator' account.")

    if not email:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        email = d.get_email(
            "StatusNet Email",
            "Please enter email address for the StatusNet 'administrator' account.",
            "admin@example.com")

    if not domain:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        domain = d.get_input(
            "StatusNet Domain",
            "Enter the domain to serve StatusNet",
            DEFAULT_DOMAIN)

    if domain == "DEFAULT":
        domain = DEFAULT_DOMAIN
    
    hashpass = hashlib.md5(password + '1').hexdigest()   # userid

    m = MySQL()
    m.execute('UPDATE statusnet.user SET email=\"%s\" WHERE nickname=\"administrator\";' % email)
    m.execute('UPDATE statusnet.user SET password=\"%s\" WHERE nickname=\"administrator\";' % hashpass)
    m.execute('UPDATE statusnet.user SET uri=\"http://%s/user/1\" WHERE nickname=\"administrator\";' % domain)

    new = []
    config = "/var/www/statusnet/config.php"
    for s in file(config).readlines():
        s = s.rstrip()
        s = re.sub("\['server'\](.*);", "['server'] = '%s';" % domain, s)
        new.append(s)

    fh = file(config, "w")
    print >> fh, "\n".join(new)
    fh.close()

if __name__ == "__main__":
    main()

