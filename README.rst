eea.usersdb
===========

Library to access the EIONET users database, stored in LDAP.

    >>> import eea.usersdb
    >>> users_db = eea.usersdb.UsersDB(ldap_server='ldap2.eionet.europa.eu')
    >>> print users_db.user_info('someuserid')
    ... {'id': 'someuserid', 'full_name': ...}

Changes
=======

1.0.1 (2011-04-06)
------------------

- Backport to Python 2.4.

1.0 (2011-03-07)
----------------

- Initial version.
